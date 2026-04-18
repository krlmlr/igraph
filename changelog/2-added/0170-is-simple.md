# igraph_is_simple()

`igraph_is_simple()` gained an extra `igraph_bool_t` argument that decides whether edge directions should be considered. Directed graphs with a mutual edge pair are treated as non-simple if this argument is set to `IGRAPH_UNDIRECTED` (which treats the graph as if it was undirected).

---

**Original changelog wording:**

> `igraph_is_simple()` gained an extra `igraph_bool_t` argument that decides whether edge directions should be considered. Directed graphs with a mutual edge pair are treated as non-simple if this argument is set to `IGRAPH_UNDIRECTED` (which treats the graph as if it was undirected).
