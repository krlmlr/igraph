# igraph_community_leiden()

**Category**: Community detection

`igraph_community_leiden()` now takes two `vertex_out_weights` and `vertex_in_weights` parameters in order to support directed graphs, instead of the previous single `node_weights` parameter. To obtain the old behavior for undirected graphs, pass the vertex weights as `vertex_out_weights` and set `vertex_in_weights` to `NULL`.

---

**Original changelog wording:**

> `igraph_community_leiden()` now takes two `vertex_out_weights` and `vertex_in_weights` parameters in order to support directed graphs, instead of the previous single `node_weights` parameter. To obtain the old behavior for undirected graphs, pass the vertex weights as `vertex_out_weights` and set `vertex_in_weights` to `NULL`.
