# igraph_community_edge_betweenness()

`igraph_community_edge_betweenness()` now takes both a `weights` and a `lengths` parameter, and treats edges with large weights as strong connections. Edge weights (interpreted as connection strengths) are used to divide betweenness scores before selecting them for removal as well as for the modularity computation. Edge lengths are used for defining shortest path lengths during the betweenness computation.

---

**Original changelog wording:**

> `igraph_community_edge_betweenness()` now takes both a `weights` and a `lengths` parameter, and treats edges with large weights as strong connections. Edge weights (interpreted as connection strengths) are used to divide betweenness scores before selecting them for removal as well as for the modularity computation. Edge lengths are used for defining shortest path lengths during the betweenness computation.
