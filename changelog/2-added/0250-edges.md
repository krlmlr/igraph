# igraph_edges()

`igraph_edges()` gained a new `igraph_bool_t bycol` argument that determines the order in which the edges are returned. `bycol = false` reproduces the existing behaviour, while `bycol = true` returns the edges suitable for a matrix stored in column-wise order.

---

**Original changelog wording:**

> `igraph_edges()` gained a new `igraph_bool_t bycol` argument that determines the order in which the edges are returned. `bycol = false` reproduces the existing behaviour, while `bycol = true` returns the edges suitable for a matrix stored in column-wise order.
