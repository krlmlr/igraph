# igraph_get_all_simple_paths()

**Category**: Paths and cycles

`igraph_get_all_simple_paths()` returns its results in an integer vector list (`igraph_vector_int_list_t`) instead of a single integer vector.

---

**Original changelog wording:**

> `igraph_get_all_simple_paths()` returns its results in an integer vector list (`igraph_vector_int_list_t`) instead of a single integer vector.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0590-get-all-simple-paths.md
  55    90    51    84  include/igraph_paths.h
  77    55     0     0  src/paths/simple_paths.c
  30    21     3     3  tests/unit/igraph_get_all_simple_paths.c
  81    10     0     0  tests/unit/igraph_get_all_simple_paths.out
```

Notes on remaining differences:
- `include/igraph_paths.h`: Remaining diff (51/84) is from other changelog entries not yet ported (other function signature changes, removal of deprecated functions, copyright header updates, etc.).
- `tests/unit/igraph_get_all_simple_paths.c`: Remaining diff (3/3) is because `IGRAPH_UNLIMITED` (added in changelog/2-added/0360-unlimited.md) is not yet in main-dev; the test uses `-1` instead of `IGRAPH_UNLIMITED` as a minimal adaptation.
