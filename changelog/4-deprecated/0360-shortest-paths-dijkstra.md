# Deprecated `igraph_shortest_paths_dijkstra()` removed

The `igraph_shortest_paths_dijkstra()` alias - deprecated in
favour of `igraph_distances_dijkstra()` since 0.10.0 - has been
removed. Update call sites to use `igraph_distances_dijkstra()`,
which has the same signature and semantics.
