# igraph_distances() and 4 others

**Category**: Paths and cycles

`igraph_distances()`, `igraph_distances_cutoff()`, `igraph_get_shortest_path()`, `igraph_get_shortest_paths()` and `igraph_get_all_shortest_paths()` gained a `weights` argument. The functions now automatically select the appropriate implementation (unweighted, Dijkstra, Bellman-Ford or Johnson) algorithm based on whether weights are present and whether there are negative weights or not. You can still call the individual methods by their more specific names.

---

**Original changelog wording:**

> `igraph_distances()`, `igraph_distances_cutoff()`, `igraph_get_shortest_path()`, `igraph_get_shortest_paths()` and `igraph_get_all_shortest_paths()` gained a `weights` argument. The functions now automatically select the appropriate implementation (unweighted, Dijkstra, Bellman-Ford or Johnson) algorithm based on whether weights are present and whether there are negative weights or not. You can still call the individual methods by their more specific names.
