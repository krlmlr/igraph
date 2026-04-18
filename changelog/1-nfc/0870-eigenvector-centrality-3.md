# igraph_eigenvector_centrality()

**Category**: Warnings and behavioral refinements

`igraph_eigenvector_centrality()` now warns about eigenvector centralities equal to zero, as these indicate a disconnected graph, for which eigenvector centrality is not meaningful.

---

**Original changelog wording:**

> `igraph_eigenvector_centrality()` now warns about eigenvector centralities equal to zero, as these indicate a disconnected graph, for which eigenvector centrality is not meaningful.
