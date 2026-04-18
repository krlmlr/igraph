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
  48   130    42   124  src/misc/conversion.c
```

Notes on remaining differences:
- `changelog/1-nfc/0840-get-stochastic-sparse.md`: Fully resolved (11→0).
- `src/misc/conversion.c`: Reduced from 48/130 to 42/124 (6 lines each). The change ported the doc comment update and `allow_zeros` parameter change. Remaining diffs are unrelated: copyright header, `igraph_get_stochastic()` refactoring, deprecated function removal, error message punctuation, and other function changes.
