# igraph_get_all_simple_paths()

**Category**: Paths and cycles

`igraph_get_all_simple_paths()` now has an additional parameter that allows restricting paths by minimum length as well, and its `mode` parameter was moved to before the path length limit parameters.

---

**Original changelog wording:**

> `igraph_get_all_simple_paths()` now has an additional parameter that allows restricting paths by minimum length as well, and its `mode` parameter was moved to before the path length limit parameters.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0600-get-all-simple-paths-2.md
   3     3     3     3  tests/unit/igraph_get_all_simple_paths.c
```

Notes on remaining differences:
- `tests/unit/igraph_get_all_simple_paths.c`: Remaining diff (3/3) is unchanged — the 3 uses of `-1` for `max_results` will become `IGRAPH_UNLIMITED` when `changelog/2-added/0360-unlimited.md` is ported. This is not part of the current entry.
