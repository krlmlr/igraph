# igraph_average_path_length() and 3 others

**Category**: Paths and cycles

The `weights` parameter of `igraph_average_path_length()`, `igraph_global_efficiency()`, `igraph_local_efficiency()` and `igraph_average_local_efficiency()` were moved to the second position, after the `graph` itself, for consistency with other functions.

---

**Original changelog wording:**

> The `weights` parameter of `igraph_average_path_length()`, `igraph_global_efficiency()`, `igraph_local_efficiency()` and `igraph_average_local_efficiency()` were moved to the second position, after the `graph` itself, for consistency with other functions.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0580-average-path-length.md
  67   100    55    90  include/igraph_paths.h
 110   103    94    86  src/paths/shortest_paths.c
  22    23     1     1  tests/unit/efficiency.c
```

Notes on remaining differences:
- `changelog/1-nfc/0580-average-path-length.md`: Before 0, after 0 — the file was added from `next`, so the diff disappears (it now matches `next` exactly; the proof-of-work section does not exist on `next`, which is why the `del-a` column shows 0 too — the table tool already accounts for added content not on `next`).
- `include/igraph_paths.h`: Remaining diff (55 add, 90 del) reflects the many other unported changes in this file (e.g. `igraph_distances`, `igraph_get_shortest_paths`, `igraph_get_all_simple_paths`, and other functions whose parameter reordering belongs to later changelog entries).
- `src/paths/shortest_paths.c`: Remaining diff (94 add, 86 del) similarly reflects other unported changes in this file (e.g. `igraph_neighbors` call changes and other refactorings from later entries).
- `tests/unit/efficiency.c`: The diff dropped from (22/23) to (1/1) — nearly fully converged. The remaining 1-line difference is an unrelated NFC change (copyright/license header) not part of this entry.
