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
- `changelog/1-nfc/0870-eigenvector-centrality-3.md`: Fully resolved (11→0).
- `src/centrality/eigenvector.c`: Reduced from 25/6 to 5/6 (20-line reduction). Added doc comments for `warn_zero_entries()`, tolerance choice, starting value branches, and zero eigenvalue handling. Remaining diffs (5/6) are from other entries: copyright header, include changes (`igraph_cycles.h`, `math.h`, removing `igraph_isomorphism.h`), and whitespace reformatting.
