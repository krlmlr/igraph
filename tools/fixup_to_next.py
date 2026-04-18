#!/usr/bin/env python3
"""Create fixup commits so the current branch matches next.

For each file that differs between HEAD and next:
  * Stage the change (copy from next, or delete locally).
  * Find the most recent commit reachable from HEAD that touched the file.
  * Commit with `git commit --fixup=<sha>` if one exists, otherwise use a
    distinctive message mentioning the path.
"""

from __future__ import annotations

import subprocess
import sys

TARGET = "next"


def run(args, *, check=True):
    return subprocess.run(args, check=check)


def capture_stdout(args, *, check=True) -> str:
    return subprocess.run(args, check=check, capture_output=True, text=True).stdout


def capture_stdout_bytes(args, *, check=True) -> bytes:
    return subprocess.run(args, check=check, capture_output=True).stdout


def file_exists_in_rev(rev: str, path: str) -> bool:
    return subprocess.run(
        ["git", "cat-file", "-e", f"{rev}:{path}"], capture_output=True
    ).returncode == 0


def differing_files() -> list[str]:
    out = capture_stdout_bytes(
        ["git", "diff", "--no-renames", "-z", "--name-only", "HEAD", TARGET]
    )
    return [p.decode("utf-8") for p in out.split(b"\x00") if p]


def last_touching_commit(path: str) -> str:
    return capture_stdout(
        ["git", "log", "-1", "--format=%H", "HEAD", "--", path]
    ).strip()


def apply_file(path: str) -> None:
    if file_exists_in_rev(TARGET, path):
        run(["git", "checkout", TARGET, "--", path])
        run(["git", "add", "--", path])
    elif file_exists_in_rev("HEAD", path):
        run(["git", "rm", "-f", "--", path])
    else:
        raise RuntimeError(f"File {path!r} is not in HEAD nor in {TARGET}")


def commit_fixup(path: str) -> None:
    sha = last_touching_commit(path)
    if sha:
        run(["git", "commit", "--fixup", sha, "--no-verify"])
    else:
        run(["git", "commit", "-m",
             f"Add file not previously in history: {path}", "--no-verify"])


def verify_clean_against_next() -> None:
    out = capture_stdout(
        ["git", "diff", "--no-renames", "--name-only", "HEAD", TARGET]
    ).strip()
    if out:
        print("Remaining differences vs next:", file=sys.stderr)
        print(out, file=sys.stderr)
        sys.exit(1)


def main() -> int:
    files = differing_files()
    total = len(files)
    print(f"Processing {total} differing files")

    before = int(capture_stdout(["git", "rev-list", "--count", "HEAD"]).strip())

    for i, path in enumerate(files, 1):
        apply_file(path)
        commit_fixup(path)
        if i % 50 == 0 or i == total:
            print(f"  [{i}/{total}] {path}")

    after = int(capture_stdout(["git", "rev-list", "--count", "HEAD"]).strip())
    created = after - before
    print(f"Created {created} commits (expected {total})")
    if created != total:
        sys.exit(f"Commit count mismatch: {created} != {total}")

    verify_clean_against_next()
    print("HEAD now matches next.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
