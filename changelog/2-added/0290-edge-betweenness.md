# igraph_edge_betweenness(), igraph_edge_betweenness_cutoff()

`igraph_edge_betweenness()` and `igraph_edge_betweenness_cutoff()` now have an `eids` parameter to return only a subset of results. This makes their interface consistent with other betweenness functions.

---

**Original changelog wording:**

> `igraph_edge_betweenness()` and `igraph_edge_betweenness_cutoff()` now have an `eids` parameter to return only a subset of results. This makes their interface consistent with other betweenness functions.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0290-edge-betweenness.md
```

Notes on remaining differences:
- This is a changelog-only port. The `eids` parameter for `igraph_edge_betweenness()` and `igraph_edge_betweenness_cutoff()` was already present on `main-dev` from a prior porting effort. Only the changelog file was missing.
