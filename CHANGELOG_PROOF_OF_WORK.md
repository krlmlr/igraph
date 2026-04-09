# Changelog Reorganization: Proof of Work

This document shows the mapping from original changelog sections to the new four-category structure.

## Category Mapping

| Original Section | New Category |
|---|---|
| Fixed | Non-functional changes |
| Other | Non-functional changes |
| Acknowledgments | Non-functional changes |
| Added | Added functionality |
| Highlights | Added functionality |
| Changed | Modified functionality |
| Breaking changes | Modified functionality |
| Finalized experimental functions | Modified functionality |
| Release notes | Modified functionality |
| Deprecated | Deprecated and removed functionality |
| Removed | Deprecated and removed functionality |
| (items with no subsection) | Modified functionality |

## Detailed Item Mapping

| Original Location | New Location | Item (truncated) |
|---|---|---|
| [1.0.1] / Fixed | Non-functional changes / [1.0.1] | - Eliminated references to `exit()` from the igraph shared library. These were accidentally introduced into igraph 1.0.0 |
| [1.0.1] / Fixed | Non-functional changes / [1.0.1] | - Eliminated references to `std::cout` from the igraph shared library, as required by CRAN. |
| [1.0.1] / Fixed | Non-functional changes / [1.0.1] | - Fixed a bug in `igraph_hub_and_authority_scores()` that printed a warning about zero entries in the result even when t |
| [1.0.1] / Fixed | Non-functional changes / [1.0.1] | - Fixed compilation and tests when Infomap support is disabled. |
| [1.0.1] / Fixed | Non-functional changes / [1.0.1] | - Fixed rare compilation issues on some Apple systems with some non-standard compilers due to incompatibilities between  |
| [1.0.1] / Fixed | Non-functional changes / [1.0.1] | - Fixed inconsistent libf2c prototypes for `s_copy()` and `s_cat()`. This restores compatibility with emscripten. |
| [1.0.1] / Other | Non-functional changes / [1.0.1] | - Documentation improvements. |
| [1.0.1] / Other | Non-functional changes / [1.0.1] | - nanoflann was updated to version 1.9.0 |
| [1.0.0] / Highlights | Added functionality / [1.0.0] | - A more consistent and more predictable API. |
| [1.0.0] / Highlights | Added functionality / [1.0.0] | - Explicit versioning policy. |
| [1.0.0] / Highlights | Added functionality / [1.0.0] | - Several random graph generators, including the Erdős-Rényi generators, can now produce graphs with multi-edges. |
| [1.0.0] / Highlights | Added functionality / [1.0.0] | - Several functions that can generate a large number of results (cliques, cycles, etc.) now have a feature to limit the  |
| [1.0.0] / Highlights | Added functionality / [1.0.0] | - Functionality for generating several kinds of spatial networks. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - igraph now requires a C++ compiler that supports the C++14 standard. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_setup()` is now recommended to be called before using the library. This function may gain essential functions  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_integer_t` was renamed to `igraph_int_t`, but `igraph_integer_t` is kept as an alias and it will remain availa |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_rng_set_default()` now returns a pointer to the previous default RNG. Furthermore, this function now only stor |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - Interruption handlers do not take a `void *` argument anymore; this is relevant to maintainers of higher-level interfa |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - Interruption handlers now return an `igraph_bool_t` instead of an `igraph_error_t`; the returned value must be true if |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_status()`, `igraph_statusf()` and their macro versions (`IGRAPH_STATUS()` and `IGRAPH_STATUSF()`) do not conve |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `RNG_BEGIN()` and `RNG_END()` macros were removed. You are now responsible for seeding the RNG before using any ig |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - Projects that depend on igraph must only include the `<igraph.h>` header. While an igraph installation includes severa |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `IGRAPH_EINVEVECTOR` error code was removed; `igraph_create()` and `igraph_add_edges()` that used to return this e |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `IGRAPH_NONSQUARE` error code was removed; functions that used this error code now return `IGRAPH_EINVAL` instead  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `IGRAPH_EGLP` error code and all other GLP-specific error codes (starting with `IGRAPH_GLP_`) were removed; functi |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `IGRAPH_ELAPACK` error code was removed; functions that used this error code now return `IGRAPH_FAILURE` instead,  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `IGRAPH_CPUTIME` error code was removed in favour of the interruption mechanism built into igraph. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The unused `IGRAPH_EDIVZERO` and `IGRAPH_EATTRIBUTES` error codes were removed with no replacement. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The deprecated error code `IGRAPH_ENEGLOOP` was removed. Use `IGRAPH_ENEGCYCLE` instead. The underlying numerical valu |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - ARPACK-specific error codes (starting with `IGRAPH_ARPACK_...`) were replaced with a single `IGRAPH_EARPACK` error cod |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - A new error code called `IGRAPH_EINVEID` was added for cases when an invalid edge ID was encountered in an edge ID vec |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_strvector_push_back_len()` now takes a length parameter of `size_t` instead of `igraph_int_t`. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_strvector_print()` no longer takes a file parameter. Use `igraph_strvector_fprint()` to print to a file. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_vector_reverse()` no longer returns an error code. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_vector_shuffle()` no longer returns an error code. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_vector_swap()` and `igraph_matrix_swap()` no longer return an error code. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_vector_list_swap()` and `igraph_graph_list_swap()` no longer return an error code. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_vector_swap_elements()` no longer returns an error code. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_vector_list_swap_elements()` and `igraph_graph_list_swap_elements()` no longer return an error code. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_matrix_copy_to()` gained an `igraph_matrix_storage_t storage` parameter that specifies whether the data should |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_vector_view()`, `igraph_matrix_view()`, `igraph_matrix_view_from_vector()`, and `igraph_vector_ptr_view()` now |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_attribute_handler_t` members that formerly took an untyped `igraph_vector_ptr_t` argument are now taking a typ |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The deprecated `IGRAPH_ATTRIBUTE_DEFAULT` value of the `igraph_attribute_type_t` enum was removed. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `gettype` member of `igraph_attribute_table_t` was renamed to `get_type` for consistency with the naming scheme of |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - Attribute table members that retrieve graph, vertex or edge attributes must not clear the incoming result vector any m |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `value` member of `igraph_attribute_record_t` is now a union that can be used to formally treat the associated poi |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_delete_vertices_map()` (formerly called `igraph_delete_vertices_idx()`) and `igraph_induced_subgraph_map()` no |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_edges()` gained a new `igraph_bool_t bycol` argument that determines the order in which the edges are returned |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_neighbors()` and `igraph_vs_adj()` gained two extra arguments, `igraph_loops_t loops` and `igraph_bool_t multi |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_incident()` and `igraph_es_incident()` gained an extra `igraph_loops_t loops` argument to specify what to do w |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `igraph_multiple_t` enum type was removed from the public API as it was essentially a Boolean. The symbolic consta |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_density()` now takes an optional `weights` parameter. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_is_simple()` gained an extra `igraph_bool_t` argument that decides whether edge directions should be considere |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The type of the `loops` argument of `igraph_adjlist_init_complementer()`, `igraph_centralization_degree()`, `igraph_ce |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_get_biadjacency()` now takes a `weights` parameter, and can optionally create weighted biadjacency matrices. |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_adjacency()` now treats `IGRAPH_LOOPS_TWICE` as `IGRAPH_LOOPS_ONCE` when the mode is `IGRAPH_ADJ_DIRECTED`, `I |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_barabasi_game()`, `igraph_barabasi_aging_game()`, `igraph_recent_degree_game()` and `igraph_recent_degree_agin |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_degree_sequence_game()` no longer interprets an empty in-degree vector as a request for generating undirected  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_erdos_renyi_game_gnm()` uses a `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `igraph_bool_t  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_erdos_renyi_game_gnp()` uses a `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `igraph_bool_t  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_bipartite_game_gnm()` gained an `igraph_edge_type_sw_t allowed_edge_types` parameter, and can now uniformly sa |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_bipartite_game_gnp()` gained an `igraph_edge_type_sw_t allowed_edge_types` parameter, and can now sample multi |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_lcf()` was renamed to `igraph_lcf_small()` and `igraph_lcf_vector()` was renamed to `igraph_lcf()`. Now `igrap |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_sbm_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `igraph_bool_t loops` and  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_rewire_edges()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and `multiple` |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_rewire()` now takes an `igraph_edge_type_sw_t allowed_edge_types` parameter to specify whether to create self- |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_rewire()` now takes an optional `igraph_rewiring_stats_t *` output argument. You can pass the appropriate stru |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_watts_strogatz_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and `mu |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_static_fitness_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and `mu |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_static_power_law_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and ` |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_correlated_game()` now takes the graph being constructed as the _first_ argument to remain consistent with oth |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The semantics of the `permutation` argument of `igraph_correlated_game()` and `igraph_correlated_pair_game()` has chan |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_distances()`, `igraph_distances_cutoff()`, `igraph_get_shortest_path()`, `igraph_get_shortest_paths()` and `ig |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_distances_johnson()` now takes an `igraph_neimode_t mode` parameter to determine in which direction paths shou |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The weighted variants of `igraph_diameter()`, `igraph_pseudo_diameter()`, `igraph_radius()`, `igraph_graph_center()`,  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `weights` parameter of `igraph_average_path_length()`, `igraph_global_efficiency()`, `igraph_local_efficiency()` a |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_get_all_simple_paths()` returns its results in an integer vector list (`igraph_vector_int_list_t`) instead of  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_get_all_simple_paths()` now has an additional parameter that allows restricting paths by minimum length as wel |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_get_all_simple_paths()` gained a `max_results` parameter to limit the number of returned results. Pass `1` to  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_simple_cycles()` gained a `max_results` parameter to limit the number of returned results. Pass `1` to return  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_community_edge_betweenness()` now takes both a `weights` and a `lengths` parameter. Edge weights (interpreted  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_community_infomap()` now supports regularization and gained the `is_regularized` and `regularization_strength` |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_community_label_propagation()` gained the `igraph_lpa_variant_t lpa_variant` parameter to allow specification  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_community_leiden()` now takes two `vertex_out_weights` and `vertex_in_weights` parameters in order to support  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `history` parameter of `igraph_community_leading_eigenvector()` is now a pointer to an `igraph_vector_int_t` inste |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_community_optimal_modularity()` now takes a `resolution` parameter and its `weight` parameter was moved to the |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_community_spinglass_single()` now uses `igraph_real_t` for its `inner_links` and `outer_links` output paramete |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_count_automorphisms()` has been renamed to `igraph_count_automorphisms_bliss()` because it has a BLISS-specifi |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_automorphism_group()` has been renamed to `igraph_automorphism_group_bliss()` because it has a BLISS-specific  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_canonical_permutation()` has been renamed to `igraph_canonical_permutation_bliss()` because it has a BLISS-spe |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_subisomorphic_lad()` does not have a CPU time limit parameter any more. If you wish to stop the calculation fr |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The semantics of the `igraph_permute_vertices()` permutation argument has changed: the i-th element of the vector now  |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - As a consequence to the change in the semantics of the `igraph_permute_vertices()` permutation argument, the semantics |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_isoclass_subgraph()` now takes a parameter of type `igraph_vs_t vids` instead of `igraph_vector_int_t vids`. A |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - All betweenness functions got a `normalized` parameter to support normalizing the result by the number of vertex pairs |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_edge_betweenness()` and `igraph_edge_betweenness_cutoff()` now have an `eids` parameter to return only a subse |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_eigenvector_centrality()`, `igraph_centralization_eigenvector_centrality()` and `igraph_centralization_eigenve |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_eigenvector_centrality()`, `igraph_centralization_eigenvector_centrality()` and `igraph_centralization_eigenve |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_hub_and_authority_scores()` no longer has a `scale` parameter. The result is now always scaled so that the lar |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_pagerank()`, `igraph_personalized_pagerank()` and `igraph_personalized_pagerank_vs()` had their parameter orde |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_cliques()`, `igraph_weighed_cliques()`, `igraph_maximal_cliques()`, `igraph_maximal_cliques_file()`, `igraph_m |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_maximal_independent_sets()` received `min_size` and `max_size` parameters that control the range of independen |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_weighted_cliques()` had its parameter ordering standardized: the `igraph_bool_t maximal` parameter now comes b |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_maximal_cliques_callback()` had its parameter ordering standardized: the `igraph_clique_handler_t *cliquehandl |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_layout_sugiyama()` does not return an "extended graph" anymore. The bends in the edges of the layout are encod |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_similarity_jaccard()` and `igraph_similarity_dice()` now take two sets of vertices (`to` and `from` parameters |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_minimum_spanning_tree()` takes a new `method` parameter that controls the algorithm used for finding the spann |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_motifs_randesu_no()` and `igraph_motifs_randesu_estimate()` now take an `igraph_real_t` as their `result` argu |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The `igraph_motifs_handler_t` callback type now takes a `const igraph_vector_int_t *vids` parameter. Previously this w |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - The experimental functions `igraph_fundamental_cycles()` and `igraph_minimum_cycle_basis()` now use the type `igraph_r |
| [1.0.0] / Breaking changes | Modified functionality / [1.0.0] | - `igraph_read_graph_ncol()` and `igraph_read_graph_lgl()` now uses a default edge weight of 1 instead of 0 for files th |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_setup()` performs all initialization tasks that are recommended before using the igraph library. Right now thi |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_iea_game()` samples random multigraphs through independent edge assignment. |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_bipartite_iea_game()` samples random bipartite multigraph through independent edge assignment. |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_weighted_biadjacency()` creates a weighted graph from a bipartite adjacency matrix. |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_vector_ptr_capacity()` returns the allocated capacity of a pointer vector. |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_vector_ptr_resize_min()` deallocates unused capacity of a pointer vector. |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_strvector_fprint()` prints a string vector to a file. |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_rng_sample_dirichlet()`, `igraph_rng_sample_sphere_volume()` and `igraph_rng_sample_sphere_surface()` samples  |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_nearest_neighbor_graph()` computes a neighborhood graph of spatial points based on a neighbor count, cutoff di |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_delaunay_graph()` computes a Delaunay graph of a spatial point set (experimental function). Thanks to Arnór Fr |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_gabriel_graph()` computes the Gabriel graph of a spatial point set (experimental function). Thanks to Arnór Fr |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_relative_neighborhood_graph()` computes the relative neighborhood graph of a spatial point set (experimental f |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_lune_beta_skeleton()` and `igraph_circle_beta_skeleton()` compute the lune and circle based β-skeletons of a s |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_beta_weighted_gabriel_graph()` computes a Gabriel graph of a spatial point set, along with a threshold β value |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_spatial_edge_lengths()` computes edge lengths based on spatial vertex coordinates (experimental function). |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_community_leiden_simple()` is a simplified interface to `igraph_community_leiden()` that allows selecting the  |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `igraph_vector_difference_and_intersection_sorted()` calculates the intersection and the differences of two vectors si |
| [1.0.0] / Added | Added functionality / [1.0.0] | - `IGRAPH_UNLIMITED`, defined to `-1`, is a convenience constant for use with various "size limit" parameters, such as n |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - The Pajek format reader and writer now map vertex labels to the `name` vertex attribute in igraph. The `id` attribute  |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - `igraph_minimum_size_separators()` no longer returns any separating vertex sets for complete graphs. Prior to igraph 1 |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - `igraph_community_edge_betweenness()` now treats edges with large weights as strong connections. |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - `igraph_biadjacency()` now truncates non-integer matrix entries to their integer part instead of rounding them up. Thi |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - The order of edges in the graph returned by `igraph_(weighted_)adjacency()` and `igraph_biadjacency()` has changed. No |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - `igraph_eigenvector_centrality()` now warns about eigenvector centralities equal to zero, as these indicate a disconne |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - `igraph_hub_and_authority_scores()` now warns when a large fraction of centrality scores are zero, as this indicates a |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - `igraph_hub_and_authority_scores()` now warns when providing an undirected graph as input, and falls back to the equiv |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - `igraph_get_stochastic_sparse()` no longer throws an error when some row or column sums are zero. This brings its beha |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - `igraph_vector_append()`, `igraph_strvector_append()` and `igraph_vector_ptr_append()` now use a different allocation  |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - The implementation of the Infomap algorithm behind `igraph_community_infomap()` has been updated with a more recent ve |
| [1.0.0] / Changed | Modified functionality / [1.0.0] | - `igraph_vector_difference_sorted()` now handles multisets properly (and documents how the multiplicities are handled). |
| [1.0.0] / Finalized experimental functions | Modified functionality / [1.0.0] | - The following functions are not experimental any more: `igraph_count_loops()`, `igraph_count_reachable()`, `igraph_deg |
| [1.0.0] / Fixed | Non-functional changes / [1.0.0] | - `igraph_community_spinglass_single()` now uses `igraph_real_t` for its `inner_links` and `outer_links` output paramete |
| [1.0.0] / Fixed | Non-functional changes / [1.0.0] | - `igraph_correlated_game()` and `igraph_correlated_pair_game()` validate their `permutation` argument. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - Removed `igraph_Calloc()`, `igraph_Realloc()` and `igraph_Free()`. Use `IGRAPH_CALLOC()`, `IGRAPH_REALLOC()` and `IGRA |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_adjacent_triangles()` was removed. Use `igraph_count_adjacent_triangles()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_are_connected()` was removed. Use `igraph_are_adjacent()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_automorphisms()` was removed. Use `igraph_count_automorphisms()` or `igraph_count_automorphisms |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_convex_hull()` was removed. Use `igraph_convex_hull_2d()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_decompose_destroy()` was removed. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_hub_score()` and `igraph_authority_score()` were removed. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_vs_seq()`, `igraph_vss_seq()`, `igraph_es_seq()`, `igraph_ess_range()`, and `igraph_vector_init |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_erdos_renyi_game()` and `igraph_bipartite_game()` were removed. Use the corresponding functions |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_tree()` was removed. Use `igraph_kary_tree()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_lattice()` was removed. Use `igraph_square_lattice()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_minimum_spanning_tree_prim()` was removed. Use `igraph_minimum_spanning_tree()` in conjunction  |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_minimum_spanning_tree_unweighted()` was removed. Use `igraph_minimum_spanning_tree()` in conjun |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_get_sparsemat()` was removed. Use `igraph_get_adjacency_sparse()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_get_stochastic_sparsemat()` was removed. Use `igraph_get_stochastic_sparse()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_laplacian()` was removed. Use `igraph_get_laplacian()` or `igraph_get_laplacian_sparse()` inste |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_subgraph_edges()` was removed. Use `igraph_subgraph_from_edges()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_read_graph_dimacs()` and `igraph_write_graph_dimacs()` were removed. These names may be re-used |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_isomorphic_function_vf2()` was removed. Use `igraph_get_isomorphisms_vf2_callback()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_subisomorphic_function_vf2()` was removed. Use `igraph_get_subisomorphisms_vf2_callback()` inst |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_isomorphic_34()` was removed. Its functionality is accessible through `igraph_isomorphic()`. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_transitive_closure_dag()` was removed. Use `igraph_transitive_closure()` instead, which works f |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_sparsemat_copy()` was removed. Use `igraph_sparsemat_init_copy()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_sparsemat_eye()` was removed. Use `igraph_sparsemat_init_eye()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_sparsemat_diag()` was removed. Use `igraph_sparsemat_init_diag()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_sparsemat()` and `igraph_weighted_sparsemat()` functions were removed; use `igraph_get_adjacenc |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_random_edge_walk()` was removed. Its functionality is incorporated in `igraph_random_walk()`. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_vector_qsort_ind()` was removed. Use `igraph_vector_sort_ind()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_vector_binsearch2()` was removed. Use `igraph_vector_contains_sorted()` instead. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_vector_copy()` and `igraph_matrix_copy()` were removed. Use `igraph_vector_init_copy()` and `ig |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_vector_e()`, `igraph_vector_e_ptr()`, `igraph_matrix_e()` and `igraph_matrix_e_ptr()` were remo |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_vector_move_interval2()` was removed. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_rng_get_dirichlet()` function was removed. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_zeroin()` was removed. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The deprecated `igraph_deterministic_optimal_imitation()`, `igraph_moran_process()`, `igraph_roulette_wheel_imitation( |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - `igraph_sample_dirichlet()`, `igraph_sample_sphere_surface()` and `igraph_sample_sphere_volume()` were removed in favo |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The unused enum type `igraph_fileformat_type_t` was removed. |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - The macros `IGRAPH_POSINFINITY` and `IGRAPH_NEGINFINITY` were removed. Use `IGRAPH_INFINITY` and `-IGRAPH_INFINITY` in |
| [1.0.0] / Removed | Deprecated and removed functionality / [1.0.0] | - Removed `igraph_sparsemat_view()` as its design was broken and required the user to reach into the internals of `igrap |
| [1.0.0] / Deprecated | Deprecated and removed functionality / [1.0.0] | - `igraph_delete_vertices_idx()` is now deprecated in favour of `igraph_delete_vertices_map()`, which is functionally eq |
| [1.0.0] / Other | Non-functional changes / [1.0.0] | - The documentation was reorganized. |
| [1.0.0] / Other | Non-functional changes / [1.0.0] | - Various documentation improvements. |
| [1.0.0] / Other | Non-functional changes / [1.0.0] | - Improved performance when creating graphs from dense adjacency matrices (`igraph_adjacency()` and `igraph_weighted_adj |
| [0.10.17] - 2025-09-19 / Added | Added functionality / [0.10.17] - 2025-09-19 | - `igraph_layout_align()` attempts to align a graph layout with the coordinate axes in a visually pleasing manner (exper |
| [0.10.17] - 2025-09-19 / Added | Added functionality / [0.10.17] - 2025-09-19 | - `igraph_product()` supports the lexicographic, strong and modular graph products. Thanks to Gulshan Kumar @gulshan-123 |
| [0.10.17] - 2025-09-19 / Added | Added functionality / [0.10.17] - 2025-09-19 | - `igraph_rooted_product()` computes the rooted graph product (experimental function). Thanks to Gulshan Kumar @gulshan- |
| [0.10.17] - 2025-09-19 / Added | Added functionality / [0.10.17] - 2025-09-19 | - `igraph_mycielskian()` (experimental function) and `igraph_mycielski_graph()` compute a Mycielski transformation of a  |
| [0.10.17] - 2025-09-19 / Added | Added functionality / [0.10.17] - 2025-09-19 | - `igraph_path_graph()` is a convenience wrapper for `igraph_ring()` with `circular=false`. |
| [0.10.17] - 2025-09-19 / Added | Added functionality / [0.10.17] - 2025-09-19 | - `igraph_cycle_graph()` is a convenience wrapper for `igraph_ring()` with `circular=true`. |
| [0.10.17] - 2025-09-19 / Added | Added functionality / [0.10.17] - 2025-09-19 | - `igraph_site_percolation()`, `igraph_bond_percolation()` and `igraph_edgelist_percolation()` compute the evolution of  |
| [0.10.17] - 2025-09-19 / Added | Added functionality / [0.10.17] - 2025-09-19 | - `igraph_invert_permutation()` inverts a permutation stored in an integer vector. |
| [0.10.17] - 2025-09-19 / Added | Added functionality / [0.10.17] - 2025-09-19 | - `igraph_is_vertex_coloring()` and `igraph_is_edge_coloring()` check if a vertex or edge coloring is valid, i.e. whethe |
| [0.10.17] - 2025-09-19 / Added | Added functionality / [0.10.17] - 2025-09-19 | - `igraph_is_bipartite_coloring()` checks if a bipartite type assignment is valid, i.e. whether adjacent vertices always |
| [0.10.17] - 2025-09-19 / Added | Added functionality / [0.10.17] - 2025-09-19 | - `igraph_rich_club_sequence()` calculates how the density of a graph changes as vertices are removed (experimental func |
| [0.10.17] - 2025-09-19 / Changed | Modified functionality / [0.10.17] - 2025-09-19 | - `igraph_bipartite_game_gnp()` can now generate graphs with more than a hundred million vertices. Thanks to Dev Lohani  |
| [0.10.17] - 2025-09-19 / Changed | Modified functionality / [0.10.17] - 2025-09-19 | - `igraph_reindex_membership()` now supports arbitrary cluster indices. Previously, it would error when indices are not  |
| [0.10.17] - 2025-09-19 / Changed | Modified functionality / [0.10.17] - 2025-09-19 | - `igraph_modularity()` now supports arbitrary cluster indices. However, ensuring that cluster indices are within the ra |
| [0.10.17] - 2025-09-19 / Fixed | Non-functional changes / [0.10.17] - 2025-09-19 | - Fix failure in SIR simulation due to roundoff errors creating slightly negative rates. |
| [0.10.17] - 2025-09-19 / Fixed | Non-functional changes / [0.10.17] - 2025-09-19 | - Fix infinite coordinates for certain path graphs with `igraph_layout_kamada_kawai_3d()`. |
| [0.10.17] - 2025-09-19 / Fixed | Non-functional changes / [0.10.17] - 2025-09-19 | - `igraph_community_leiden()` did not iterate until the partition ceased to change when `n_iterations < 0`. Thanks to Lu |
| [0.10.17] - 2025-09-19 / Fixed | Non-functional changes / [0.10.17] - 2025-09-19 | - The widest path functions `igraph_widest_path_widths_floyd_warshall()`, `igraph_widest_path_widths_dijkstra()`, `igrap |
| [0.10.17] - 2025-09-19 / Fixed | Non-functional changes / [0.10.17] - 2025-09-19 | - `igraph_cliques_callback()` would sometimes fail to respect a request to stop (i.e. returning `IGRAPH_STOP`) from the  |
| [0.10.17] - 2025-09-19 / Fixed | Non-functional changes / [0.10.17] - 2025-09-19 | - `igraph_hypercube()` now validates the hypercube dimension and prevents negative values. |
| [0.10.17] - 2025-09-19 / Fixed | Non-functional changes / [0.10.17] - 2025-09-19 | - `igraph_sparsemat_view()` checks for out-of-memory conditions. |
| [0.10.17] - 2025-09-19 / Fixed | Non-functional changes / [0.10.17] - 2025-09-19 | - Fix assertion error when stopping search early in `igraph_simple_cycles_callback()` by returning `IGRAPH_STOP` from th |
| [0.10.17] - 2025-09-19 / Deprecated | Deprecated and removed functionality / [0.10.17] - 2025-09-19 | - `igraph_sparsemat()` and `igraph_weighted_sparsemat()` are now deprecated; their functionality is duplicated by `igrap |
| [0.10.17] - 2025-09-19 / Deprecated | Deprecated and removed functionality / [0.10.17] - 2025-09-19 | - `igraph_convex_hull()` is deprecated in favour of `igraph_convex_hull_2d()` and scheduled for removal in 1.0. |
| [0.10.17] - 2025-09-19 / Other | Non-functional changes / [0.10.17] - 2025-09-19 | - Documentation improvements, including a new glossary. |
| [0.10.17] - 2025-09-19 / Other | Non-functional changes / [0.10.17] - 2025-09-19 | - Simple cycle search (`igraph_simple_cycles()` and `igraph_simple_cycles_callback()`) is sped up by skipping cycle sear |
| [0.10.17] - 2025-09-19 / Other | Non-functional changes / [0.10.17] - 2025-09-19 | - `igraph_realize_degree_sequence()` is significantly sped up for simple undirected graphs, and now has near-linear comp |
| [0.10.16] - 2025-06-10 / Added | Added functionality / [0.10.16] - 2025-06-10 | - `igraph_count_triangles()` counts undirected triangles in a graph. |
| [0.10.16] - 2025-06-10 / Added | Added functionality / [0.10.16] - 2025-06-10 | - `igraph_count_adjacent_triangles()` (rename of `igraph_adjacent_triangles()`). |
| [0.10.16] - 2025-06-10 / Added | Added functionality / [0.10.16] - 2025-06-10 | - `igraph_rng_get_bool()` and `RNG_BOOL()` produce a single random boolean. |
| [0.10.16] - 2025-06-10 / Added | Added functionality / [0.10.16] - 2025-06-10 | - `igraph_product()` computes various kinds of graph products of two graphs. Thanks to Gulshan Kumar @gulshan-123 for co |
| [0.10.16] - 2025-06-10 / Changed | Modified functionality / [0.10.16] - 2025-06-10 | - `igraph_neighborhood_size()`, `igraph_neighborhood()` and `igraph_neighborhood_graphs()` now accept a negative `order` |
| [0.10.16] - 2025-06-10 / Changed | Modified functionality / [0.10.16] - 2025-06-10 | - `igraph_famous()` now accepts `Groetzsch` as an alias of `Grotzsch`. |
| [0.10.16] - 2025-06-10 / Changed | Modified functionality / [0.10.16] - 2025-06-10 | - `igraph_vertex_path_from_edge_path()` can now determine the start vertex automatically. |
| [0.10.16] - 2025-06-10 / Fixed | Non-functional changes / [0.10.16] - 2025-06-10 | - `igraph_largest_independent_vertex_sets()` and `igraph_maximal_independent_vertex_sets()` would sometimes return incor |
| [0.10.16] - 2025-06-10 / Fixed | Non-functional changes / [0.10.16] - 2025-06-10 | - `igraph_vertex_path_from_edge_path()` now validates the start vertex. |
| [0.10.16] - 2025-06-10 / Fixed | Non-functional changes / [0.10.16] - 2025-06-10 | - Fixed a memory leak in the GraphML parser for cases when the `id` attribute was specified multiple times within the sa |
| [0.10.16] - 2025-06-10 / Deprecated | Deprecated and removed functionality / [0.10.16] - 2025-06-10 | - The undocumented function `igraph_vector_sumsq()` is deprecated. Use `igraph_blas_dnrm2()` to compute the Euclidean no |
| [0.10.16] - 2025-06-10 / Deprecated | Deprecated and removed functionality / [0.10.16] - 2025-06-10 | - `igraph_adjacent_triangles()` is deprecated and scheduled for removal in 1.0. |
| [0.10.16] - 2025-06-10 / Deprecated | Deprecated and removed functionality / [0.10.16] - 2025-06-10 | - `igraph_deterministic_optimal_imitation()`, `igraph_moran_process()`, `igraph_roulette_wheel_imitation()` and `igraph_ |
| [0.10.16] - 2025-06-10 / Deprecated | Deprecated and removed functionality / [0.10.16] - 2025-06-10 | - `igraph_rng_get_dirichlet()` is deprecated and scheduled for removal in 1.0. Its interface is inconsistent with the ot |
| [0.10.16] - 2025-06-10 / Other | Non-functional changes / [0.10.16] - 2025-06-10 | - Workaround for bug in CMake 3.31.0, see <https://gitlab.kitware.com/cmake/cmake/-/issues/26449> |
| [0.10.16] - 2025-06-10 / Other | Non-functional changes / [0.10.16] - 2025-06-10 | - Updated the vendored `plfit` library to version 1.0.0. This works around a bug in some MSVC / Windows SDK versions tha |
| [0.10.16] - 2025-06-10 / Other | Non-functional changes / [0.10.16] - 2025-06-10 | - Updated vendored BLAS to 3.12.0 and vendored ARPACK to ARPACK-NG 3.7.0. |
| [0.10.16] - 2025-06-10 / Other | Non-functional changes / [0.10.16] - 2025-06-10 | - Re-translated vendored BLAS/LAPACK/ARPACK sources with f2c version 20240504. |
| [0.10.16] - 2025-06-10 / Other | Non-functional changes / [0.10.16] - 2025-06-10 | - The performance of `igraph_transitivity_undirected()` is improved by a factor of about 2.5. |
| [0.10.16] - 2025-06-10 / Other | Non-functional changes / [0.10.16] - 2025-06-10 | - The performance of `igraph_degree_sequence_game()` is improved when using `IGRAPH_DEGSEQ_CONFIGURATION_SIMPLE`. |
| [0.10.16] - 2025-06-10 / Other | Non-functional changes / [0.10.16] - 2025-06-10 | - Documentation improvements and fixes. |
| [0.10.15] / Added | Added functionality / [0.10.15] | - `igraph_bitset_update()` copies the contents of one bitset into another (experimental function). |
| [0.10.15] / Added | Added functionality / [0.10.15] | - `igraph_vector_sort_ind()` (rename of `igraph_vector_qsort_ind()`). |
| [0.10.15] / Added | Added functionality / [0.10.15] | - `igraph_vector_contains_sorted()` (rename of `igraph_vector_binsearch2()`). |
| [0.10.15] / Added | Added functionality / [0.10.15] | - `igraph_vector_reverse_section()` reverses a contiguous section of a vector. |
| [0.10.15] / Added | Added functionality / [0.10.15] | - `igraph_vector_rotate_left()` applies a cyclic permutation to a vector. |
| [0.10.15] / Added | Added functionality / [0.10.15] | - `igraph_strvector_swap_elements()` swaps two strings in an `igraph_strvector_t`. |
| [0.10.15] / Added | Added functionality / [0.10.15] | - `igraph_find_cycle()` finds a single cycle in a graph, if it exists (experimental function). |
| [0.10.15] / Added | Added functionality / [0.10.15] | - `igraph_feedback_vertex_set()` finds a minimum feedback vertex set in a directed or undirected graph (experimental fun |
| [0.10.15] / Added | Added functionality / [0.10.15] | - `igraph_simple_cycles()` and `igraph_simple_cycles_callback()` find all simple cycles in a graph, optionally with an u |
| [0.10.15] / Changed | Modified functionality / [0.10.15] | - `igraph_feedback_arc_set()` uses a much faster method for solving the exact minimum feedback arc set problem. The new  |
| [0.10.15] / Changed | Modified functionality / [0.10.15] | - `igraph_motifs_randesu()`, `igraph_motifs_randesu_callback()`, `igraph_motifs_randesu_estimate()` and `igraph_motifs_r |
| [0.10.15] / Changed | Modified functionality / [0.10.15] | - `igraph_centralization_eigenvector_centrality_tmax()` and `igraph_centralization_eigenvector_centrality()` cannot prod |
| [0.10.15] / Changed | Modified functionality / [0.10.15] | - When `igraph_eigenvector_centrality()` receives a directed acyclic graph as input, it now produces an eigenvector whic |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - `igraph_layout_drl()` and `igraph_layout_drl_3d()` would crash with an assertion failure when interrupted. This is now |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - Removed broken interruption support from `igraph_community_spinglass_single()`. |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - In rare cases `igraph_community_multilevel()` could enter an infinite loop. This is now corrected. |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - Fixed null-dereference in `igraph_community_voronoi()` when requesting `modularity` but not `membership`. |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - Fixed null-dereference in `igraph_community_optimal_modularity()` when requesting `modularity` but not `membership` an |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - `igraph_layout_umap()` and `igraph_layout_umap_3d()` would crash when passing `distances=NULL` and `distances_are_weig |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - `igraph_layout_umap()` and `igraph_layout_umap_3d()` would crash on interruption. This is now fixed. |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - `igraph_read_graph_pajek()` now warns about duplicate vertex IDs in input files. |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - The documented `igraph_strvector_resize_min()` was missing from headers. |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - `igraph_feedback_arc_set()` now validates the edge weights. |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - `igraph_layout_lgl()` was not working correctly since igraph 0.10.0 due to a poor choice of initial coordinates. This  |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - `igraph_centralization_degree_tmax()`, `igraph_centralization_betweenness_tmax()`, `igraph_centralization_closeness_tm |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - `igraph_centralization_degree_tmax()`, `igraph_centralization_betweenness_tmax()`, `igraph_centralization_closeness_tm |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - `igraph_centralization_eigenvector_centrality_tmax()` now returns 0 for the undirected singleton graph. Previous it wo |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - `igraph_motifs_randesu_estimate()` now validates the sample size. |
| [0.10.15] / Fixed | Non-functional changes / [0.10.15] | - `igraph_bipartite_projection_size()` now validates the bipartite `types` vector. |
| [0.10.15] / Deprecated | Deprecated and removed functionality / [0.10.15] | - `igraph_minimum_spanning_tree_prim()` and `igraph_minimum_spanning_tree_unweighted()` are deprecated. Use `igraph_mini |
| [0.10.15] / Deprecated | Deprecated and removed functionality / [0.10.15] | - `igraph_array3_t` and all associated functions are deprecated and scheduled for removal in igraph 1.0. |
| [0.10.15] / Deprecated | Deprecated and removed functionality / [0.10.15] | - `igraph_vector_qsort_ind()` is deprecated in favour of `igraph_vector_sort_ind()`. |
| [0.10.15] / Deprecated | Deprecated and removed functionality / [0.10.15] | - `igraph_vector_binsearch2()` is deprecated in favour of `igraph_vector_contains_sorted()`. |
| [0.10.15] / Deprecated | Deprecated and removed functionality / [0.10.15] | - The error code `IGRAPH_ENEGLOOP` is deprecated in favour of the newly introduced `IGRAPH_ENEGCYCLE`. The underlying in |
| [0.10.15] / Other | Non-functional changes / [0.10.15] | - Fixed multiple memory leaks in benchmark programs. |
| [0.10.15] / Other | Non-functional changes / [0.10.15] | - Documentation improvements. |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_bitset_fill()` sets all elements of a bitset to the same value (experimental function). |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_bitset_null()` clears all elements of a bitset (experimental function). |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_bitset_is_all_zero()`, `igraph_bitset_is_all_one()`, `igraph_bitset_is_any_zero()`, `igraph_bitset_is_any_one( |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_chung_lu_game()` implements the classic Chung-Lu model, as well as a number of its variants (experimental func |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_mean_degree()` computes the average of vertex degrees (experimental function). |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_count_loops()` counts self-loops in the graph (experimental function). |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_is_clique()` checks if all pairs within a set of vertices are connected (experimental function). |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_is_independent_vertex_set()` checks if no pairs within a set of vertices are connected (experimental function) |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_hypercube()` creates a hypercube graph (experimental function). |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_vector_intersection_size_sorted()` counts elements common to two sorted vectors (experimental function). |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_stack_capacity()` returns the allocated capacity of a stack. |
| [0.10.13] / Added | Added functionality / [0.10.13] | - `igraph_vector_is_all_finite()` checks if all elements in a vector are finite (i.e. neither NaN nor Inf). |
| [0.10.13] / Fixed | Non-functional changes / [0.10.13] | - Fixed a bug that incorrectly cached that a graph has no multiple edges when `igraph_init_adjlist()` was called with `I |
| [0.10.13] / Fixed | Non-functional changes / [0.10.13] | - `igraph_is_forest()` would fail to set the result variable when testing for a directed forest, and it was already cach |
| [0.10.13] / Fixed | Non-functional changes / [0.10.13] | - `igraph_hub_and_authority_scores()` no longer clips negative results to zeros when negative weights are present. |
| [0.10.13] / Fixed | Non-functional changes / [0.10.13] | - Fixed an assertion failure in `igraph_realize_bipartite_degree_sequence()` with some non-graphical degree sequences wh |
| [0.10.13] / Fixed | Non-functional changes / [0.10.13] | - `igraph_static_fitness_game()` checks the input more carefully, and avoids an infinite loop in rare edge cases, such a |
| [0.10.13] / Fixed | Non-functional changes / [0.10.13] | - `igraph_arpack_rnsolve()` used the incorrect error message text for some errors. This is now corrected. |
| [0.10.13] / Fixed | Non-functional changes / [0.10.13] | - Corrected the detection of some MSVC-specific bitset intrinsics during configuration. |
| [0.10.13] / Fixed | Non-functional changes / [0.10.13] | - Corrected a bug in the fallback implementation of `igraph_bitset_countl_zero()` when `IGRAPH_INTEGER_SIZE` was set to  |
| [0.10.13] / Changed | Modified functionality / [0.10.13] | - `igraph_is_graphical()` and `igraph_is_bigraphical()` are now linear-time in all cases, and generally several times fa |
| [0.10.13] / Changed | Modified functionality / [0.10.13] | - `igraph_erdos_renyi_game_gnp()` can now generate graphs with more than a hundred million vertices. |
| [0.10.13] / Changed | Modified functionality / [0.10.13] | - `igraph_hub_and_authority_scores()` now warns when negative edge weights are present. |
| [0.10.13] / Changed | Modified functionality / [0.10.13] | - `igraph_layout_lgl()` now uses a BFS tree rooted in the vertex specified as `proot` to guide the layout. Previously it |
| [0.10.13] / Changed | Modified functionality / [0.10.13] | - Updated the internal heuristics used by igraph's ARPACK interface, `igraph_arpack_rssolve()` and `igraph_arpack_rnsolv |
| [0.10.13] / Changed | Modified functionality / [0.10.13] | - Updated the initial vector construction in `igraph_hub_and_authority_scores()`, `igraph_eigenvector_centrality()` and  |
| [0.10.13] / Other | Non-functional changes / [0.10.13] | - Documentation improvements. |
| [0.10.13] / Other | Non-functional changes / [0.10.13] | - Reduced the memory usage of several functions by using bitsets instead of boolean vectors. |
| [0.10.13] / Other | Non-functional changes / [0.10.13] | - `igraph_vector_intersect_sorted()` has better performance when the input vector sizes are similar. |
| [0.10.12] - 2024-05-06 / Added | Added functionality / [0.10.12] - 2024-05-06 | - `igraph_transitive_closure()` computes the transitive closure of a graph (experimental function). |
| [0.10.12] - 2024-05-06 / Added | Added functionality / [0.10.12] - 2024-05-06 | - `igraph_reachability()` determines which vertices are reachable from each other in a graph (experimental function). |
| [0.10.12] - 2024-05-06 / Added | Added functionality / [0.10.12] - 2024-05-06 | - `igraph_count_reachable()` counts how many vertices are reachable from each vertex (experimental function). |
| [0.10.12] - 2024-05-06 / Added | Added functionality / [0.10.12] - 2024-05-06 | - Added a bitset data structure, `igraph_bitset_t`, and a set of corresponding functions (experimental functionality). |
| [0.10.12] - 2024-05-06 / Fixed | Non-functional changes / [0.10.12] - 2024-05-06 | - `igraph_community_label_propagation()` is now interruptible. |
| [0.10.12] - 2024-05-06 / Fixed | Non-functional changes / [0.10.12] - 2024-05-06 | - `igraph_is_bipartite()` would on rare occasions return invalid results when the cache was employed. |
| [0.10.12] - 2024-05-06 / Fixed | Non-functional changes / [0.10.12] - 2024-05-06 | - `igraph_weighted_adjacency()` correctly passes through NaN values with `IGRAPH_ADJ_MAX`, and correctly recognizes symm |
| [0.10.12] - 2024-05-06 / Fixed | Non-functional changes / [0.10.12] - 2024-05-06 | - `igraph_read_graph_gml()` can now read GML files that use ids larger than what is representable on 32 bits, provided t |
| [0.10.12] - 2024-05-06 / Fixed | Non-functional changes / [0.10.12] - 2024-05-06 | - Fixed a performance issue in `igraph_read_graph_graphml()` with files containing a very large number of entities, such |
| [0.10.12] - 2024-05-06 / Fixed | Non-functional changes / [0.10.12] - 2024-05-06 | - `igraph_read_graph_pajek()` has improved vertex ID validation that better matches that of Pajek's own behavior. |
| [0.10.12] - 2024-05-06 / Changed | Modified functionality / [0.10.12] - 2024-05-06 | - `igraph_eigenvector_centrality()` no longer issues a warning when the input is directed and weighted. When using this  |
| [0.10.12] - 2024-05-06 / Deprecated | Deprecated and removed functionality / [0.10.12] - 2024-05-06 | - `igraph_transitive_closure_dag()` is deprecated in favour of `igraph_transitive_closure()` |
| [0.10.12] - 2024-05-06 / Other | Non-functional changes / [0.10.12] - 2024-05-06 | - Documentation improvements. |
| [0.10.12] - 2024-05-06 / Other | Non-functional changes / [0.10.12] - 2024-05-06 | - `igraph_strength()` and `igraph_degree(loops=false)` are now faster when calculating values for all vertices (contribu |
| [0.10.11] - 2024-04-02 / Added | Added functionality / [0.10.11] - 2024-04-02 | - `igraph_is_complete()` checks whether there is a connection between all pairs of vertices (experimental function, cont |
| [0.10.11] - 2024-04-02 / Added | Added functionality / [0.10.11] - 2024-04-02 | - `igraph_join()` creates the _join_ of two graphs (experimental function, contributed by Quinn Buratynski @GanzuraTheCo |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - Fixed a corruption of the "finally" stack in `igraph_write_graph_gml()` for certain invalid GML files. |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - Fixed a memory leak in `igraph_write_graph_lgl()` when vertex names were present but edge weights were not. |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - Fixed the handling of duplicate edge IDs in `igraph_subgraph_from_edges()`. |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - Fixed conversion of sparse matrices to dense with `igraph_sparsemat_as_matrix()` when sparse matrix object did not mak |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - `igraph_write_graph_ncol()` and `igraph_write_graph_lgl()` now refuse to write vertex names which would result in an i |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - `igraph_write_graph_gml()` now ignores graph attributes called `edge` or `node` with a warning. Writing these would cr |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - `igraph_disjoint_union()` and `igraph_disjoint_union_many()` now check for overflow. |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - `igraph_read_graph_graphml()` now correctly compares attribute values with certain expected values, meaning that prefi |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - Empty IDs are not allowed any more in `<key>` tags of GraphML files as this is a violation of the GraphML specificatio |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - `igraph_is_separator()` and `igraph_is_minimal_separator()` now work correctly with disconnected graphs. |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - `igraph_linegraph()` now considers self-loops to be self-adjacent in undirected graphs, bringing consistency with how  |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - `igraph_all_st_mincuts()` now correctly returns all minimum cuts. This also fixes a problem with `igraph_minimum_size_ |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - Corrected minor error in `igraph_community_label_propagation()` when adding labels to isolated nodes with some fixed l |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - `igraph_community_spinglass()` no longer crashes when passing an edgeless graph and an empty weight vector. |
| [0.10.11] - 2024-04-02 / Fixed | Non-functional changes / [0.10.11] - 2024-04-02 | - `igraph_rewire()` no longer crashes on graphs with more than three vertices but fewer than two edges. |
| [0.10.11] - 2024-04-02 / Changed | Modified functionality / [0.10.11] - 2024-04-02 | - `igraph_rewire()` on longer throws an error on graphs with fewer than four vertices. These graphs are now returned unc |
| [0.10.11] - 2024-04-02 / Other | Non-functional changes / [0.10.11] - 2024-04-02 | - Performance: `igraph_is_simple()` now makes more granular use of the cache. |
| [0.10.11] - 2024-04-02 / Other | Non-functional changes / [0.10.11] - 2024-04-02 | - Performance: `igraph_degree()` now makes use of the cache when checking for self-loops. |
| [0.10.11] - 2024-04-02 / Other | Non-functional changes / [0.10.11] - 2024-04-02 | - The performance of `igraph_is_minimal_separator()` was improved. |
| [0.10.11] - 2024-04-02 / Other | Non-functional changes / [0.10.11] - 2024-04-02 | - `igraph_is_graphical()` now performs graphicality checks for degree sequences of simple directed graphs in linear time |
| [0.10.11] - 2024-04-02 / Other | Non-functional changes / [0.10.11] - 2024-04-02 | - Documentation improvements. |
| [0.10.10] - 2024-02-13 / Fixed | Non-functional changes / [0.10.10] - 2024-02-13 | - When `igraph_is_forest()` determined that a graph is not a directed forest, and the `roots` output parameter was set t |
| [0.10.10] - 2024-02-13 / Fixed | Non-functional changes / [0.10.10] - 2024-02-13 | - `igraph_spanner()` now correctly ignores edge directions, and no longer crashes on directed graphs. |
| [0.10.10] - 2024-02-13 / Deprecated | Deprecated and removed functionality / [0.10.10] - 2024-02-13 | - `igraph_are_connected()` is renamed to `igraph_are_adjacent()`; the old name is kept available until at least igraph 1 |
| [0.10.10] - 2024-02-13 / Other | Non-functional changes / [0.10.10] - 2024-02-13 | - Documentation improvements. |
| [0.10.9] - 2024-02-02 / Added | Added functionality / [0.10.9] - 2024-02-02 | - `igraph_is_biconnected()` checks if a graph is biconnected. |
| [0.10.9] - 2024-02-02 / Added | Added functionality / [0.10.9] - 2024-02-02 | - `igraph_realize_bipartite_degree_sequence()` constructs a bipartite graph that has the given bidegree sequence, option |
| [0.10.9] - 2024-02-02 / Fixed | Non-functional changes / [0.10.9] - 2024-02-02 | - More robust error handling in HRG code. |
| [0.10.9] - 2024-02-02 / Fixed | Non-functional changes / [0.10.9] - 2024-02-02 | - Fixed infinite loop in `igraph_hrg_sample_many()`. |
| [0.10.9] - 2024-02-02 / Fixed | Non-functional changes / [0.10.9] - 2024-02-02 | - `igraph_community_fastgreedy()` no longer crashes when providing a modularity vector only, but not a merges matrix of  |
| [0.10.9] - 2024-02-02 / Fixed | Non-functional changes / [0.10.9] - 2024-02-02 | - The graph property cache was not initialized correctly on systems where the size of `bool` was not 1 byte (#2477). |
| [0.10.9] - 2024-02-02 / Fixed | Non-functional changes / [0.10.9] - 2024-02-02 | - Compatibility with libxml2 version 2.12 (#2442). |
| [0.10.9] - 2024-02-02 / Deprecated | Deprecated and removed functionality / [0.10.9] - 2024-02-02 | - The macro `STR()` is deprecated; use the function `igraph_strvector_get()` instead. |
| [0.10.9] - 2024-02-02 / Other | Non-functional changes / [0.10.9] - 2024-02-02 | - Performance: Reduced memory usage and improved initialization performance for `igraph_strvector_t`. |
| [0.10.9] - 2024-02-02 / Other | Non-functional changes / [0.10.9] - 2024-02-02 | - Performance: Improved cache use by `igraph_is_bipartite()`. |
| [0.10.9] - 2024-02-02 / Other | Non-functional changes / [0.10.9] - 2024-02-02 | - The documentation is now also generated in Texinfo format. |
| [0.10.9] - 2024-02-02 / Other | Non-functional changes / [0.10.9] - 2024-02-02 | - Documentation improvements. |
| [0.10.8] - 2023-11-17 / Added | Added functionality / [0.10.8] - 2023-11-17 | - `igraph_joint_degree_matrix()` computes the joint degree matrix, i.e. counts connections between vertices of different |
| [0.10.8] - 2023-11-17 / Added | Added functionality / [0.10.8] - 2023-11-17 | - `igraph_joint_degree_distribution()` computes the joint distribution of degrees at either end of edges. |
| [0.10.8] - 2023-11-17 / Added | Added functionality / [0.10.8] - 2023-11-17 | - `igraph_joint_type_distribution()` computes the joint distribution of vertex categories at either end of edges, i.e. t |
| [0.10.8] - 2023-11-17 / Added | Added functionality / [0.10.8] - 2023-11-17 | - `igraph_degree_correlation_vector()` computes the degree correlation function and its various directed generalizations |
| [0.10.8] - 2023-11-17 / Changed | Modified functionality / [0.10.8] - 2023-11-17 | - The behaviour of the Pajek format reader and writer is now more closely aligned with the Pajek software and the reader |
| [0.10.8] - 2023-11-17 / Changed | Modified functionality / [0.10.8] - 2023-11-17 | - The Pajek format writer now encodes newline and quotation mark characters in a Pajek-compatible manner (`\n` and `&#34 |
| [0.10.8] - 2023-11-17 / Changed | Modified functionality / [0.10.8] - 2023-11-17 | - `igraph_avg_nearest_neighbor_degree()` now supports non-simple graphs. |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - Resolved "ignoring duplicate libraries" warning when building tests with Xcode 15 on macOS. |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - Fixed the handling of duplicate vertex IDs in `igraph_induced_subgraph()`. |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - `igraph_vector_which_min()` and `igraph_vector_which_max()` no longer allow zero-length input, which makes them consis |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - `igraph_erdos_renyi_game_gnm()` and `igraph_erdos_renyi_game_gnp()` are now interruptible. |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - `igraph_de_bruijn()` and `igraph_kautz()` are now interruptible. |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - `igraph_full()`, `igraph_full_citation()`, `igraph_full_multipartite()` and `igraph_turan()` are now interruptible. |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - `igraph_avg_nearest_neighbor_degree()` did not compute `knnk` correctly in the weighted case. |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - Fixed variadic arguments of invalid types, which could cause incorrect behaviour with `igraph_matrix_print()`, as well |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - `igraph_subisomorphic_lad()` now returns a single null map when the pattern is the null graph. |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - `igraph_community_spinglass()` now checks its parameters more carefully. |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - `igraph_similarity_dice_pairs()` and `igraph_similarity_jaccard_pairs()` now validate vertex IDs. |
| [0.10.8] - 2023-11-17 / Fixed | Non-functional changes / [0.10.8] - 2023-11-17 | - `igraph_maxflow()` now returns an error code if the source and target vertices are the same. It used to get stuck in a |
| [0.10.8] - 2023-11-17 / Other | Non-functional changes / [0.10.8] - 2023-11-17 | - Updated vendored mini-gmp to 6.3.0. |
| [0.10.8] - 2023-11-17 / Other | Non-functional changes / [0.10.8] - 2023-11-17 | - `igraph_connected_components()` makes better use of the cache, improving overall performance. |
| [0.10.8] - 2023-11-17 / Other | Non-functional changes / [0.10.8] - 2023-11-17 | - Documentation improvements. |
| [0.10.7] - 2023-09-04 / Added | Added functionality / [0.10.7] - 2023-09-04 | - `igraph_radius_dijkstra()` computes the graph radius with weighted edges (experimental function). |
| [0.10.7] - 2023-09-04 / Added | Added functionality / [0.10.7] - 2023-09-04 | - `igraph_graph_center_dijkstra()` computes the graph center, i.e. the set of minimum eccentricity vertices, with weight |
| [0.10.7] - 2023-09-04 / Fixed | Non-functional changes / [0.10.7] - 2023-09-04 | - `igraph_full_bipartite()` now checks for overflow. |
| [0.10.7] - 2023-09-04 / Fixed | Non-functional changes / [0.10.7] - 2023-09-04 | - `igraph_bipartite_game_gnm()` and `igraph_bipartite_game_gnp()` are now more robust to overflow. |
| [0.10.7] - 2023-09-04 / Fixed | Non-functional changes / [0.10.7] - 2023-09-04 | - Bipartite graph creation functions now check input arguments. |
| [0.10.7] - 2023-09-04 / Fixed | Non-functional changes / [0.10.7] - 2023-09-04 | - `igraph_write_graph_dot()` now quotes real numbers written in exponential notation as necessary. |
| [0.10.7] - 2023-09-04 / Fixed | Non-functional changes / [0.10.7] - 2023-09-04 | - Independent vertex set finding functions could trigger the fatal error "Finally stack too large" when called on large  |
| [0.10.7] - 2023-09-04 / Deprecated | Deprecated and removed functionality / [0.10.7] - 2023-09-04 | - `igraph_bipartite_game()` is now deprecated; use `igraph_bipartite_game_gnm()` and `igraph_bipartite_game_gnp()` inste |
| [0.10.7] - 2023-09-04 / Other | Non-functional changes / [0.10.7] - 2023-09-04 | - Documentation improvements. |
| [0.10.6] - 2023-07-13 / Fixed | Non-functional changes / [0.10.6] - 2023-07-13 | - Compatibility with libxml2 2.11. |
| [0.10.6] - 2023-07-13 / Fixed | Non-functional changes / [0.10.6] - 2023-07-13 | - Fixed some converge failures in `igraph_community_voronoi()`. |
| [0.10.6] - 2023-07-13 / Fixed | Non-functional changes / [0.10.6] - 2023-07-13 | - `IGRAPH_CALLOC()` and `IGRAPH_REALLOC()` now check for overflow. |
| [0.10.6] - 2023-07-13 / Fixed | Non-functional changes / [0.10.6] - 2023-07-13 | - CMake packages created with the `install` target of the CMake build system are now relocatable, i.e. the generated `ig |
| [0.10.5] - 2023-06-29 / Added | Added functionality / [0.10.5] - 2023-06-29 | - `igraph_graph_power()` computes the kth power of a graph (experimental function). |
| [0.10.5] - 2023-06-29 / Added | Added functionality / [0.10.5] - 2023-06-29 | - `igraph_community_voronoi()` for detecting communities using Voronoi partitioning (experimental function). |
| [0.10.5] - 2023-06-29 / Changed | Modified functionality / [0.10.5] - 2023-06-29 | - `igraph_community_walktrap()` no longer requires `modularity` and `merges` to be non-NULL when `membership` is non-NUL |
| [0.10.5] - 2023-06-29 / Changed | Modified functionality / [0.10.5] - 2023-06-29 | - `igraph_isomorphic()` now supports multigraphs. |
| [0.10.5] - 2023-06-29 / Changed | Modified functionality / [0.10.5] - 2023-06-29 | - Shortest path related functions now consistently ignore edges with positive infinite weights. |
| [0.10.5] - 2023-06-29 / Fixed | Non-functional changes / [0.10.5] - 2023-06-29 | - `igraph_hub_and_authority_scores()`, `igraph_hub_score()` and `igraph_authority_score()` considered self-loops only on |
| [0.10.5] - 2023-06-29 / Fixed | Non-functional changes / [0.10.5] - 2023-06-29 | - `igraph_community_infomap()` now checks edge and vertex weights for validity. |
| [0.10.5] - 2023-06-29 / Fixed | Non-functional changes / [0.10.5] - 2023-06-29 | - `igraph_minimum_spanning_tree()` and `igraph_minimum_spanning_tree_prim()` now check that edge weights are not NaN. |
| [0.10.5] - 2023-06-29 / Fixed | Non-functional changes / [0.10.5] - 2023-06-29 | - Fixed an initialization error in the string attribute combiner of the C attribute handler. |
| [0.10.5] - 2023-06-29 / Fixed | Non-functional changes / [0.10.5] - 2023-06-29 | - Fixed an issue with the weighted clique number calculation when all the weights were the same. |
| [0.10.5] - 2023-06-29 / Fixed | Non-functional changes / [0.10.5] - 2023-06-29 | - HRG functions now require a graph with at least 3 vertices; previous versions crashed with smaller graphs. |
| [0.10.5] - 2023-06-29 / Fixed | Non-functional changes / [0.10.5] - 2023-06-29 | - `igraph_arpack_rssolve()` and `igraph_arpack_rnsolve()`, i.e. the ARPACK interface in igraph, are now interruptible. A |
| [0.10.5] - 2023-06-29 / Fixed | Non-functional changes / [0.10.5] - 2023-06-29 | - `igraph_get_shortest_paths_dijkstra()`, `igraph_get_all_shortest_paths_dijkstra()` and `igraph_get_shortest_paths_bell |
| [0.10.5] - 2023-06-29 / Fixed | Non-functional changes / [0.10.5] - 2023-06-29 | - Fixed bugs in `igraph_local_scan_1_ecount()` for weighted undirected graphs which would miscount loops and multi-edges |
| [0.10.5] - 2023-06-29 / Deprecated | Deprecated and removed functionality / [0.10.5] - 2023-06-29 | - `igraph_automorphisms()` is now deprecated; its new name is `igraph_count_automorphisms()`. The old name is kept avail |
| [0.10.5] - 2023-06-29 / Deprecated | Deprecated and removed functionality / [0.10.5] - 2023-06-29 | - `igraph_hub_score()` and `igraph_authority_score()` are now deprecated. Use `igraph_hub_and_authority_scores()` instea |
| [0.10.5] - 2023-06-29 / Deprecated | Deprecated and removed functionality / [0.10.5] - 2023-06-29 | - `igraph_get_incidence()` is now deprecated; its new name is `igraph_get_biadjacency()` to reflect that the returned ma |
| [0.10.5] - 2023-06-29 / Deprecated | Deprecated and removed functionality / [0.10.5] - 2023-06-29 | - `igraph_hrg_dendrogram()` is deprecated because it requires an attribute handler and it goes against the convention of |
| [0.10.5] - 2023-06-29 / Other | Non-functional changes / [0.10.5] - 2023-06-29 | - Improved performance for `igraph_vertex_connectivity()`. |
| [0.10.5] - 2023-06-29 / Other | Non-functional changes / [0.10.5] - 2023-06-29 | - `igraph_simplify()` makes use of the cache, and avoids simplification when the graph is already known to be simple. |
| [0.10.5] - 2023-06-29 / Other | Non-functional changes / [0.10.5] - 2023-06-29 | - Documentation improvements. |
| [0.10.4] - 2023-01-26 / Added | Added functionality / [0.10.4] - 2023-01-26 | - `igraph_get_shortest_path_astar()` finds a shortest path with the A\* algorithm. |
| [0.10.4] - 2023-01-26 / Added | Added functionality / [0.10.4] - 2023-01-26 | - `igraph_vertex_coloring_greedy()` now supports the DSatur heuristics through `IGRAPH_COLORING_GREEDY_DSATUR` (#2284, t |
| [0.10.4] - 2023-01-26 / Changed | Modified functionality / [0.10.4] - 2023-01-26 | - The `test` build target now only _runs_ the unit tests, but it does not _build_ them. In order to both build and run t |
| [0.10.4] - 2023-01-26 / Changed | Modified functionality / [0.10.4] - 2023-01-26 | - The experimental function `igraph_distances_floyd_warshall()` now has `from` and `to` parameters for choosing source a |
| [0.10.4] - 2023-01-26 / Changed | Modified functionality / [0.10.4] - 2023-01-26 | - The experimental function `igraph_distances_floyd_warshall()` now has an additional `method` parameter to select a spe |
| [0.10.4] - 2023-01-26 / Fixed | Non-functional changes / [0.10.4] - 2023-01-26 | - The Bellman-Ford shortest path finder is now interruptible. |
| [0.10.4] - 2023-01-26 / Fixed | Non-functional changes / [0.10.4] - 2023-01-26 | - The Floyd-Warshall shortest path finder is now interruptible. |
| [0.10.4] - 2023-01-26 / Fixed | Non-functional changes / [0.10.4] - 2023-01-26 | - Running CTest no longer builds the tests automatically, as this interfered with VSCode, which would invoke the `ctest` |
| [0.10.4] - 2023-01-26 / Other | Non-functional changes / [0.10.4] - 2023-01-26 | - Improved the performance and memory usage of `igraph_widest_path_widths_floyd_warshall()`. |
| [0.10.4] - 2023-01-26 / Other | Non-functional changes / [0.10.4] - 2023-01-26 | - Documentation improvements. |
| [0.10.3] - 2022-12-30 / Added | Added functionality / [0.10.3] - 2022-12-30 | - `igraph_matrix_init_array()` to initialize an igraph matrix by copying an existing C array in column-major or row-majo |
| [0.10.3] - 2022-12-30 / Added | Added functionality / [0.10.3] - 2022-12-30 | - `igraph_layout_umap_compute_weights()` computes weights for the UMAP layout algorithm from distances. This used to be  |
| [0.10.3] - 2022-12-30 / Added | Added functionality / [0.10.3] - 2022-12-30 | - `igraph_triangular_lattice()` to generate triangular lattices of various kinds (#2235, thanks to @rfulekjames). |
| [0.10.3] - 2022-12-30 / Added | Added functionality / [0.10.3] - 2022-12-30 | - `igraph_hexagonal_lattice()` to generate hexagonal lattices of various kinds (#2262, thanks to @rfulekjames). |
| [0.10.3] - 2022-12-30 / Added | Added functionality / [0.10.3] - 2022-12-30 | - `igraph_tree_from_parent_vector()` to create a tree or a forest from a parent vector (i.e. a vector that encodes the p |
| [0.10.3] - 2022-12-30 / Added | Added functionality / [0.10.3] - 2022-12-30 | - `igraph_induced_subgraph_edges()` produces the IDs of edges contained within a subgraph induced by the given vertices. |
| [0.10.3] - 2022-12-30 / Changed | Modified functionality / [0.10.3] - 2022-12-30 | - The signature of the experimental `igraph_layout_umap()` function changed; the last argument is now a Boolean that spe |
| [0.10.3] - 2022-12-30 / Fixed | Non-functional changes / [0.10.3] - 2022-12-30 | - `igraph_transitivity_barrat()`, `igraph_community_fluid_communities()`, `igraph_sir()`, `igraph_trussness()` and graph |
| [0.10.3] - 2022-12-30 / Fixed | Non-functional changes / [0.10.3] - 2022-12-30 | - Fixed a bug in `igraph_2dgrid_move()` that sometimes crashed the Large Graph Layout function when a grid cell became e |
| [0.10.3] - 2022-12-30 / Fixed | Non-functional changes / [0.10.3] - 2022-12-30 | - `igraph_pagerank()` and `igraph_personalized_pagerank()` would fail to converge when the ARPACK implementation was use |
| [0.10.3] - 2022-12-30 / Fixed | Non-functional changes / [0.10.3] - 2022-12-30 | - `igraph_pagerank()` and `igraph_personalized_pagerank()` no longer allow negative weights. Previously, edges with nega |
| [0.10.3] - 2022-12-30 / Fixed | Non-functional changes / [0.10.3] - 2022-12-30 | - `igraph_all_st_cuts()` and `igraph_all_st_mincuts()` no longer trigger the "Finally stack too large" fatal error when  |
| [0.10.3] - 2022-12-30 / Fixed | Non-functional changes / [0.10.3] - 2022-12-30 | - `igraph_community_label_propagation()` no longer rounds weights to integers. This was a regression in igraph 0.10. |
| [0.10.3] - 2022-12-30 / Fixed | Non-functional changes / [0.10.3] - 2022-12-30 | - `igraph_read_graph_graphdb()` does more thorough checks on the input file. |
| [0.10.3] - 2022-12-30 / Fixed | Non-functional changes / [0.10.3] - 2022-12-30 | - `igraph_calloc()` did not zero-initialize the allocated memory. This is now corrected. Note that the macro `IGRAPH_CAL |
| [0.10.3] - 2022-12-30 / Fixed | Non-functional changes / [0.10.3] - 2022-12-30 | - Fixed new warnings issued by the Xcode 14.1 toolchain. |
| [0.10.3] - 2022-12-30 / Deprecated | Deprecated and removed functionality / [0.10.3] - 2022-12-30 | - `igraph_subgraph_edges()` is now deprecated to avoid confusion with `igraph_induced_subgraph_edges()`; its new name is |
| [0.10.3] - 2022-12-30 / Other | Non-functional changes / [0.10.3] - 2022-12-30 | - Significantly improved performance for `igraph_matrix_transpose()`. |
| [0.10.3] - 2022-12-30 / Other | Non-functional changes / [0.10.3] - 2022-12-30 | - Documentation improvements. |
| [0.10.2] - 2022-10-14 / Added | Added functionality / [0.10.2] - 2022-10-14 | - `igraph_distances_cutoff()` and `igraph_distances_dijkstra_cutoff()` calculate shortest paths with an upper limit on t |
| [0.10.2] - 2022-10-14 / Added | Added functionality / [0.10.2] - 2022-10-14 | - `igraph_distances_floyd_warshall()` for computing all-pairs shortest path lengths in dense graphs (experimental functi |
| [0.10.2] - 2022-10-14 / Added | Added functionality / [0.10.2] - 2022-10-14 | - `igraph_ecc()` computes the edge clustering coefficient of some edges (experimental function). |
| [0.10.2] - 2022-10-14 / Added | Added functionality / [0.10.2] - 2022-10-14 | - `igraph_voronoi()` computes a Voronoi partitioning of vertices (experimental function). |
| [0.10.2] - 2022-10-14 / Added | Added functionality / [0.10.2] - 2022-10-14 | - `igraph_count_multiple_1()` determines the multiplicity of a single edge in the graph. |
| [0.10.2] - 2022-10-14 / Added | Added functionality / [0.10.2] - 2022-10-14 | - `igraph_dqueue_get()` accesses an element in a queue by index. |
| [0.10.2] - 2022-10-14 / Added | Added functionality / [0.10.2] - 2022-10-14 | - `igraph_degree_1()` efficiently retrieves the degee of a single vertex. |
| [0.10.2] - 2022-10-14 / Added | Added functionality / [0.10.2] - 2022-10-14 | - `igraph_lazy_adjlist_has()` and `igraph_lazy_inclist_has()` to check if adjacent vertices / incident edges have alread |
| [0.10.2] - 2022-10-14 / Changed | Modified functionality / [0.10.2] - 2022-10-14 | - `igraph_edge()` now verifies that the input edge ID is valid. |
| [0.10.2] - 2022-10-14 / Changed | Modified functionality / [0.10.2] - 2022-10-14 | - `igraph_community_leading_eigenvector()`, `igraph_adjacency_spectral_embedding()`, `igraph_laplacian_spectral_embeddin |
| [0.10.2] - 2022-10-14 / Changed | Modified functionality / [0.10.2] - 2022-10-14 | - `igraph_community_leading_eigenvector()` does not stop the splitting process any more when there are multiple equally  |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - Fixed a bug in `igraph_get_k_shortest_paths()` that sometimes yielded incorrect results on undirected graphs when the  |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - `igraph_trussness()` is now interruptible. |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - `igraph_spanner()` is now interruptible. |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - `igraph_layout_umap()` and `igraph_layout_umap3d()` are now interruptible. |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - In some rare cases, roundoff errors would cause `igraph_distance_johnson()` to fail on graphs with negative weights. |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - `igraph_eulerian_cycle()` and `igraph_eulerian_path()` now returns a more specific error code (`IGRAPH_ENOSOL`) when t |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - `igraph_heap_init_array()` did not copy the array data correctly for non-real specializations. |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - `igraph_layout_umap_3d()` now actually uses three dimensions. |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - `igraph_layout_umap()` and `igraph_layout_umap_3d()` are now interruptible. |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - `igraph_vit_create()` and `igraph_eit_create()` no longer fails when trying to create an iterator for the null graph o |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - `igraph_write_graph_leda()` did not correctly print attribute names in some warning messages. |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - Addressed new warnings introduced by Clang 15. |
| [0.10.2] - 2022-10-14 / Fixed | Non-functional changes / [0.10.2] - 2022-10-14 | - In the generated pkg-config file, libxml2 is now placed in the `Requires.private` section instead of the `Libs.private |
| [0.10.2] - 2022-10-14 / Removed | Deprecated and removed functionality / [0.10.2] - 2022-10-14 | - Removed unused and undocumented `igraph_bfgs()` function. |
| [0.10.2] - 2022-10-14 / Removed | Deprecated and removed functionality / [0.10.2] - 2022-10-14 | - Removed the undocumented function `igraph_complex_mod()`. Use `igraph_complex_abs()` instead, as it has identical func |
| [0.10.2] - 2022-10-14 / Deprecated | Deprecated and removed functionality / [0.10.2] - 2022-10-14 | - The `IGRAPH_EDRL` error code was deprecated; the DrL algorithm now returns `IGRAPH_FAILURE` when it used to return `IG |
| [0.10.2] - 2022-10-14 / Deprecated | Deprecated and removed functionality / [0.10.2] - 2022-10-14 | - The undocumented function `igraph_dqueue_e()` is now deprecated and replaced by `igraph_dqueue_get()`. |
| [0.10.2] - 2022-10-14 / Deprecated | Deprecated and removed functionality / [0.10.2] - 2022-10-14 | - `igraph_finite()`, `igraph_is_nan()`, `igraph_is_inf()`, `igraph_is_posinf()` and `igraph_is_neginf()` are now depreca |
| [0.10.2] - 2022-10-14 / Other | Non-functional changes / [0.10.2] - 2022-10-14 | - Documentation improvements. |
| [0.10.1] - 2022-09-08 / Fixed | Non-functional changes / [0.10.1] - 2022-09-08 | - Corrected a regression (compared to igraph 0.9) in weighted clique search functions. |
| [0.10.1] - 2022-09-08 / Fixed | Non-functional changes / [0.10.1] - 2022-09-08 | - `igraph_girth()` no longer fails when the graph has no cycles and the `girth` parameter is set to `NULL`. |
| [0.10.1] - 2022-09-08 / Fixed | Non-functional changes / [0.10.1] - 2022-09-08 | - `igraph_write_graph_gml()` did not respect entity encoding options when writing the `Creator` line. |
| [0.10.1] - 2022-09-08 / Fixed | Non-functional changes / [0.10.1] - 2022-09-08 | - Fixed potential memory leak on out-of-memory condition in `igraph_asymmetric_preference_game()`, `igraph_vs_copy()` an |
| [0.10.1] - 2022-09-08 / Fixed | Non-functional changes / [0.10.1] - 2022-09-08 | - Fixed an assertion failure in `igraph_barabasi_game()` and `igraph_barabasi_aging_game()` when passing in negative deg |
| [0.10.1] - 2022-09-08 / Fixed | Non-functional changes / [0.10.1] - 2022-09-08 | - Fixed a compilation failure with some old Clang versions. |
| [0.10.1] - 2022-09-08 / Changed | Modified functionality / [0.10.1] - 2022-09-08 | - `igraph_write_graph_leda()` can now write boolean attributes. |
| [0.10.1] - 2022-09-08 / Other | Non-functional changes / [0.10.1] - 2022-09-08 | - Support for ARM64 on Windows. |
| [0.10.1] - 2022-09-08 / Other | Non-functional changes / [0.10.1] - 2022-09-08 | - Documentation improvements. |
| [0.10.0] - 2022-09-05 / Release notes | Modified functionality / [0.10.0] - 2022-09-05 | - A consistent use of `igraph_integer_t` for all indices and most integer quantities, both in the API and internally. Th |
| [0.10.0] - 2022-09-05 / Release notes | Modified functionality / [0.10.0] - 2022-09-05 | - The random number generation framework has been overhauled. Sampling from the full range of `igraph_integer_t` is now  |
| [0.10.0] - 2022-09-05 / Release notes | Modified functionality / [0.10.0] - 2022-09-05 | - There is a new fully memory-managed container type for lists of vectors (`igraph_vector_list_t`), replacing most previ |
| [0.10.0] - 2022-09-05 / Release notes | Modified functionality / [0.10.0] - 2022-09-05 | - Some simple graph properties, such as whether a graph contains self-loops or multi-edges, or whether it is connected,  |
| [0.10.0] - 2022-09-05 / Release notes | Modified functionality / [0.10.0] - 2022-09-05 | - File format readers are much more robust and more tolerant of invalid input. |
| [0.10.0] - 2022-09-05 / Release notes | Modified functionality / [0.10.0] - 2022-09-05 | - igraph is much more resilient to overflow errors. |
| [0.10.0] - 2022-09-05 / Release notes | Modified functionality / [0.10.0] - 2022-09-05 | - Many improvements to robustness and reliability, made possible by internal refactorings. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - igraph now requires CMake 3.18 or later. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - In order to facilitate the usage of graphs with more than 2 billion vertices and edges, we have made the size of the ` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_bool_t` is now a C99 `bool` and not an `int`. Similarly, `igraph_vector_bool_t` now consumes `sizeof(bool)` by |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The random number generator interface, `igraph_rng_type_t`, has been overhauled. Check the declaration of the type for |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The default random number generator has been changed from Mersenne Twister to PCG32. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Functions related to spectral coarse graining (i.e. all functions starting with `igraph_scg_...`) were separated into  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Since `igraph_integer_t` aims to be the largest integer size that is feasible on a particular platform, there is no ne |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Generic data types based on `float` were removed as they were not used anywhere in the library. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Several igraph functions that used to take a `long int` or return a `long int` now takes or returns an `igraph_integer |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Similarly, igraph functions that used to accept the `long` variant of a generic igraph data type (e.g., `igraph_vector |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The type `igraph_stack_ptr_t` and its associated functions were removed. Use `igraph_vector_ptr_t` and associated func |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Error handlers should no longer perform a `longjmp()`. Doing so will introduce memory leaks, as resource cleanup is no |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Most callback functions now return an error code. In previous versions they returned a boolean value indicating whethe |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_add_edges()` now uses an `igraph_vector_int_t` for its `edges` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_adjacency()` no longer accepts a negative number of edges in its adjacency matrix. When negative entries are f |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_adjacency()` gained an additional `loops` argument that lets you specify whether the diagonal entries should b |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_all_minimal_st_separators()` now returns the separators in an `igraph_vector_int_list_t` containing `igraph_ve |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_all_st_cuts()` and `igraph_all_st_mincuts()` now return the cuts in an `igraph_vector_int_list_t` containing ` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_arpack_unpack_complex()` now uses `igraph_integer_t` for its `nev` argument instead of `long int`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_articulation_points()` now uses an `igraph_vector_int_t` to return the list of articulation points, not an `ig |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_assortativity_nominal()` now accepts vertex types in an `igraph_vector_int_t` instead of an `igraph_vector_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_asymmetric_preferennce_game()` now uses an `igraph_vector_int_t` to return the types of the nodes in the gener |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_atlas()` now uses `igraph_integer_t` for its `number` argument. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_automorphism_group()` now returns the generators in an `igraph_vector_int_list_t` instead of a pointer vector  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_barabasi_game()`, `igraph_barabasi_aging_game()`, `igraph_recent_degree_game()` and `igraph_recent_degree_agin |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_bfs()` now takes an `igraph_vector_int_t` for its `roots`, `restricted`, `order`, `father`, `pred`, `succ` and |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_bfs_simple()` now takes `igraph_vector_int_t` for its `vids`, `layers` and `parents` arguments instead of an ` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_bfs_simple()` now returns -1 in `parents` for the root node of the traversal, and -2 for unreachable vertices. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_biconnected_components()` now uses an `igraph_vector_int_t` to return the list of articulation points, not an  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_bipartite_projection()` now uses `igraph_vector_int_t` to return `multiplicity1` and `multiplicity2`, not `igr |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_bridges()` now uses an `igraph_vector_int_t` to return the list of bridges, not an `igraph_vector_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_callaway_traits_game()` returns the node types in an `igraph_vector_int_t` instead of an `igraph_vector_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_canonical_permutation()` now uses an `igraph_vector_int_t` for its labeling parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_cattribute_list()` now uses `igraph_vector_int_t` to return `gtypes`, `vtypes` and `etypes`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_cited_type_game()` now uses an `igraph_vector_int_t` for its types parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_citing_cited_type_game()` now uses an `igraph_vector_int_t` for its |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_clique_handler_t` now uses an `igraph_vector_int_t` for its `clique` parameter, and must return an `igraph_err |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `res` parameter of `igraph_cliques()` is now an `igraph_vector_int_list_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Callbacks used by `igraph_cliques_callback()` need to be updated to account for the fact that the callback does not ow |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_closeness()` and `igraph_closeness_cutoff()` now use an `igraph_vector_int_t` to return `reachable_count`, not |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_cohesive_blocks()` now uses an `igraph_vector_int_t` to return the mapping from block indices to parent block  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `igraph_community_eb_get_merges()` bridges parameter now starts the indices into the edge removal vector at 0, not |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `igraph_community_eb_get_merges()` now reports an error when not all edges in the graph are removed, instead of a  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_edge_betweenness()` now uses an `igraph_vector_int_t` to return the edge IDs in the order of their r |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_fluid_communities()` does not provide the modularity in a separate output argument any more; use `ig |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_infomap()` now uses `igraph_integer_t` for its `nb_trials` argument. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_label_propagation()` now uses an `igraph_vector_int_t` for its `initial` parameter. It also takes a  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_label_propagation()` does not provide the modularity in a separate output argument any more; use `ig |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_leiden()` has an additional parameter to indicate the number of iterations to perform (PR #2177). |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_walktrap()`, `igraph_community_edge_betweenness()`, `igraph_community_eb_get_merges()`, `igraph_comm |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_walktrap()` now uses `igraph_integer_t` for its `steps` argument. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_coreness()` now uses an `igraph_vector_int_t` to return the coreness |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_create()` now uses an `igraph_vector_int_t` for its `edges` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_create_bipartite()` now uses an `igraph_vector_int_t` for its `edges` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_compose()` now returns the edge maps in an `igraph_vector_int_t` instead of an `igraph_vector_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_count_multiple()` now returns the multiplicities in an `igraph_vector_int_t` instead of an `igraph_vector_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_decompose()` now uses an `igraph_integer_t` for its `maxcompno` and `minelements` arguments instead of a `long |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_degree()` now uses an `igraph_vector_int_t` to return the degrees. If you need the degrees in a vector contain |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_degree_sequence_game()` now takes degree sequences represented as `igraph_vector_int_t` instead of `igraph_vec |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_degseq_t`, used by `igraph_degree_sequence_game()`, uses new names for its constants. The old names are deprec |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_delete_vertices_idx()` now uses `igraph_vector_int_t` vectors to return the mapping and the inverse mapping of |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_deterministic_optimal_imitation()` now expects the list of strategies in an `igraph_vector_int_t` instead of a |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_dfs()` now takes an `igraph_vector_int_t` for its `order`, `order_out`, `father` and `dist` arguments instead  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_diameter()` and `igraph_diameter_dijkstra()` now use `igraph_vector_int_t` vectors to return the list of verte |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_dominator_tree()` now takes an `igraph_vector_int_t` for its `dom` and `leftout` arguments instead of an `igra |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_dyad_census()` now uses `igraph_real_t` instead of `igraph_integer_t` for its output arguments, and it no long |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_edges()` now takes an `igraph_vector_int_t` for its `edges` argument instead of an `igraph_vector_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_es_multipairs()` was removed; you can use the newly added `igraph_es_all_between()` instead. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_establishment_game()` now takes an `igraph_vector_int_t` for its `node_type_vec` argument instead of an `igrap |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_eulerian_path()` and `igraph_eulerian_cycle()` now use `igraph_vector_int_t` to return the list of edge and ve |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_feedback_arc_set()` now uses an `igraph_vector_int_t` to return the IDs of the edges in the feedback arc set i |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_adjacency()` no longer has the `eids` argument, which would produce an adjacency matrix where non-zero val |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_adjacency_sparse()` now returns the sparse adjacency matrix in an `igraph_sparsemat_t` structure, and it a |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_adjacency()` and `igraph_get_adjacency_sparse()` now has a `loops` argument that lets the user specify how |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_edgelist()` now uses an `igraph_vector_int_t` for its `res` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_eids()` now uses `igraph_vector_int_t` to return lists of edge IDs and to receive lists of vertex IDs. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `path` argument of `igraph_get_eids()` was removed. You can replicate the old behaviour by constructing the list o |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_eids_multi()` was removed as its design was fundamentally broken; there was no way to retrieve the IDs of  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_incidence()` now returns the vertex IDs corresponding to the rows and columns of the incidence matrix as ` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_shortest_path()`, `igraph_get_shortest_path_bellman_ford()` and `igraph_get_shortest_path_dijkstra()` now  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_shortest_paths()`, `igraph_get_shortest_paths_dijkstra()` and `igraph_get_shortest_paths_bellman_ford()` n |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The functions `igraph_get_all_shortest_paths()`, `igraph_get_all_shortest_paths_dijkstra()`, `igraph_get_shortest_path |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The vector of parents in `igraph_get_shortest_paths()`, `igraph_get_shortest_paths_bellman_ford()` and `igraph_get_sho |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `maps` parameters in `igraph_get_isomorphisms_vf2()` and `igraph_get_subisomorphisms_vf2()` are now of type `igrap |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_stochastic()` now has an additional `weights` argument for edge weights. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_stochastic_sparse()` now returns the sparse adjacency matrix in an `igraph_sparsemat_t` structure, and it  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_girth()` now uses an `igraph_vector_int_t` for its `circle` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_girth()` now uses `igraph_real_t` as the return value so we can return infinity for graphs with no cycles (ins |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `cliques` parameters of type `igraph_vector_ptr_t` in `igraph_graphlets()`, `igraph_graphlets_candidate_basis()` a |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_hrg_init()` and `igraph_hrg_resize()` now takes an `igraph_integer_t` as their size arguments instead of an `i |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_hrg_consensus()` now returns the parent vector in an `igraph_vector_int_t` instead of an `igraph_vector_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_hrg_create()` now takes a vector of probabilities corresponding to the internal nodes of the dendogram. It use |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_hrg_predict()` now uses an `igraph_vector_int_t` for its `edges` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_hrg_sample()` now always samples a single graph only. Use `igraph_hrg_sample_many()` if you need more than one |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_hrg_size()` now returns an `igraph_integer_t` instead of an `int`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_incidence()` does not accept negative incidence counts any more. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_incident()` now uses an `igraph_vector_int_t` for its `eids` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `res` parameter in `igraph_independent_vertex_sets()` is now an `igraph_vector_int_list_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_induced_subgraph_map()` now uses `igraph_vector_int_t` vectors to return the mapping and the inverse mapping o |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_intersection()` now uses an `igraph_vector_int_t` for its `edge_map1` and `edge_map2` parameters. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `edgemaps` parameter of `igraph_intersection_many()` is now an `igraph_vector_int_list_t` instead of a pointer vec |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_is_chordal()` now uses an `igraph_vector_int_t` for its `alpha`, `alpham1` and `fill_in` parameters. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_is_graphical()` and `igraph_is_bigraphical()` now take degree sequences represented as `igraph_vector_int_t` i |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_is_matching()`, `igraph_is_maximal_matching()` and `igraph_maximum_bipartite_matching` now use an `igraph_vect |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_is_mutual()` has an additional parameter which controls whether directed self-loops are considered mutual. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `vids` parameter for `igraph_isoclass_subgraph()` is now an `igraph_vector_int_t` instead of `igraph_vector_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_isomorphic_vf2()`, `igraph_get_isomorphisms_vf2_callback()` (which used to be called `igraph_isomorphic_functi |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `cliques` parameter of type `igraph_vector_ptr_t` in `igraph_largest_cliques()` was changed to an `igraph_vector_i |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `res` parameters of type `igraph_vector_ptr_t` in `igraph_largest_independent_vertex_sets()` and `igraph_largest_w |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The dimension vector parameter for `igraph_square_lattice()` (used to be `igraph_lattice()`) is now an `igraph_vector_ |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The maxiter parameter of `igraph_layout_bipartite()` is now an `igraph_integer_t` instead of `long int`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The fixed parameter of `igraph_layout_drl()` and `igraph_layout_drl_3d()` was removed as it has never been implemented |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The width parameter of `igraph_layout_grid()` is now an `igraph_integer_t` instead of `long int`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The width and height parameters of `igraph_layout_grid_3d()` are now `igraph_integer_t` instead of `long int`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The dimension parameter of `igraph_layout_mds()` is now an `igraph_integer_t` instead of `long int`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `roots` and `rootlevel` parameters of `igraph_layout_reingold_tilford()` are now `igraph_vector_int_t` instead of  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `roots` and `rootlevel` parameters of `igraph_layout_reingold_tilford_circular()` are now `igraph_vector_int_t` in |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The order parameter of `igraph_layout_star()` is now an `igraph_vector_int_t` instead of an `igraph_vector_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The maxiter parameter of `igraph_layout_sugiyama()` is now an `igraph_integer_t` instead of `long int`. Also, the func |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The shifts parameter of `igraph_lcf_vector()` is now an `igraph_vector_int_t` instead of an `igraph_vector_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_matrix_minmax()`, `igraph_matrix_which_minmax()`, `igraph_matrix_which_min()` and `igraph_matrix_which_max()`  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_maxflow()` now uses an `igraph_vector_int_t` for its `cut`, `partition` and `partition2` parameters. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `igraph_maxflow_stats_t` struct now contains `igraph_integer_t` values instead of `int` ones. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `res` parameters in `igraph_maximal_cliques()` and `igraph_maximal_cliques_subset()` are now of type `igraph_vecto |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Callbacks used by `igraph_maximal_cliques_callback()` need to be updated to account for the fact that the callback doe |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `res` parameter in `igraph_maximal_independent_vertex_sets()` is now an `igraph_vector_int_list_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_maximum_cardinality_search()` now uses an `igraph_vector_int_t` for its `alpha` and `alpham1` arguments. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_mincut()` now uses an `igraph_vector_int_t` for its `cut`, `partition` and `partition2` parameters. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_moran_process()` now expects the list of strategies in an `igraph_vector_int_t` instead of an `igraph_int_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Motif callbacks of type `igraph_motifs_handler_t` now take an `igraph_vector_int_t` with the vertex IDs instead of an  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Motif functions now use `igraph_integer_t` instead of `int` for their `size` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_neighborhood_size()` now uses an `igraph_vector_int_t` for its `res` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `res` parameter of `igraph_neighborhood()` is now an `igraph_vector_int_list_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_neighbors()` now uses an `igraph_vector_int_t` for its `neis` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_permute_vertices()` now takes an `igraph_vector_int_t` as the permutation vector. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_power_law_fit()` does not calculate the p-value automatically any more because the previous estimation method  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_preference_game()` now uses an `igraph_vector_int_t` to return the types of the nodes in the generated graph. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_random_walk()` now uses an `igraph_vector_int_t` for its results. Also, the function now takes both vertices a |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_random_edge_walk()` now uses an `igraph_vector_int_t` for its `edgewalk` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_read_graph_dimacs_flow()` now uses an `igraph_vector_int_t` for its label parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_read_graph_graphml()` now uses `igraph_integer_t` for its `index` argument. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_read_graph_pajek()` now creates a Boolean `type` attribute for bipartite graphs. Previously it created a numer |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_realize_degree_sequence()` now uses an `igraph_vector_int_t` for its `outdeg` and `indeg` parameters. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_reindex_membership()` now uses an `igraph_vector_int_t` for its `new_to_old` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_rng_seed()` now requires an `igraph_uint_t` as its seed arguments. RNG implementations are free to use only th |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_rngtype_rand` (i.e. the RNG that is based on BSD `rand()`) was removed due to poor statistical properties that |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_roulette_wheel_imitation()` now expects the list of strategies in an `igraph_vector_int_t` instead of an `igra |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_similarity_dice_pairs()` now uses an `igraph_vector_int_t` for its `pairs` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_similarity_jaccard_pairs()` now uses an `igraph_vector_int_t` for its `pairs` parameter. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_simple_interconnected_islands_game()` does not generate multi-edges between islands any more. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_sort_vertex_ids_by_degree()` and `igraph_topological_sorting()` now use an `igraph_vector_int_t` to return the |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_spanning_tree()`, `igraph_minimum_spanning_tree()` and `igraph_random_spanning_tree()` now all use an `igraph_ |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_sparsemat_cholsol()`, `igraph_sparsemat_lusol()`, `igraph_sparsemat_symbqr()` and `igraph_sparsemat_symblu()`  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_sparsemat_count_nonzero()` and `igraph_sparsemat_count_nonzerotol()` now return an `igraph_integer_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_sparsemat_is_symmetric()` now returns an error code and the result itself is provided in an output argument. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `values` argument of `igraph_sparsemat_transpose()` was removed; now the function always copies the values over to |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_spmatrix_t` and related functions were removed as they mostly duplicated functionality that was already presen |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_stochastic_imitation()` now expects the list of strategies in an `igraph_vector_int_t` instead of an `igraph_i |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_st_mincut()` now uses an `igraph_vector_int_t` for its `cut`, `partition` and `partition2` parameters. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_st_vertex_connectivity()` now ignores edges between source and target for `IGRAPH_VCONN_NEI_IGNORE` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_strvector_get()` now returns strings in the return value, not in an output argument. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_subcomponent()` now uses an `igraph_integer_t` for the seed vertex instead of an `igraph_real_t`. It also uses |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_subisomorphic_vf2()`, `igraph_get_subisomorphisms_vf2_callback()` (which used to be called `igraph_subisomorph |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `maps` parameters in `igraph_subisomorphic_lad()`, `igraph_get_isomorphisms_vf2()` and `igraph_get_subisomorphisms |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_subisomorphic_lad()` now uses an `igraph_vector_int_t` for its `map` parameter. Also, its `domains` parameter  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_unfold_tree()` now uses an `igraph_vector_int_t` for its `vertex_index` and `roots` parameters. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_union()` now uses an `igraph_vector_int_t` for its `edge_map1` and `edge_map2` parameters. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `edgemaps` parameter of `igraph_union_many()` is now an `igraph_vector_int_list_t` instead of a pointer vector. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_init_copy()` was refactored to take _another_ vector that the newly initialized vector should copy. The |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_ptr_init_copy()` was renamed to `igraph_vector_ptr_init_array()` for sake of consistency. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_vs_vector()`, `igraph_vss_vector()` and `igraph_vs_vector_copy()` now all take an `igraph_vector_int_t` as the |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `res` parameter of `igraph_weighted_cliques()` is now an `igraph_vector_int_list_t`. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_write_graph_dimacs_flow()` now uses `igraph_integer_t` for the source and target vertex index instead of a `lo |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_*()`, `igraph_matrix_*()`, `igraph_stack_*()`, `igraph_array_*()` and several other generic igraph data |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_minmax()` and `igraph_vector_which_minmax()` no longer return an error code. The return type is now `vo |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_order()` was removed; use `igraph_vector_int_pair_order()` instead. (The original function worked for v |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_resize_min()` and `igraph_matrix_resize_min()` no longer return an error code (return type is now `void |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_qsort_ind()` and its variants now take an `igraph_order_t` enum instead of a boolean to denote whether  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_weighted_adjacency()` now returns the weights in a separate vector instead of storing it in a vertex attribute |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `loops` argument of `igraph_weighted_adjacency()` was converted to an `igraph_loops_t` for sake of consistency wit |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_write_graph_gml()` takes an additional bitfield parameter controlling some aspects of writing the GML file. |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - The `add_edges()` function in the attribute handler now takes an `igraph_vector_int_t` for its `edges` parameter inste |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - igraph functions that interface with external libraries such as BLAS or LAPACK may now fail if the underlying BLAS or  |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - Functions that used an `igraph_vector_t` to represent cluster size and cluster membership now use an `igraph_vector_in |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_connected_components()` (used to be `igraph_clusters()` in 0.9 and before) |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_eb_get_merges()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_edge_betweenness()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_fastgreedy()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_fluid_communities()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_infomap()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_label_propagation()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_leading_eigenvector()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_leiden()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_multilevel()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_optimal_modularity()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_spinglass()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_spinglass_single()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_to_membership()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_walktrap()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_compare_communities()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_le_community_to_membership()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_modularity()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_reindex_membership()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_split_join_distance()` |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_community_multilevel()` additionally uses a `igraph_matrix_int_t` instead of `igraph_matrix_t()` for its membe |
| [0.10.0] - 2022-09-05 / Breaking changes | Modified functionality / [0.10.0] - 2022-09-05 | - `IGRAPH_TOTAL` was removed from the `igraph_neimode_t` enum; use the equivalent `IGRAPH_ALL` instead. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - A new integer type, `igraph_uint_t` has been added. This is the unsigned pair of `igraph_integer_t` and they are alway |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - A new container type, `igraph_vector_list_t` has been added, replacing most uses of `igraph_vector_ptr_t` in the API w |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - A new container type, `igraph_matrix_list_t` has been added, replacing most uses of `igraph_vector_ptr_t` in the API w |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - A new container type, `igraph_graph_list_t` has been added, replacing most uses of `igraph_vector_ptr_t` in the API wh |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - The vector container type, `igraph_vector_t`, has been extended with a new variant whose functions all start with `igr |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_adjlist_init_from_inclist()` to create an adjacency list from an already existing incidence list by resolving  |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_almost_equals()` and `igraph_cmp_epsilon()` to compare floating point numbers with a relative tolerance. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_betweenness_subset()` and `igraph_edge_betweenness_subset()` calculates betweenness and edge betweenness score |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_blas_dgemm()` to multiply two matrices. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_calloc()` and `igraph_realloc()` are now publicly exposed; these functions provide variants of `calloc()` and  |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_circulant()` to create circulant graphs (#1856, thanks to @Gomango999). |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_complex_almost_equals()` to compare complex numbers with a relative tolerance. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_eccentricity_dijkstra()` finds the longest weighted path length among all shortest paths between a set of vert |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_enter_safelocale()` and `igraph_exit_safelocale()` for temporarily setting the locale to C. Foreign format rea |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_es_all_between()` to create an edge selector that selects all edges between a pair of vertices. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_full_multipartite()` generates full multipartite graphs (a generalization of bipartite graphs to multiple grou |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_fundamental_cycles()` computes a fundamental cycle basis (experimental). |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_generalized_petersen()` to create generalized Petersen graphs (#1844, thanks to @alexsyou). |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_get_all_eids_between()` returns the IDs of all edges between a pair of vertices. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_get_k_shortest_paths()` finds the k shortest paths between a source and a target vertex. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_get_laplacian()` and `igraph_get_laplacian_sparse()` return the Laplacian matrix of the graph as a dense or sp |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_get_widest_path()`, `igraph_get_widest_paths()`, `igraph_widest_path_widths_dijkstra()` and `igraph_widest_pat |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_graph_center()` finds the central vertices of the graph. The central vertices are the ones having a minimum ec |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_graph_count()` returns the number of unlabelled graphs on a given number of vertices. It is meant to find the  |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_has_mutual()` checks if a directed graph has any mutual edges. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_heap_clear()` and `igraph_heap_min_clear()` remove all elements from an `igraph_heap_t` or an `igraph_heap_min |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_invalidate_cache()` invalidates all cached graph properties, forcing their recomputation next time they are re |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_is_forest()` to check whether a graph is a forest (#1888, thanks to @rohitt28). |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_is_acyclic()` to check whether a graph is acyclic (#1945, thanks to @borsgeorgica). |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_is_perfect()` to check whether a graph is a perfect graph (#1730, thanks to @guyroznb). |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_hub_and_authority_scores()` calculates the hub and authority scores of a graph as a matching pair. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_layout_umap()` and `igraph_layout_umap_3d()` to lay out a graph in 2D or 3D space using the UMAP dimensionalit |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_local_scan_subset_ecount()` counts the number of edges in induced sugraphs from a subset of vertices. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_matrix_view_from_vector()` allows interpreting the data stored in a vector as a matrix of the specified size. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_minimum_cycle_basis()` computes an unweighted minimum cycle basis (experimental). |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_pseudo_diameter()` and `igraph_pseudo_diameter_dijkstra()` to determine a lower bound for the diameter of a gr |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_regular_tree()` creates a regular tree where all internal vertices have the same total degree. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_rngtype_pcg32` and `igraph_rngtype_pcg64` implement 32-bit and 64-bit variants of the PCG random number genera |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_rng_get_pois()` generates random variates from the Poisson distribution. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_roots_for_tree_layout()` computes a set of roots suitable for a nice tree layout. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_spanner()` calculates a spanner of a graph with a given stretch factor (#1752, thanks to @guyroznb) |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_sparse_adjacency()` and `igraph_sparse_weighted_adjacency()` constructs graphs from (weighted) sparse matrices |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_sparsemat_get()` to retrieve a single element of a sparse matrix. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_sparsemat_normalize_rows()` and `igraph_sparsemat_normalize_cols()` to normalize sparse matrices row-wise or c |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_stack_capacity()` to query the capacity of a stack. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_strvector_capacity()` returns the maximum number of strings that can be stored in a string vector without real |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_strvector_merge()` moves all strings from one string vectors to the end of another without re-allocating them. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_strvector_push_back_len()` adds a new string to the end of a string vector and allows the user to specify the  |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_strvector_reserve()` reserves space for a given number of string pointers in a string vector. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_symmetric_tree()` to create a tree with the specified number of branches at each level (#1859, thanks to @Yuli |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_trussness()` calculates the trussness of each edge in the graph (#1034, thanks to @alexperrone) |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_turan()` generates Turán graphs (#2088, thanks to @pradkrish) |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_all_almost_e()`, `igraph_vector_complex_all_almost_e()`, `igraph_matrix_all_almost_e()`, `igraph_matrix |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_complex_zapsmall()` and `igraph_matrix_complex_zapsmall()` for replacing small components of complex ve |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_lex_cmp_untyped()` and `igraph_vector_colex_cmp_untyped()` for lexicographic and colexicographic compar |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_permute()` functions to permute a vector based on an index vector. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_ptr_sort_ind()` to obtain an index vector that would sort a vector of pointers based on some comparison |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_range()` to fill an existing vector with a range of increasing numbers. |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_remove_fast()` functions to remove an item from a vector by swapping it with the last element and then  |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_vertex_path_from_edge_path()` converts a sequence of edge IDs representing a path to an equivalent sequence of |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_vs_range()`, `igraph_vss_range()`, `igraph_es_range()` and `igraph_ess_range()` creates vertex and edge sequen |
| [0.10.0] - 2022-09-05 / Added | Added functionality / [0.10.0] - 2022-09-05 | - `igraph_wheel()` to create a wheel graph (#1938, thanks to @kwofach). |
| [0.10.0] - 2022-09-05 / Removed | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_adjlist_remove_duplicate()`, `igraph_betweenness_estimate()`, `igraph_closeness_estimate()`, `igraph_edge_betw |
| [0.10.0] - 2022-09-05 / Removed | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_dnorm()`, `igraph_strvector_move_interval()`, `igraph_strvector_permdelete()` and `igraph_strvector_remove_neg |
| [0.10.0] - 2022-09-05 / Removed | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_eigen_laplacian()`, `igraph_es_fromto()` and `igraph_maximum_matching()` were removed. These are not breaking  |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_degree_sequence_game()` now supports an additional method, `IGRAPH_DEGSEQ_EDGE_SWITCHING_SIMPLE`, an edge-swit |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_get_adjacency()` and `igraph_get_adjacency_sparse()` now count loop edges _twice_ in undirected graphs when us |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_matrix_print()` and `igraph_matrix_fprint()` functions now align columns when priting. |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_read_graph_gml()` now supports graph attributes (in addition to vertex and edge attributes). |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_read_graph_gml()` now uses NaN as the default numerical attribute values instead of 0. |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - The Pajek parser in `igraph_read_graph_pajek()` is now less strict and accepts more files. |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_ring()` no longer simplifies its result when generating a one- or two-vertex graph. The one-cycle has a self-l |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_view()` now allows `data` to be `NULL` in the special case when `length == 0`. |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_version()` no longer returns an error code. |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_write_graph_gml()` uses the `creator` parameter in a different way: the supplied string is now written into th |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_write_graph_gml()` skips writing NaN values. These two changes ensure consistent round-tripping. |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_write_graph_gml()` and `igraph_read_graph_gml()` now have limited support for entity encoding. |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - `igraph_write_graph_ncol()` now preserves the edge ordering of the graph when writing an NCOL file. |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - igraph functions that take an ARPACK options object now also accept `NULL` in place of an options object, and they wil |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - Foreign format readers now present more informative error messages. |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - The default tolerance of the zapsmall functions is now `eps^(2/3)` instead of `eps^(1/2)` where eps is the machine eps |
| [0.10.0] - 2022-09-05 / Changed | Modified functionality / [0.10.0] - 2022-09-05 | - It is now possible to override the uniform integer and the Poisson samplers in the random number generator interface. |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - When an error occurs during parsing DL, GML, NCOL, LGL or Pajek files, line numbers are now reported correctly. |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - The GraphML parser does not print to stderr any more in case of encoding errors and other error conditions originating |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - The GraphML parser would omit some edges and vertices when reading files with custom attribute types, such as those pr |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - The GML parser no longer mixes up Inf and NaN and -Inf now works. |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - The GML parser now supports nodes with no id field. |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - The GML parser now performs more stringent checks on the input file, such as verifying that `id`, `source`, `target` a |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - The core data structures (vector, etc.) have overflow checks now. |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - Deterministic graph generators, as well as most random ones, have overflow checks now. |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - Graphs no longer lose all their attributes after calling `igraph_contract_vertices()`. |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - `igraph_hrg_init()` does not throw an assertion error anymore for zero vertices. |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - `igraph_matrix_complex_create()` and `igraph_matrix_complex_create_polar()` now set their sizes correctly. |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - `igraph_random_walk()` took one fewer steps than specified. |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - `igraph_sparsemat_getelements_sorted()` did not sort the elements for triplet matrices correctly; this is fixed now. |
| [0.10.0] - 2022-09-05 / Fixed | Non-functional changes / [0.10.0] - 2022-09-05 | - `igraph_write_graph_gml()` no longer produces corrupt output when some string attribute values contain `"` characters. |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_clusters()` has been renamed to `igraph_connected_components()`; the old name is deprecated and will be remove |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_complex_eq_tol()` is now deprecated in favour of `igraph_complex_almost_equals()`. |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_get_sparsemat()` is deprecated in favour of `igraph_get_adjacency_sparse()`, and will be removed in 0.11. Note |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_get_stochastic_sparsemat()` is deprecated in favour of `igraph_get_stochastic_sparse()`, and will be removed i |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_isomorphic_34()` has been deprecated in favour of `igraph_isomorphic()`. Note that `igraph_isomorphic()` calls |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_laplacian()` is now deprecated; use `igraph_get_laplacian()` or `igraph_get_laplacian_sparse()` depending on w |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_lattice()` has been renamed to `igraph_square_lattice()` to indicate that this function generates square latti |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_local_scan_neighborhood_ecount()` is now deprecated in favour of `igraph_local_scan_subset_ecount()`. |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_matrix_all_e_tol()` is now deprecated in favour of `igraph_matrix_all_almost_e()`. |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_matrix_copy()` is now deprecated; use `igraph_matrix_init_copy()` instead. The new name emphasizes that the fu |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_matrix_e()` and `igraph_matrix_e_ptr()` have been renamed to `igraph_matrix_get()` and `igraph_matrix_get_ptr( |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_random_edge_walk()` has been deprecated by `igraph_random_walk()` to support edges and/or vertices for the ran |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_sparsemat_copy()`, `igraph_sparsemat_diag()` and `igraph_sparsemat_eye()` have been renamed to `igraph_sparsem |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_strvector_add()` has been renamed to `igraph_strvector_push_back()` for sake of consistency with other vector- |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_strvector_copy()` has been renamed to `igraph_strvector_init_copy()` for sake of consistency with other vector |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_strvector_get()` now returns a `const char*` and not a `char*` to indicate that you are not supposed to modify |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_strvector_set2()` has been renamed to `igraph_strvector_set_len()`; the old name is deprecated and will be rem |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_tree()` has been renamed to `igraph_kary_tree()`; the old name is deprecated and will be removed in 0.11. |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_e()` and `igraph_vector_e_ptr()` have been renamed to `igraph_vector_get()` and `igraph_vector_get_ptr( |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_e_tol()` is now deprecated in favour of `igraph_vector_all_almost_e()`. |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_copy()` is now deprecated; use `igraph_vector_init_copy()` instead. The new name emphasizes that the fu |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_vector_init_seq()` is now deprecated in favour of `igraph_vector_init_range()`, which uses C-style intervals ( |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_vs_seq()`, `igraph_vss_seq()`, `igraph_es_seq()` and `igraph_ess_seq()` are now deprecated in favour of `igrap |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_write_graph_dimacs()` has been renamed to `igraph_write_graph_dimacs_flow()`; the old name is deprecated and m |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - `igraph_zeroin()` is deprecated and will be removed in 0.11, with no replacement. The function is not graph-related an |
| [0.10.0] - 2022-09-05 / Deprecated | Deprecated and removed functionality / [0.10.0] - 2022-09-05 | - The macros `igraph_Calloc`, `igraph_Realloc` and `igraph_Free` have been deprecated in favour of `IGRAPH_CALLOC`, `IGR |
| [0.10.0] - 2022-09-05 / Other | Non-functional changes / [0.10.0] - 2022-09-05 | - Documentation improvements. |
| [0.10.0] - 2022-09-05 / Other | Non-functional changes / [0.10.0] - 2022-09-05 | - Support for Intel's LLVM-based compiler. |
| [0.9.10] - 2022-09-02 / Added | Added functionality / [0.9.10] - 2022-09-02 | - `igraph_reverse_edges()` reverses the specified edges in the graph while preserving all attributes. |
| [0.9.10] - 2022-09-02 / Changed | Modified functionality / [0.9.10] - 2022-09-02 | - The `IGRAPH_ARPACK_PROD` error code is no longer used. Instead, the specific error encountered while doing matrix mult |
| [0.9.10] - 2022-09-02 / Changed | Modified functionality / [0.9.10] - 2022-09-02 | - XML external entities are not resolved any more when parsing GraphML files to prevent XML external entity injection (X |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - Fixed incorrect results from `igraph_local_scan_1_ecount()` when the graph was directed but the mode was `IGRAPH_ALL`  |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - Fixed incorrect counting of self-loops in `igraph_local_scan_neighborhood_ecount()` when the graph was undirected. |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - In some rare edge cases, `igraph_pagerank()` with the ARPACK method and `igraph_hub_score()` / `igraph_authority_score |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - `igraph_permute_vertices()` now checks for out-of-range indices and duplicates in the permutation vector. |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - `igraph_create()` now checks for non-finite vertex indices in the edges vector. |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - `igraph_eigenvector_centrality()` would return incorrect scores when some weights were negative. |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - `igraph_es_seq()` and `igraph_ess_seq()` did not include the `to` vertex in the sequence. |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - `igraph_eit_create()` and `igraph_vit_create()` now check that all edge/vertex indices are in range when creating iter |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - `igraph_grg_game()` now validates its arguments. |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - `igraph_layout_drl()` and its 3D version now validate their inputs. |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - `igraph_layout_kamada_kawai()`, `igraph_layout_fruchterman_reingold()`, `igraph_layout_drl()`, as well as their 3D ver |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - `igraph_asymmetric_preference_game()` interpreted its `type_dist_matrix` argument incorrectly. |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - Fixed incorrect result of `igraph_community_spinglass()` for null and singleton graphs. |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - `igraph_layout_gem()` does not crash any more for graphs with only a single vertex. |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - `igraph_bridges()` no longer uses recursion and thus is no longer prone to stack overflow. |
| [0.9.10] - 2022-09-02 / Fixed | Non-functional changes / [0.9.10] - 2022-09-02 | - Include paths of dependent packages would be specified incorrectly in some environments. |
| [0.9.10] - 2022-09-02 / Other | Non-functional changes / [0.9.10] - 2022-09-02 | - Documentation improvements. |
| [0.9.9] - 2022-06-04 / Changed | Modified functionality / [0.9.9] - 2022-06-04 | - `igraph_community_walktrap()` now uses double precision floating point operations internally instead of single precisi |
| [0.9.9] - 2022-06-04 / Changed | Modified functionality / [0.9.9] - 2022-06-04 | - In `igraph_community_leiden()`, the `nb_clusters` output parameter is now optional (i.e. it can be `NULL`). |
| [0.9.9] - 2022-06-04 / Changed | Modified functionality / [0.9.9] - 2022-06-04 | - `igraph_read_graph_graphml()` no longer attempts to temporarily set the C locale, and will therefore not work correctl |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_community_walktrap()` would return an invalid `modularity` vector when the `merges` matrix was not requested. |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_community_walktrap()` would return a `modularity` vector that was too long for disconnected graphs. This would |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_community_walktrap()` now checks the weight vector: only non-negative weights are accepted, and all vertices m |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_community_walktrap()` now returns a modularity score of NaN for graphs with no edges. |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_community_fast_greedy()` now returns a modularity score of NaN for graphs with no edges. |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_community_edge_betweenness()` now returns a modularity vector with a single NaN entry for graph with no edges. |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_community_leading_eigenvector()` does not ignore non-ARPACK-related errors from `igraph_arpack_rssolve()` any  |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_preference_game()` now works correctly when `fixed_size` is true and |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - Fixed a memory leak in `igraph_hrg_fit()` when using `start=1`. |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_write_graph_dot()` now outputs NaN values unchanged. |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_write_graph_dot()` no longer produces invalid DOT files when empty string attributes are present. |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_layout_fruchterman_reingold()` and `igraph_layout_kamada_kawai()`, as well as their 3D versions, did not respe |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - The initial coordinates of the Kamada-Kawai layout (`igraph_layout_kamada_kawai()` and `igraph_layout_kamada_kawai_3d( |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - Improved numerical stability in Kamada-Kawai layout. |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - Corrected a problem in the calculation of displacements in `igraph_layout_fruchterman_reingold()` and its 3D version.  |
| [0.9.9] - 2022-06-04 / Fixed | Non-functional changes / [0.9.9] - 2022-06-04 | - `igraph_sumtree_search()` would consider search intervals open on the left and closed on the right, contrary to the do |
| [0.9.9] - 2022-06-04 / Other | Non-functional changes / [0.9.9] - 2022-06-04 | - Greatly improved error reporting from foregin format parsers. |
| [0.9.9] - 2022-06-04 / Other | Non-functional changes / [0.9.9] - 2022-06-04 | - Documentation improvements. |
| [0.9.8] - 2022-04-08 / Fixed | Non-functional changes / [0.9.8] - 2022-04-08 | - Assertion failure in `igraph_bfs()` when an empty `roots` or `restricted` vector was provided. |
| [0.9.8] - 2022-04-08 / Fixed | Non-functional changes / [0.9.8] - 2022-04-08 | - `igraph_diversity()` now returns 0 for degree-1 vertices. Previously it incorrectly returned NaN or +-Inf depending on |
| [0.9.8] - 2022-04-08 / Fixed | Non-functional changes / [0.9.8] - 2022-04-08 | - `igraph_community_walktrap()` does not crash any more when provided with |
| [0.9.8] - 2022-04-08 / Other | Non-functional changes / [0.9.8] - 2022-04-08 | - Documentation improvements. |
| [0.9.7] - 2022-03-16 / Changed | Modified functionality / [0.9.7] - 2022-03-16 | - `igraph_get_all_shortest_paths_dijsktra()` now uses tolerances when comparing path |
| [0.9.7] - 2022-03-16 / Changed | Modified functionality / [0.9.7] - 2022-03-16 | - `igraph_vector_*_swap` and `igraph_matrix_swap` now take O(1) instead of O(n) and accept all sizes. |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - NCOL and LGL format writers no longer accept "name" and "weight" attributes |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - The LGL writer could not access numerical weight attributes, potentially leading |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - External PLFIT libraries and their headers are now detected at their standard |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - `igraph_vector_init()` no longer accepts negative vector sizes. |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - `igraph_assortativity_nominal()` crashed on the null graph. |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - Label propagation now ensures that all labels are dominant. |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - Fixed incorrect partition results for walktrap algorithm (issue #1927) |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - Negative values returned by `igraph_rng_get_integer()` and `RNG_INTEGER()` were incorrect, |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - `igraph_community_walktrap()` now checks its `steps` input argument. |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - The first modularity value reported by `igraph_community_walktrap()` was |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - `igraph_correlated_game()` would return incorrect results, or exhaust the memory, |
| [0.9.7] - 2022-03-16 / Fixed | Non-functional changes / [0.9.7] - 2022-03-16 | - `igraph_community_label_propagation` incorrectly did not result in all labels being dominant (issue #1963, fixed in PR |
| [0.9.7] - 2022-03-16 / Other | Non-functional changes / [0.9.7] - 2022-03-16 | - The C attribute handler now verifies attribute types when retrieving attributes. |
| [0.9.7] - 2022-03-16 / Other | Non-functional changes / [0.9.7] - 2022-03-16 | - Documentation improvements. |
| [0.9.6] - 2022-01-05 / (no subsection) | Modified functionality / [0.9.6] - 2022-01-05 | - Isomorphism class functions (`igraph_isoclass()`, `igraph_isoclass_subgraph()`, |
| [0.9.6] - 2022-01-05 / Fixed | Non-functional changes / [0.9.6] - 2022-01-05 | - igraph would not build with MinGW when using the vendored GLPK and enabling TLS. |
| [0.9.6] - 2022-01-05 / Fixed | Non-functional changes / [0.9.6] - 2022-01-05 | - Removed some uses of `abort()` from vendored libraries, which could unexpectedly |
| [0.9.6] - 2022-01-05 / Fixed | Non-functional changes / [0.9.6] - 2022-01-05 | - `igraph_community_label_propagation()` no longer leaves any vertices unlabeled |
| [0.9.6] - 2022-01-05 / Fixed | Non-functional changes / [0.9.6] - 2022-01-05 | - The Kamada-Kawai layout is now interruptible. |
| [0.9.6] - 2022-01-05 / Fixed | Non-functional changes / [0.9.6] - 2022-01-05 | - The Fruchterman-Reingold layout is now interruptible. |
| [0.9.6] - 2022-01-05 / Fixed | Non-functional changes / [0.9.6] - 2022-01-05 | - Fixed a bug in `igraph_cmp_epsilon()` that resulted in incorrect results for |
| [0.9.6] - 2022-01-05 / Fixed | Non-functional changes / [0.9.6] - 2022-01-05 | - Weighted clique related functions now fall back to the unweighted variants |
| [0.9.6] - 2022-01-05 / Fixed | Non-functional changes / [0.9.6] - 2022-01-05 | - `igraph_erdos_renyi_game_(gnm\|gnp)` would not produce self-loops for the singleton |
| [0.9.6] - 2022-01-05 / Fixed | Non-functional changes / [0.9.6] - 2022-01-05 | - Fixed a bug in `igraph_local_efficiency()` that sometimes erroneously |
| [0.9.6] - 2022-01-05 / Fixed | Non-functional changes / [0.9.6] - 2022-01-05 | - `igraph_vector_update()` (and its type-specific variants) did not check for |
| [0.9.6] - 2022-01-05 / Fixed | Non-functional changes / [0.9.6] - 2022-01-05 | - Fixed a potential crash in the GraphML reader that would be triggered by some |
| [0.9.6] - 2022-01-05 / Other | Non-functional changes / [0.9.6] - 2022-01-05 | - `igraph_is_tree()` has improved performance and memory usage. |
| [0.9.6] - 2022-01-05 / Other | Non-functional changes / [0.9.6] - 2022-01-05 | - `igraph_is_connected()` has improved performance when checking weak connectedness. |
| [0.9.6] - 2022-01-05 / Other | Non-functional changes / [0.9.6] - 2022-01-05 | - Improved error handling in `igraph_maximal_cliques()` and related functions. |
| [0.9.6] - 2022-01-05 / Other | Non-functional changes / [0.9.6] - 2022-01-05 | - The build system now checks that GLPK is of a compatible version (4.57 or later). |
| [0.9.6] - 2022-01-05 / Other | Non-functional changes / [0.9.6] - 2022-01-05 | - The vendored `plfit` package was updated to 0.9.3. |
| [0.9.6] - 2022-01-05 / Other | Non-functional changes / [0.9.6] - 2022-01-05 | - You can now build igraph with an external `plfit` instead of the vendored one. |
| [0.9.6] - 2022-01-05 / Other | Non-functional changes / [0.9.6] - 2022-01-05 | - Documentation improvements. |
| [0.9.5] - 2021-11-11 / Fixed | Non-functional changes / [0.9.5] - 2021-11-11 | - `igraph_reindex_membership()` does not allow negative membership indices any more. |
| [0.9.5] - 2021-11-11 / Fixed | Non-functional changes / [0.9.5] - 2021-11-11 | - `igraph_rewire_directed_edges()` now generates multigraphs when edge directions |
| [0.9.5] - 2021-11-11 / Fixed | Non-functional changes / [0.9.5] - 2021-11-11 | - Fixed a bug in `igraph_gomory_hu_tree()` that returned only the equivalent flow |
| [0.9.5] - 2021-11-11 / Fixed | Non-functional changes / [0.9.5] - 2021-11-11 | - Fixed a bug in the `IGRAPH_TO_UNDIRECTED_COLLAPSE` mode of |
| [0.9.5] - 2021-11-11 / Fixed | Non-functional changes / [0.9.5] - 2021-11-11 | - Fixed the behaviour of the `IGRAPH_ENABLE_LTO` option when it was set to |
| [0.9.5] - 2021-11-11 / Fixed | Non-functional changes / [0.9.5] - 2021-11-11 | - When using igraph from a CMake project, it is now checked that the project has |
| [0.9.5] - 2021-11-11 / Other | Non-functional changes / [0.9.5] - 2021-11-11 | - Improved the root selection method for disconnected graphs in the |
| [0.9.5] - 2021-11-11 / Other | Non-functional changes / [0.9.5] - 2021-11-11 | - `igraph_decompose()` is now much faster for large graphs containing many |
| [0.9.5] - 2021-11-11 / Other | Non-functional changes / [0.9.5] - 2021-11-11 | - `igraph_largest_cliques()` and `igraph_clique_number()` were re-written to |
| [0.9.5] - 2021-11-11 / Other | Non-functional changes / [0.9.5] - 2021-11-11 | - The vendored GLPK has been upgraded to GLPK 5.0. |
| [0.9.5] - 2021-11-11 / Other | Non-functional changes / [0.9.5] - 2021-11-11 | - Documentation improvements. |
| [0.9.4] - 2021-05-31 / Changed | Modified functionality / [0.9.4] - 2021-05-31 | - Unweighted transitivity (i.e. clustering coefficient) calculations now ignore multi-edges and edge directions instead  |
| [0.9.4] - 2021-05-31 / Changed | Modified functionality / [0.9.4] - 2021-05-31 | - `igraph_transitivity_barrat()` now returns an error code if the input graph has multiple edges (which is not handled c |
| [0.9.4] - 2021-05-31 / Fixed | Non-functional changes / [0.9.4] - 2021-05-31 | - `igraph_local_scan_k_ecount()` now handles loops correctly. |
| [0.9.4] - 2021-05-31 / Fixed | Non-functional changes / [0.9.4] - 2021-05-31 | - `igraph_transitivity_avglocal_undirected()` is no longer slower than `igraph_transitivity_local_undirected()`. |
| [0.9.4] - 2021-05-31 / Fixed | Non-functional changes / [0.9.4] - 2021-05-31 | - Worked around an invalid warning issued by Clang 9.0 when compiling with OpenMP. |
| [0.9.4] - 2021-05-31 / Other | Non-functional changes / [0.9.4] - 2021-05-31 | - Documentation improvements. |
| [0.9.3] - 2021-05-05 / Added | Added functionality / [0.9.3] - 2021-05-05 | - OpenMP is now enabled and used by certain functions (notably PageRank calculation) when the compiler supports it. Set  |
| [0.9.3] - 2021-05-05 / Fixed | Non-functional changes / [0.9.3] - 2021-05-05 | - `igraph_get_incidence()` no longer reads and writes out of bounds when given a non-bipartite graph, but gives a warnin |
| [0.9.3] - 2021-05-05 / Fixed | Non-functional changes / [0.9.3] - 2021-05-05 | - `igraph_dyad_census()` no longer reports an overflow on singleton graphs, and handles loops and multigraphs correctly. |
| [0.9.3] - 2021-05-05 / Fixed | Non-functional changes / [0.9.3] - 2021-05-05 | - `igraph_vector_lex_cmp()` and `igraph_vector_colex_cmp()` dereferenced their arguments only once instead of twice, and |
| [0.9.3] - 2021-05-05 / Fixed | Non-functional changes / [0.9.3] - 2021-05-05 | - `igraph_maximal_cliques_subset()` and `igraph_transitivity_barrat()` corrupted the error handling stack ("finally stac |
| [0.9.3] - 2021-05-05 / Fixed | Non-functional changes / [0.9.3] - 2021-05-05 | - CMake package files did not respect `CMAKE_INSTALL_LIBDIR`. This only affected Linux distributions which install into  |
| [0.9.3] - 2021-05-05 / Fixed | Non-functional changes / [0.9.3] - 2021-05-05 | - The parser sources could not be generated when igraph was in a location that contained spaces in its path. |
| [0.9.3] - 2021-05-05 / Fixed | Non-functional changes / [0.9.3] - 2021-05-05 | - igraph no longer links to the math library (`libm`) when this is not necessary. |
| [0.9.3] - 2021-05-05 / Fixed | Non-functional changes / [0.9.3] - 2021-05-05 | - `_CRT_SECURE_NO_WARNINGS` is now defined during compilation to enable compatibility with UWP. |
| [0.9.3] - 2021-05-05 / Fixed | Non-functional changes / [0.9.3] - 2021-05-05 | - Fixed a compilation issue on MSYS / MinGW when link-time optimization was enabled and the `MSYS Makefiles` CMake gener |
| [0.9.3] - 2021-05-05 / Deprecated | Deprecated and removed functionality / [0.9.3] - 2021-05-05 | - `igraph_rng_min()` is now deprecated; assume a constant zero as its return value if you used this function in your own |
| [0.9.3] - 2021-05-05 / Other | Non-functional changes / [0.9.3] - 2021-05-05 | - Updated the vendored CXSparse library to version 3.2.0 |
| [0.9.2] - 2021-04-14 / Added | Added functionality / [0.9.2] - 2021-04-14 | - CMake package files are now installed with igraph. This allows `find_package(igraph)` to find igraph and detect the ap |
| [0.9.2] - 2021-04-14 / Fixed | Non-functional changes / [0.9.2] - 2021-04-14 | - igraph can now be used as a CMake subproject in other CMake-based projects. |
| [0.9.2] - 2021-04-14 / Fixed | Non-functional changes / [0.9.2] - 2021-04-14 | - The documentaton can now be built from the release tarball. |
| [0.9.2] - 2021-04-14 / Fixed | Non-functional changes / [0.9.2] - 2021-04-14 | - Configuration will no longer fail when the release tarball is extracted into a subdirectory of an unrelated git reposi |
| [0.9.2] - 2021-04-14 / Fixed | Non-functional changes / [0.9.2] - 2021-04-14 | - The generated pkg-config file was incorrect when `CMAKE_INSTALL_<dir>` variables were absolute paths. |
| [0.9.2] - 2021-04-14 / Fixed | Non-functional changes / [0.9.2] - 2021-04-14 | - On Unix-like systems, the library name is now `libigraph.so.0.0.0`, as it used to be for igraph 0.8 and earlier. |
| [0.9.2] - 2021-04-14 / Fixed | Non-functional changes / [0.9.2] - 2021-04-14 | - Fixed a return type mismatch in parser sources, and fixed some warnings with recent versions of gcc. |
| [0.9.2] - 2021-04-14 / Fixed | Non-functional changes / [0.9.2] - 2021-04-14 | - Fixed a bug in `igraph_get_shortest_paths_dijkstra()` and `igraph_get_shortest_paths_bellman_ford()` that returned inc |
| [0.9.2] - 2021-04-14 / Other | Non-functional changes / [0.9.2] - 2021-04-14 | - Improved installation instructions and tutorial. |
| [0.9.1] - 2021-03-23 / Added | Added functionality / [0.9.1] - 2021-03-23 | - `igraph_vector_lex_cmp()` and `igraph_vector_colex_cmp()` for lexicographic |
| [0.9.1] - 2021-03-23 / Changed | Modified functionality / [0.9.1] - 2021-03-23 | - `igraph_community_multilevel()` is now randomized (PR #1696, thanks to Daniel Noom). |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - CMake settings that controlled the library installation directory name, such as `CMAKE_INSTALL_LIBDIR`, were not respe |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - Under some conditions, the generated pkg-config file contained an incorrect include directory path. |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - The following functions were not exported from the shared library: `igraph_subcomponent()`, `igraph_stack_ptr_free_all |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - Built-in random number generators (`igraph_rngtype_mt19937`, `igraph_rngtype_rand`, `igraph_rngtype_glibc2`) were not  |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - `igraph_layout_graphopt()` no longer rounds the `spring_length` parameter to an integer. |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - `igraph_get_all_shortest_paths_dijkstra()` no longer modifies the `res` vector's item destructor. |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - `igraph_get_shortest_path_bellman_ford()` did not work correctly when calculating paths to all vertices. |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - `igraph_arpack_rnsolve()` checks its parameters more carefully. |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - `igraph_community_to_membership()` does not crash anymore when `csize` is requested but `membership` is not. |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - `igraph_citing_cited_type_game()`: fixed memory leaks (PR #1700, thanks to Daniel Noom). |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - `igraph_transitivity_undirected()`, `igraph_transitivity_avglocal_undirected()` and `igraph_transitivity_barrat()` no  |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - `igraph_(personalized_)pagerank()` would return incorrect results for weighted multigraphs with fewer than 128 vertice |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - `igraph_diversity()` now checks its input more carefully, and throws an error when the input graph has multi-edges or  |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - `igraph_shortest_paths_johnson()` would return incorrect results when the `to` argument differed from `from` (thanks t |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - `igraph_is_graphical()` would fail to set the result variable for certain special degree sequences in the undirected s |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - Non-maximal clique finding functions would sometimes return incomplete results when finding more than 2147483647 (i.e. |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - GLPK internal errors no longer crash igraph. |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - Fixed some potential memory leaks that could happen on error conditions or when certain functions were interrupted. |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - When testing a DLL build on Windows, the `PATH` was sometimes not set correctly, causing the tests to fail (PR #1692). |
| [0.9.1] - 2021-03-23 / Fixed | Non-functional changes / [0.9.1] - 2021-03-23 | - When compiling from the git repository (as opposed to the release tarball), the build would fail with recent versions  |
| [0.9.1] - 2021-03-23 / Other | Non-functional changes / [0.9.1] - 2021-03-23 | - Documentation improvements. |
| [0.9.1] - 2021-03-23 / Other | Non-functional changes / [0.9.1] - 2021-03-23 | - Much faster documentation builds. |
| [0.9.1] - 2021-03-23 / Other | Non-functional changes / [0.9.1] - 2021-03-23 | - Allow using a pre-generated `arith.h` header for f2c when cross-compiling; see the Installation section of the documen |
| [0.9.1] - 2021-03-23 / Other | Non-functional changes / [0.9.1] - 2021-03-23 | - The `IGRAPH_ENABLE_LTO` build option now supports the `AUTO` value, which uses LTO only if the compiler supports it. W |
| [0.9.1] - 2021-03-23 / Other | Non-functional changes / [0.9.1] - 2021-03-23 | - The following functions are now interruptible: `igraph_grg_game()`, `igraph_sbm_game()`, `igraph_barabasi_game()`, `ig |
| [0.9.1] - 2021-03-23 / Other | Non-functional changes / [0.9.1] - 2021-03-23 | - Functions that use GLPK, such as `igraph_feedback_arc_set()` and `igraph_community_optimal_modularity()` are now inter |
| [0.9.1] - 2021-03-23 / Other | Non-functional changes / [0.9.1] - 2021-03-23 | - Add support for older versions of Clang that do not recognize the `-Wno-varargs` flag. |
| [0.9.1] - 2021-03-23 / Acknowledgments | Non-functional changes / [0.9.1] - 2021-03-23 | - Big thanks to Daniel Noom for continuing to expand the test suite and discovering and fixing several bugs in the proce |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - Eulerian paths/cycles (PR #1346): |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_is_eulerian()` finds out whether an Eulerian path/cycle exists. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_eulerian_path()` returns an Eulerian path. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_eulerian_cycle()` returns an Eulerian cycle. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - Efficiency (PR #1344): |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_global_efficiency()` computes the global efficiency of a network. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_local_efficiency()` computes the local efficiency around each vertex. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_average_local_efficiency()` computes the mean local efficiency. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - Degree sequences (PR #1445): |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_is_graphical()` checks if a degree sequence has a realization as a simple or multigraph, with or without self- |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_is_bigraphical()` checks if two degree sequences have a realization as a bipartite graph. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_realize_degree_sequence()` now supports constructing non-simple graphs as well. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - There is a new fatal error handling mechanism (PR #1548): |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_set_fatal_handler()` sets the fatal error handler. It is the only function in this functionality group that is |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - The macro `IGRAPH_FATAL()` and the functions `igraph_fatal()` and `igraph_fatalf()` raise a fatal error. These are for |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `IGRAPH_ASSERT()` is a replacement for the `assert()` macro. It is for internal use. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_fatal_handler_abort()` is the default fatal error handler. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - The new `IGRAPH_WARNINGF`, `IGRAPH_ERRORF` and `IGRAPH_FATALF` macros provide warning/error reporting with `printf`-li |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_average_path_length_dijkstra()` computes the mean shortest path length in weighted graphs (PR #1344). |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_get_shortest_paths_bellman_ford()` computes the shortest paths (including the vertex and edge IDs along the pa |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_get_shortest_path_bellman_ford()` is a wrapper for `igraph_get_shortest_paths_bellman_ford()` for the single p |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_is_same_graph()` cheks that two labelled graphs are the same (PR #1604). |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - Harmonic centrality (PR #1583): |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_harmonic_centrality()` computes the harmonic centrality of vertices. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_harmonic_centrality_cutoff()` computes the range-limited harmonic centrality. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - Range-limited centralities, currently equivalent to the old functions with names ending in `_estimate` (PR #1583): |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_closeness_cutoff()`. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_betweenness_cutoff()`. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_edge_betweenness_cutoff()`. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_vector_is_any_nan()` checks if any elements of an `igraph_vector_t` is NaN. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_inclist_size()` returns the number of vertices in an incidence list. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_lazy_adjlist_size()` returns the number of vertices in a lazy adjacency list. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_lazy_inclist_size()` returns the number of vertices in a lazy incidence list. |
| [0.9.0] - 2021-02-16 / Added | Added functionality / [0.9.0] - 2021-02-16 | - `igraph_bfs_simple()` now provides a simpler interface to the breadth-first search functionality. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - igraph now uses a CMake-based build sysyem. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - GMP support can no longer be disabled. When GMP is not present on the system, igraph will use an embedded copy of Mini |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - Bliss has been updated to version 0.75. Bliss functions are now interruptible. Thanks to Tommi Junttila for making thi |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - Adjacency and incidence lists: |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_adjlist_init()` and `igraph_lazy_adjlist_init()` now require the caller to specify what to do with loop and mu |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_inclist_init()` and `igraph_lazy_inclist_init()` now require the caller to specify what to do with loop edges. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - Adjacency and incidence lists now use `igraph_vector_int_t` consistently. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - Community detection: |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_community_multilevel()`: added resolution parameter. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_community_fluid_communities()`: graphs with no vertices or with one vertex only are now supported; they return |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - Modularity: |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_modularity()` and `igraph_modularity_matrix()`: added resolution parameter. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_modularity()` and `igraph_modularity_matrix()` now support the directed version of modularity. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_modularity()` returns NaN for graphs with no edges to indicate that the modularity is not well-defined for suc |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - Centralities: |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `cutoff=0` is no longer interpreted as infinity (i.e. no cutoff) in `betweenness`, `edge_betweenness` and `closeness`. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - The `nobigint` argument has been removed from `igraph_betweenness()`, `igraph_betweenness_estimate()` and `igraph_cent |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_closeness()` now considers only reachable vertices during the calculation (i.e. the closeness is calculated pe |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_closeness()` gained two additional output parameters, `reachable_count` and `all_reachable`, returning the num |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_pagerank()`, `igraph_personalized_pagerank()` and `igraph_personalized_pagerank_vs()` no longer support the `I |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - Shortest paths (PR #1344): |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_average_path_length()` now returns the number of disconnected vertex pairs in the new `unconn_pairs` output ar |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_diameter()` now return the result as an `igraph_real_t` instead of an `igraph_integer_t`. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_average_path_length()` and `igraph_diameter()` now return `IGRAPH_INFINITY` when `unconn=FALSE` and the graph  |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - Trait-based random graph generators: |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_callaway_traits_game()` and `igraph_establishment_game()` now have an optional output argument to retrieve the |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_callaway_traits_game()` and `igraph_establishment_game()` now allow omitting the type distribution vector, in  |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_asymmetric_preference_game()` now accept a different number of in-types and out-types. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_subisomorphic_lad()` now supports graphs with self-loops. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_is_chordal()` and `igraph_maximum_cardinality_search()` now support non-simple graphs and directed graphs. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_realize_degree_sequence()` has an additional argument controlling whether multi-edges or self-loops are allowe |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_is_connected()` now returns false for the null graph; see <https://github.com/igraph/igraph/issues/1538> for t |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_lapack_ddot()` is renamed to `igraph_blas_ddot()`. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_to_directed()`: added RANDOM and ACYCLIC modes (PR #1511). |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_topological_sorting()` now issues an error if the input graph is not acyclic. Previously it issued a warning. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_vector_(which_)(min\|max\|minmax)()` now handles NaN elements. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_i_set_attribute_table()` is renamed to `igraph_set_attribute_table()`. |
| [0.9.0] - 2021-02-16 / Changed | Modified functionality / [0.9.0] - 2021-02-16 | - `igraph_i_sparsemat_view()` is renamed to `igraph_sparsemat_view()`. |
| [0.9.0] - 2021-02-16 / Deprecated | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - `igraph_is_degree_sequence()` and `igraph_is_graphical_degree_sequence()` are deprecated in favour of the newly added  |
| [0.9.0] - 2021-02-16 / Deprecated | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - `igraph_closeness_estimate()` is deprecated in favour of the newly added `igraph_closeness_cutoff()`. |
| [0.9.0] - 2021-02-16 / Deprecated | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - `igraph_betweenness_estimate()` and `igraph_edge_betweenness_estimate()` are deprecated in favour of the newly added ` |
| [0.9.0] - 2021-02-16 / Deprecated | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - `igraph_adjlist_remove_duplicate()` and `igraph_inclist_remove_duplicate()` are now deprecated in favour of the new co |
| [0.9.0] - 2021-02-16 / Removed | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - The following functions, all deprecated in igraph 0.6, have been removed (PR #1562): |
| [0.9.0] - 2021-02-16 / Removed | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - `igraph_adjedgelist_init()`, `igraph_adjedgelist_destroy()`, `igraph_adjedgelist_get()`, `igraph_adjedgelist_print()`, |
| [0.9.0] - 2021-02-16 / Removed | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - `igraph_lazy_adjedgelist_init()`, `igraph_lazy_adjedgelist_destroy()`, `igraph_lazy_adjedgelist_get()`, `igraph_lazy_a |
| [0.9.0] - 2021-02-16 / Removed | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - `igraph_adjacent()`. |
| [0.9.0] - 2021-02-16 / Removed | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - `igraph_es_adj()`. |
| [0.9.0] - 2021-02-16 / Removed | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - `igraph_subgraph()`. |
| [0.9.0] - 2021-02-16 / Removed | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - `igraph_pagerank_old()`, deprecated in 0.7, has been removed. |
| [0.9.0] - 2021-02-16 / Removed | Deprecated and removed functionality / [0.9.0] - 2021-02-16 | - `igraph_vector_bool` and `igraph_matrix_bool` functions that relied on inequality-comparing `igraph_bool_t` values are |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - Betweenness calculations are no longer at risk from integer overflow. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - The actual cutoff distance used in closeness calculation was one smaller than the `cutoff` parameter. This is correcte |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_layout_gem()` was not interruptible; now it is. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_barabasi_aging_game()` now checks its parameters more carefully. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_callaway_traits_game()` and `igraph_establishment_game()` now check their parameters. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_lastcit_game()` checks its parameters more carefully, and no longer crashes with zero vertices (PR #1625). |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_cited_type_game()` incorrectly rounded the attractivity vector entries to integers. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_residual_graph()` now returns the correct _residual_ capacities; previously it wrongly returned the original c |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_psumtree_update()` now checks for negative values and NaN. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_communities_spinglass()`: fixed several memory leaks in the `IGRAPH_SPINCOMM_IMP_NEG` implementation. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_incident()` now returns edges in the same order as `igraph_neighbors()`. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_modularity_matrix()` returned incorrect results for weighted graphs. This is now fixed. (PR #1649, thanks to D |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_lapack_dgetrf()` would crash when passing `NULL` for its `ipiv` argument (thanks for the fix to Daniel Noom). |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - Some `igraph_matrix` functions would fail to report errors on out-of-memory conditions. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_maxdegree()` now returns 0 for the null graph or empty vector set. Previously, it did not handle this case. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_vector_bool_all_e()` now considers all nonzero (i.e. "true") values to be the same. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - PageRank (PR #1640): |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_(personalized_)pagerank(_vs)()` now check their parameters more carefully. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_personalized_pagerank()` no longer modifies its `reset` parameter. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_(personalized_)pagerank(_vs)`: the `IGRAPH_PAGERANK_ALGO_ARPACK` method now handles self-loops correctly. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_personalized_pagerank(_vs)()`: the result retuned for edgeless or all-zero-weight graphs with the `IGRAPH_PAGE |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - `igraph_personalized_pagerank(_vs)()` with a non-uniform personalization vector, a disconnected graph and the `IGRAPH_ |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - Fixed crashes in several functions when passing a weighted graph with zero edges (due to `vector_min` being called on  |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - Fixed problems in several functions when passing in a graph with zero vertices. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - Weighted betweenness, closeness, PageRank, shortest path calculations and random walk functions now check if any weigh |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - Many functions now reject input arguments containing NaN values. |
| [0.9.0] - 2021-02-16 / Fixed | Non-functional changes / [0.9.0] - 2021-02-16 | - Compatibility with the PGI compiler. |
| [0.9.0] - 2021-02-16 / Other | Non-functional changes / [0.9.0] - 2021-02-16 | - Documentation improvements. |
| [0.9.0] - 2021-02-16 / Other | Non-functional changes / [0.9.0] - 2021-02-16 | - Improved error and warning messages. |
| [0.9.0] - 2021-02-16 / Other | Non-functional changes / [0.9.0] - 2021-02-16 | - More robust error handling. |
| [0.9.0] - 2021-02-16 / Other | Non-functional changes / [0.9.0] - 2021-02-16 | - General code cleanup to reduce the number of compiler warnings. |
| [0.9.0] - 2021-02-16 / Other | Non-functional changes / [0.9.0] - 2021-02-16 | - igraph's source files have been re-organized for better maintainability. |
| [0.9.0] - 2021-02-16 / Other | Non-functional changes / [0.9.0] - 2021-02-16 | - Debugging aid: When igraph is build with AddressSanitizer, the default error handler prints a stack trace before exiti |
| [0.9.0] - 2021-02-16 / Other | Non-functional changes / [0.9.0] - 2021-02-16 | - igraph can now be built with an external CXSparse library. |
| [0.9.0] - 2021-02-16 / Other | Non-functional changes / [0.9.0] - 2021-02-16 | - The references to igraph source files in error and warning messages are now always relative to igraph's base directory |
| [0.9.0] - 2021-02-16 / Other | Non-functional changes / [0.9.0] - 2021-02-16 | - When igraph is built as a shared library, only public symbols are exported even on Linux and macOS. |
| [0.9.0] - 2021-02-16 / Acknowledgments | Non-functional changes / [0.9.0] - 2021-02-16 | - Thanks to Daniel Noom for significantly expanding igraph's test coverage and exposing several issues in the process! |
| [0.8.5] - 2020-12-07 / Changed | Modified functionality / [0.8.5] - 2020-12-07 | - `igraph_write_graph_pajek()`: the function now always uses the platform-native line endings (CRLF on Windows, LF on Un |
| [0.8.5] - 2020-12-07 / Fixed | Non-functional changes / [0.8.5] - 2020-12-07 | - Fixed several compilation issues with MINGW32/64 (PR #1554) |
| [0.8.5] - 2020-12-07 / Fixed | Non-functional changes / [0.8.5] - 2020-12-07 | - `igraph_layout_davidson_harel()` was not interruptible; now it is. |
| [0.8.5] - 2020-12-07 / Fixed | Non-functional changes / [0.8.5] - 2020-12-07 | - Added a missing memory cleanup call in `igraph_i_cattribute_combine_vertices()`. |
| [0.8.5] - 2020-12-07 / Fixed | Non-functional changes / [0.8.5] - 2020-12-07 | - Fixed a few memory leaks in test cases. |
| [0.8.4] - 2020-11-24 / Fixed | Non-functional changes / [0.8.4] - 2020-11-24 | - `igraph_i_cattribute_combine_vertices()`: fixed invalid cleanup code that eventually filled up the "finally" stack whe |
| [0.8.4] - 2020-11-24 / Fixed | Non-functional changes / [0.8.4] - 2020-11-24 | - `igraph_hrg_sample()`: fixed incorrect function prototype |
| [0.8.4] - 2020-11-24 / Fixed | Non-functional changes / [0.8.4] - 2020-11-24 | - `igraph_is_posinf()` and `igraph_is_neginf()`: fixed incorrect result on platforms where the sign of the result of `is |
| [0.8.4] - 2020-11-24 / Fixed | Non-functional changes / [0.8.4] - 2020-11-24 | - Fixed building with vendored LAPACK and external BLAS |
| [0.8.4] - 2020-11-24 / Fixed | Non-functional changes / [0.8.4] - 2020-11-24 | - Fixed building with XCode 12.2 on macOS |
| [0.8.4] - 2020-11-24 / Other | Non-functional changes / [0.8.4] - 2020-11-24 | - Documentation improvements |
| [0.8.4] - 2020-11-24 / Other | Non-functional changes / [0.8.4] - 2020-11-24 | - General code cleanup to reduce the number of compiler warnings |
| [0.8.3] - 2020-10-02 / Added | Added functionality / [0.8.3] - 2020-10-02 | - `igraph_vector_binsearch_slice()` performs binary search on a sorted slice of a vector. |
| [0.8.3] - 2020-10-02 / Changed | Modified functionality / [0.8.3] - 2020-10-02 | - `igraph_eigenvector_centrality()` assumes the adjacency matrix of undirected graphs to have twice the number of self-l |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_isomorphic()` now verifies that the input graphs have no multi-edges (PR #1464). |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_difference()` was creating superfluous self loops (#597). |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_count_multiple()` was giving incorrect results for self-loops in directed graph (PR #1399). |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_betweenness_estimate()`: fixed incorrect results with finite cutoff (PR #1392). |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_count_multiple()` was giving incorrect results for self-loops in directed graph (PR #1399). |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_eigen_matrix_symmetric()`: fixed incorrect matrix multiplication (PR #1379). |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - Corrected several issues that could arise during an error condition (PRs #1405, #1406, #1438). |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_realize_degree_sequence()` did not correctly detect some non-graphical inputs. |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_is_graphical_degree_sequence()`: fixed incorrect results in undirected case (PR #1441). |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_community_leiden()`: fixed incorrect result when self-loops are present (PR #1476). |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_eigenvector_centrality()`: fixed incorrect value for isolated vertices in weighted graphs. |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_eigenvector_centrality()`: corrected the handling of self-loops. |
| [0.8.3] - 2020-10-02 / Fixed | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_layout_reingold_tilford()`: fixed an issue where branches of the tree would sometimes overlap. |
| [0.8.3] - 2020-10-02 / Other | Non-functional changes / [0.8.3] - 2020-10-02 | - `igraph_degree_sequence_game()`: improved performance with `IGRAPH_DEGSEQ_SIMPLE_NO_MULTIPLE_UNIFORM` method. |
| [0.8.3] - 2020-10-02 / Other | Non-functional changes / [0.8.3] - 2020-10-02 | - Improved the robustness of the test suite. |
| [0.8.3] - 2020-10-02 / Other | Non-functional changes / [0.8.3] - 2020-10-02 | - Documentation improvements. |
| [0.8.3] - 2020-10-02 / Other | Non-functional changes / [0.8.3] - 2020-10-02 | - Improved error and warning messages. |
| [0.8.3] - 2020-10-02 / Other | Non-functional changes / [0.8.3] - 2020-10-02 | - Improved compatibility with recent versions of Microsoft Visual C. |
| [0.8.2] - 2020-04-28 / Changed | Modified functionality / [0.8.2] - 2020-04-28 | - Improved argument checking: `igraph_all_st_mincuts()` and `igraph_sir()` |
| [0.8.2] - 2020-04-28 / Changed | Modified functionality / [0.8.2] - 2020-04-28 | - Improved interruptibility: `igraph_sir()` |
| [0.8.2] - 2020-04-28 / Fixed | Non-functional changes / [0.8.2] - 2020-04-28 | - `igraph_community_leiden()`: fixed crash when interrupting |
| [0.8.2] - 2020-04-28 / Fixed | Non-functional changes / [0.8.2] - 2020-04-28 | - The tests are now more robust. Some incorrect test failures were fixed when |
| [0.8.2] - 2020-04-28 / Other | Non-functional changes / [0.8.2] - 2020-04-28 | - Improved error messages from `igraph_sir()`. |
| [0.8.2] - 2020-04-28 / Other | Non-functional changes / [0.8.2] - 2020-04-28 | - Improved compatibility with more recent versions of Microsoft Visual C. |
| [0.8.1] - 2020-03-13 / Changed | Modified functionality / [0.8.1] - 2020-03-13 | - Improved interruptability: `igraph_degree_sequence_game()` |
| [0.8.1] - 2020-03-13 / Changed | Modified functionality / [0.8.1] - 2020-03-13 | - Improved argument checking: `igraph_forest_fire_game()` |
| [0.8.1] - 2020-03-13 / Changed | Modified functionality / [0.8.1] - 2020-03-13 | - Updated the plfit library to version 0.8.1 |
| [0.8.1] - 2020-03-13 / Fixed | Non-functional changes / [0.8.1] - 2020-03-13 | - `igraph_community_edge_betweenness()`: fix for graphs with no edges (PR #1312) |
| [0.8.1] - 2020-03-13 / Fixed | Non-functional changes / [0.8.1] - 2020-03-13 | - `igraph_bridges()` now handles multigraphs correctly (PR #1335) |
| [0.8.1] - 2020-03-13 / Fixed | Non-functional changes / [0.8.1] - 2020-03-13 | - `igraph_avg_nearest_neighbor_degree()`: fix for memory leak in weighted case (PR #1339) |
| [0.8.1] - 2020-03-13 / Fixed | Non-functional changes / [0.8.1] - 2020-03-13 | - `igraph_community_leiden()`: fix crash bug (PR #1357) |
| [0.8.1] - 2020-03-13 / Other | Non-functional changes / [0.8.1] - 2020-03-13 | - Included `ACKOWLEDGEMENTS.md` |
| [0.8.1] - 2020-03-13 / Other | Non-functional changes / [0.8.1] - 2020-03-13 | - Documentation improvements |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - Trees |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_to_prufer()` and `igraph_from_prufer()` convert labelled trees to/from Prüfer sequences |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_tree_game()` samples uniformly from the set of labelled trees |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_is_tree()` checks if a graph is a tree |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_random_spanning_tree()` picks a spanning tree of a graph uniformly at random |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_random_edge_walk()` returns the indices of edges traversed by a random walk; useful for multigraphs |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - Community detection |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_community_fluid_communities()` detects communities based on interacting fluids |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_community_leiden()` detects communities with the Leiden method |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - Cliques |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_maximal_cliques_hist()` counts maximal cliques of each size |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_maximal_cliques_callback()` calls a function for each maximal clique |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_clique_size_hist()` counts cliques of each size |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_cliques_callback()` calls a function for each clique |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_weighted_cliques()` finds weighted cliques in graphs with integer vertex weights |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_weighted_clique_number()` computes the weighted clique number |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_largest_weighted_cliques()` finds the largest weighted cliques |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - Graph generators |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_hsbm_game()` for a hierarchical stochastic block model |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_hsbm_list_game()` for a more general hierarchical stochastic block model |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_correlated_game()` generates pairs of correlated random graphs by perturbing existing adjacency matrix |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_correlated_pair_game()` generates pairs of correlated random graphs |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_tree_game()` samples uniformly from the set of labelled trees |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_dot_product_game()` generates a random dot product graph |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_realize_degree_sequence()` creates a single graph with a given degree sequence (Havel-Hakimi algorithm) |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - Graph embeddings |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_adjacency_spectral_embedding()` and `igraph_laplacian_spectral_embedding()` provide graph embedddings |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_dim_select()` provides dimensionality selection for singular values using profile likelihood |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - Isomorphism |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_automorphism_group()` computes the generators of the automorphism group of a simple graph |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_simplify_and_colorize()` encodes edge and self-loop multiplicities into edge and vertex colors; use in conjunc |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - Other |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_bridges()` finds edges whose removal would disconnect a graph |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_vertex_coloring_greedy()` computes a vertex coloring using a greedy algorithm |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_rewire_directed_edges()` randomly rewires only the starting points or only the endpoints of directed edges |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - Various `igraph_local_scan_*` functions provide local counts and statistics of neighborhoods |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_sample_sphere_surface()` samples points uniformly from the surface of a sphere |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_sample_sphere_volume()` samples points uniformly from the volume of a sphere |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_sample_dirichlet()` samples points from a Dirichlet distribution |
| [0.8.0] - 2020-01-29 / Added | Added functionality / [0.8.0] - 2020-01-29 | - `igraph_malloc()`, to be paired with the existing `igraph_free()` |
| [0.8.0] - 2020-01-29 / Changed | Modified functionality / [0.8.0] - 2020-01-29 | - `igraph_degree_sequence_game()`: new method added for uniform sampling: `IGRAPH_DEGSEQ_SIMPLE_NO_MULTIPLE_UNIFORM` |
| [0.8.0] - 2020-01-29 / Changed | Modified functionality / [0.8.0] - 2020-01-29 | - `igraph_modularity_matrix()`: removed `membership` argument (PR #1194) |
| [0.8.0] - 2020-01-29 / Changed | Modified functionality / [0.8.0] - 2020-01-29 | - `igraph_avg_nearest_neighbor_degree()`: added `mode` and `neighbor_degree_mode` arguments (PR #1214). |
| [0.8.0] - 2020-01-29 / Changed | Modified functionality / [0.8.0] - 2020-01-29 | - `igraph_get_all_simple_paths()`: added `cutoff` argument (PR #1232). |
| [0.8.0] - 2020-01-29 / Changed | Modified functionality / [0.8.0] - 2020-01-29 | - `igraph_unfold_tree()`: no longer preserves edge ordering of original graph |
| [0.8.0] - 2020-01-29 / Changed | Modified functionality / [0.8.0] - 2020-01-29 | - `igraph_decompose()`: support strongly connected components |
| [0.8.0] - 2020-01-29 / Changed | Modified functionality / [0.8.0] - 2020-01-29 | - `igraph_isomorphic_bliss()`, `igraph_canonical_permutation()`, `igraph_automorphisms()`: added additional arguments to |
| [0.8.0] - 2020-01-29 / Changed | Modified functionality / [0.8.0] - 2020-01-29 | - `igraph_extended_chordal_ring`: added argument to support direction (PR #1096), and fixed issue #1093. |
| [0.8.0] - 2020-01-29 / Other | Non-functional changes / [0.8.0] - 2020-01-29 | - The [Bliss isomorphism library](http://www.tcs.hut.fi/Software/bliss/) was updated to version 0.73. This version adds  |
| [0.8.0] - 2020-01-29 / Other | Non-functional changes / [0.8.0] - 2020-01-29 | - igraph now uses the high-performance [Cliquer library](https://users.aalto.fi/~pat/cliquer.html) to find (non-maximal) |
| [0.8.0] - 2020-01-29 / Other | Non-functional changes / [0.8.0] - 2020-01-29 | - Provide proper support for Windows, using `__declspec(dllexport)` and `__declspec(dllimport)` for `DLL`s and static us |
| [0.8.0] - 2020-01-29 / Other | Non-functional changes / [0.8.0] - 2020-01-29 | - Provided integer versions of `dqueue` and `stack` data types. |

Total items mapped: 1182