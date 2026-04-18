# igraph_sparsemat(), igraph_weighted_sparsemat(), igraph_get_adjacency_sparse()

The deprecated `igraph_sparsemat()` and `igraph_weighted_sparsemat()` functions were removed; use `igraph_get_adjacency_sparse()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_sparsemat()` and `igraph_weighted_sparsemat()` functions were removed; use `igraph_get_adjacency_sparse()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   5     21     5     14  include/igraph_sparsemat.h
 304    279   304    275  interfaces/functions.yaml
  31    301    31     94  src/core/sparsemat.c
```

Notes on remaining differences:
- `include/igraph_sparsemat.h`: del reduced 21→14 (7 lines: two declarations + blank lines). Remaining diff (5 add, 14 del) is from other changelog entries (copyright/license header, `__BEGIN_DECLS`/`__END_DECLS` changes).
- `interfaces/functions.yaml`: del reduced 279→275 (4 lines for entry). Remaining diff is from many other changelog entries.
- `src/core/sparsemat.c`: del reduced 301→94 (207 lines: two public functions + four static helpers + doc comments). Remaining diff (31 add, 94 del) is from other changelog entries (copyright/header, other deprecated function removals, code changes).
