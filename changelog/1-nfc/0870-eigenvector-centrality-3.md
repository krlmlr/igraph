# igraph_eigenvector_centrality()

**Category**: Warnings and behavioral refinements

`igraph_eigenvector_centrality()` now warns about eigenvector centralities equal to zero, as these indicate a disconnected graph, for which eigenvector centrality is not meaningful.

---

**Original changelog wording:**

> `igraph_eigenvector_centrality()` now warns about eigenvector centralities equal to zero, as these indicate a disconnected graph, for which eigenvector centrality is not meaningful.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0870-eigenvector-centrality-3.md
  25     6     5     6  src/centrality/eigenvector.c
```

Notes on remaining differences:
- `changelog/1-nfc/0870-eigenvector-centrality-3.md`: Fully ported (11→0 add).
- `src/centrality/eigenvector.c`: Reduced from 25→5 add. The 20-line reduction reflects the documentation comments added to `warn_zero_entries()`, the zero-degree/zero-strength starting value comments, and the zero-eigenvalue note. The warning function itself already existed on main-dev. Remaining 5 add / 6 del are from other entries: copyright/license header changes.
