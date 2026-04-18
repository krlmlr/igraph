# igraph_adjacency()

`igraph_adjacency()` now treats `IGRAPH_LOOPS_TWICE` as `IGRAPH_LOOPS_ONCE` when the mode is `IGRAPH_ADJ_DIRECTED`, `IGRAPH_ADJ_UPPER` or `IGRAPH_ADJ_LOWER`. For directed graphs, this is for the sake of consistency with the rest of the library where `IGRAPH_LOOPS_TWICE` is considered for undirected graphs only. For the "upper" and "lower" modes, double-counting the diagonal makes no sense because the double-counting artifact appears when you add the _transpose_ of an upper (or lower) diagonal matrix on top of the matrix itself. See Github issue #2501 for more context.

---

**Original changelog wording:**

> `igraph_adjacency()` now treats `IGRAPH_LOOPS_TWICE` as `IGRAPH_LOOPS_ONCE` when the mode is `IGRAPH_ADJ_DIRECTED`, `IGRAPH_ADJ_UPPER` or `IGRAPH_ADJ_LOWER`. For directed graphs, this is for the sake of consistency with the rest of the library where `IGRAPH_LOOPS_TWICE` is considered for undirected graphs only. For the "upper" and "lower" modes, double-counting the diagonal makes no sense because the double-counting artifact appears when you add the _transpose_ of an upper (or lower) diagonal matrix on top of the matrix itself. See Github issue #2501 for more context.
