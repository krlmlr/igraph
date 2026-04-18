# igraph_are_connected(), igraph_are_adjacent()

The deprecated `igraph_are_connected()` was removed. Use `igraph_are_adjacent()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_are_connected()` was removed. Use `igraph_are_adjacent()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0090-are-connected.md
   1    31     1     2  src/graph/basic_query.c
  16    39    16    38  include/igraph_structural.h
 304   321   304   317  interfaces/functions.yaml
  10    16     9    15  tests/CMakeLists.txt
   0     0     1     2  tests/unit/igraph_are_adjacent.c
   0     0     0     0  tests/unit/igraph_are_connected.c
```

Notes on remaining differences:
- `src/graph/basic_query.c`: del reduced 31→2. Remaining 1 add / 2 del are copyright/comment header changes.
- `include/igraph_structural.h`: del reduced 39→38 (1 line). Remaining are copyright/license header changes and other declaration changes from other entries.
- `interfaces/functions.yaml`: del reduced 321→317. Remaining are other deprecated function removals and signature changes.
- `tests/CMakeLists.txt`: del reduced 16→15. Remaining are other test renames/removals.
- `tests/unit/igraph_are_adjacent.c`: 1 add / 2 del remain (copyright header change from a later entry).
- `tests/unit/igraph_are_connected.c`: 0/0 — file fully removed (as on `next`).
