# igraph_get_stochastic_sparse(), igraph_get_stochastic()

**Category**: Warnings and behavioral refinements

`igraph_get_stochastic_sparse()` no longer throws an error when some row or column sums are zero. This brings its behaviour in line with `igraph_get_stochastic()`.

---

**Original changelog wording:**

> `igraph_get_stochastic_sparse()` no longer throws an error when some row or column sums are zero. This brings its behaviour in line with `igraph_get_stochastic()`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0840-get-stochastic-sparse.md
  48   130    46   128  src/misc/conversion.c
```

Notes on remaining differences:
- `changelog/1-nfc/0840-get-stochastic-sparse.md`: Fully ported (11→0 add).
- `src/misc/conversion.c`: Reduced from 48→46 add, 130→128 del. The 2-line reduction corresponds to the `allow_zeros` change from `false` to `true` in both `igraph_sparsemat_normalize_cols` and `igraph_sparsemat_normalize_rows`. Remaining diff (46/128) is from other entries: copyright changes, deprecated function removals (`igraph_get_adjacency`, `igraph_get_stochastic_sparsemat`, `igraph_to_prufer`), doc updates, and other refactoring.
