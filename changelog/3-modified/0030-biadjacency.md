# igraph_biadjacency(), igraph_adjacency()

`igraph_biadjacency()` now truncates non-integer matrix entries to their integer part instead of rounding them up. This brings consistency with related functions such as `igraph_adjacency()`.

---

**Original changelog wording:**

> `igraph_biadjacency()` now truncates non-integer matrix entries to their integer part instead of rounding them up. This brings consistency with related functions such as `igraph_adjacency()`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/3-modified/0030-biadjacency.md
 557   651   557   651  src/misc/bipartite.c
```

Notes on remaining differences:
- `src/misc/bipartite.c`: Same 557 add / 651 del because most remaining diffs are from other entries (deprecated function removal, variable declarations, error handling, bipartite game refactoring, formatting)
- The single `ceil()` → implicit truncation change doesn't show numerically since the remaining diff is large
