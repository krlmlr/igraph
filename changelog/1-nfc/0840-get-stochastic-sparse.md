# igraph_get_stochastic_sparse(), igraph_get_stochastic()

**Category**: Warnings and behavioral refinements

`igraph_get_stochastic_sparse()` no longer throws an error when some row or column sums are zero. This brings its behaviour in line with `igraph_get_stochastic()`.

---

**Original changelog wording:**

> `igraph_get_stochastic_sparse()` no longer throws an error when some row or column sums are zero. This brings its behaviour in line with `igraph_get_stochastic()`.
