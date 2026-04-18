# igraph_eigenvector_centrality(), igraph_centralization_eigenvector_centrality(), igraph_centralization_eigenvector_centrality_tmax()

**Category**: Centralities

`igraph_eigenvector_centrality()`, `igraph_centralization_eigenvector_centrality()` and `igraph_centralization_eigenvector_centrality_tmax()` now use a `mode` parameter with possible values `IGRAPH_OUT`, `IGRAPH_IN` or `IGRAPH_ALL` to control how edge directions are considered. Previously they used a boolean `directed` parameter.

---

**Original changelog wording:**

> `igraph_eigenvector_centrality()`, `igraph_centralization_eigenvector_centrality()` and `igraph_centralization_eigenvector_centrality_tmax()` now use a `mode` parameter with possible values `IGRAPH_OUT`, `IGRAPH_IN` or `IGRAPH_ALL` to control how edge directions are considered. Previously they used a boolean `directed` parameter.
