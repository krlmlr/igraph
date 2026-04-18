#!/usr/bin/env python3
"""
Apply comment-only hunks from origin/next to the working tree.

A "comment hunk" here is defined narrowly: every added line in the
hunk is part of a C-style block comment. Specifically, either the
first added line starts with `/*` (or `/**`) or the last added line
ends with `*/`. Hunks that touch real code lines are left for
later, more careful commits.

Usage:
    python3 tools/apply_comment_hunks.py           # dry run
    python3 tools/apply_comment_hunks.py --apply   # write to disk

The script writes the modified files in place.  Re-running it after
staging + amending should be a no-op.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


def get_diff_hunks():
    """
    Yield (path, hunk_header, old_start, old_count, new_start, new_count, lines) for every hunk in
    `git diff HEAD..origin/next`.
    """
    out = subprocess.run(
        ['git', 'diff', '-U0', 'HEAD..origin/next', '--', ':!/changelog'],
        check=True, capture_output=True, text=True,
    ).stdout
    path = None
    hunk_meta = None
    hunk_lines = []
    header_re = re.compile(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@')
    for line in out.split('\n'):
        if line.startswith('diff --git'):
            if path and hunk_meta:
                yield path, hunk_meta, hunk_lines
            path = None
            hunk_meta = None
            hunk_lines = []
        elif line.startswith('+++ b/'):
            path = line[6:]
        elif line.startswith('@@'):
            if hunk_meta:
                yield path, hunk_meta, hunk_lines
            m = header_re.match(line)
            if not m:
                hunk_meta = None
                hunk_lines = []
                continue
            hunk_meta = (
                line,
                int(m.group(1)),
                int(m.group(2) or 1),
                int(m.group(3)),
                int(m.group(4) or 1),
            )
            hunk_lines = []
        elif hunk_meta is not None:
            hunk_lines.append(line)
    if path and hunk_meta:
        yield path, hunk_meta, hunk_lines


_COMMENT_START = ('/*', '/**')
_COMMENT_LINE = ('*', '//')


def _is_comment_content(line):
    """Does the whole `line` sit inside a C-style block comment?"""
    s = line.strip()
    if not s:
        return True
    # Strip trailing `*/` of a closing comment that occupies the whole line.
    if s == '*/':
        return True
    # Standalone line comments.
    if s.startswith('//'):
        return True
    # Block-comment body: either a continuation line (` * ...`) or an opener
    # (``/* ...``) that does not contain any code after the comment.
    if s.startswith('*'):
        return True
    if s.startswith('/*'):
        # Allow ``/* ... */`` on its own line, but only if nothing follows
        # the closing ``*/``.
        end = s.find('*/')
        if end == -1:
            return True
        return s[end + 2:].strip() == ''
    return False


def is_comment_hunk(hunk_lines):
    """A comment hunk: every added or removed line sits inside a C-style
    block comment, *and* the hunk either opens a new block (first added line
    starts with ``/*``) or closes one (last added line ends with ``*/``).
    Added/removed lines that contain any executable code disqualify the
    hunk, so a body line like ``foo(); /* note */`` is not accepted."""
    added = [l[1:] for l in hunk_lines if l.startswith('+') and not l.startswith('+++')]
    removed = [l[1:] for l in hunk_lines if l.startswith('-') and not l.startswith('---')]
    if not added:
        return False
    first = added[0].lstrip()
    last = added[-1].rstrip()
    if not (first.startswith('/*') or last.endswith('*/')):
        return False
    return all(_is_comment_content(line) for line in added + removed)


def apply_hunk(path, hunk_meta, hunk_lines):
    """Rewrite the hunk in `path`'s working copy using the new-side lines from the diff."""
    _, old_start, old_count, new_start, _ = hunk_meta
    src = Path(path)
    if not src.exists():
        return False, f'missing file: {path}'
    content = src.read_text().split('\n')
    # `old_start` is 1-based; when count == 0 the hunk inserts *after* old_start.
    insert_after = old_count == 0
    idx = old_start - 1 if not insert_after else old_start
    removed = [l[1:] for l in hunk_lines if l.startswith('-') and not l.startswith('---')]
    added = [l[1:] for l in hunk_lines if l.startswith('+') and not l.startswith('+++')]
    actual = content[idx:idx + old_count]
    if actual != removed:
        return False, f'context mismatch at {path}:{old_start}'
    new_content = content[:idx] + added + content[idx + old_count:]
    src.write_text('\n'.join(new_content))
    return True, f'applied @{old_start} ({len(removed)} -> {len(added)})'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true',
                    help='actually write the changes; otherwise just report what would be done')
    ap.add_argument('--file', help='restrict operation to a single file path')
    args = ap.parse_args()

    # Group comment hunks by file, apply bottom-up so earlier hunk
    # line numbers stay valid after a later one is rewritten.
    by_file = {}
    total = 0
    for path, hunk_meta, hunk_lines in get_diff_hunks():
        if args.file and path != args.file:
            continue
        if not is_comment_hunk(hunk_lines):
            continue
        by_file.setdefault(path, []).append((hunk_meta, hunk_lines))
        total += 1

    print(f'Found {total} comment hunks across {len(by_file)} files', file=sys.stderr)
    applied = 0
    for path, hunks in by_file.items():
        hunks.sort(key=lambda h: h[0][1], reverse=True)
        for hunk_meta, hunk_lines in hunks:
            if not args.apply:
                print(f'[dry] {path} @{hunk_meta[1]} ({len(hunk_lines)} hunk lines)')
                continue
            ok, msg = apply_hunk(path, hunk_meta, hunk_lines)
            marker = 'ok ' if ok else 'ERR'
            print(f'{marker} {path}: {msg}')
            if ok:
                applied += 1

    if args.apply:
        print(f'Applied {applied} / {total} hunks', file=sys.stderr)


if __name__ == '__main__':
    main()
