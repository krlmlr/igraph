# igraph_count_loops() and 34 others

**Category**: Finalized experimental functions

The following functions are not experimental any more: `igraph_count_loops()`, `igraph_count_reachable()`, `igraph_degree_correlation_vector`, `igraph_distances_cutoff()`, `igraph_distances_floyd_warshall()`, `igraph_distances_dijkstra_cutoff()`, `igraph_ecc()`, `igraph_enter_safelocale()`, `igraph_exit_safelocale()`, `igraph_feedback_vertex_set()`, `igraph_find_cycle()`, `igraph_get_shortest_path_astar()`, `igraph_graph_power()`, `igraph_hexagonal_lattice()`, `igraph_hypercube()`, `igraph_is_bipartite_coloring()`, `igraph_is_clique()`, `igraph_is_complete()`, `igraph_is_edge_coloring()`, `igraph_is_vertex_coloring()`, `igraph_is_independent_vertex_set()`, `igraph_join()`,`igraph_joint_degree_distribution()`, `igraph_joint_degree_matrix()`, `igraph_joint_type_distribution()`, `igraph_layout_align()`, `igraph_layout_merge_dla()`, `igraph_mean_degree()`, `igraph_radius()`, `igraph_realize_bipartite_degree_sequence()`, `igraph_reachability()`, `igraph_transitive_closure()`, `igraph_tree_from_parent_vector()`, `igraph_triangular_lattice()`, `igraph_vector_intersection_size_sorted()`, `igraph_voronoi()`.

---

**Original changelog wording:**

> The following functions are not experimental any more: `igraph_count_loops()`, `igraph_count_reachable()`, `igraph_degree_correlation_vector`, `igraph_distances_cutoff()`, `igraph_distances_floyd_warshall()`, `igraph_distances_dijkstra_cutoff()`, `igraph_ecc()`, `igraph_enter_safelocale()`, `igraph_exit_safelocale()`, `igraph_feedback_vertex_set()`, `igraph_find_cycle()`, `igraph_get_shortest_path_astar()`, `igraph_graph_power()`, `igraph_hexagonal_lattice()`, `igraph_hypercube()`, `igraph_is_bipartite_coloring()`, `igraph_is_clique()`, `igraph_is_complete()`, `igraph_is_edge_coloring()`, `igraph_is_vertex_coloring()`, `igraph_is_independent_vertex_set()`, `igraph_join()`,`igraph_joint_degree_distribution()`, `igraph_joint_degree_matrix()`, `igraph_joint_type_distribution()`, `igraph_layout_align()`, `igraph_layout_merge_dla()`, `igraph_mean_degree()`, `igraph_radius()`, `igraph_realize_bipartite_degree_sequence()`, `igraph_reachability()`, `igraph_transitive_closure()`, `igraph_tree_from_parent_vector()`, `igraph_triangular_lattice()`, `igraph_vector_intersection_size_sorted()`, `igraph_voronoi()`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0900-count-loops.md
```

Notes on remaining differences:
- `changelog/1-nfc/0900-count-loops.md`: Fully ported (11→0 add). The file now exists on main-dev.
- No code changes were needed because all 35 functions were already finalized (had `IGRAPH_EXPERIMENTAL` removed) on `main-dev` through earlier porting efforts. None of these functions appear in the `IGRAPH_EXPERIMENTAL` list on main-dev.
