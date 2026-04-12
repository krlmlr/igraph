# igraph_biadjacency(), igraph_adjacency()

`igraph_biadjacency()` now truncates non-integer matrix entries to their integer part instead of rounding them up. This brings consistency with related functions such as `igraph_adjacency()`.

---

**Original changelog wording:**

> `igraph_biadjacency()` now truncates non-integer matrix entries to their integer part instead of rounding them up. This brings consistency with related functions such as `igraph_adjacency()`.
