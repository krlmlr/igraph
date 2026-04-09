# Changelog Reorganization: Proof of Work

## Scope

This reorganization covers versions 1.0.0 and later only.
Versions prior to 1.0.0 (34 versions: [0.10.17] - 2025-09-19, [0.10.16] - 2025-06-10, [0.10.15], [0.10.13], [0.10.12] - 2024-05-06, [0.10.11] - 2024-04-02, [0.10.10] - 2024-02-13, [0.10.9] - 2024-02-02, [0.10.8] - 2023-11-17, [0.10.7] - 2023-09-04, [0.10.6] - 2023-07-13, [0.10.5] - 2023-06-29, [0.10.4] - 2023-01-26, [0.10.3] - 2022-12-30, [0.10.2] - 2022-10-14, [0.10.1] - 2022-09-08, [0.10.0] - 2022-09-05, [0.9.10] - 2022-09-02, [0.9.9] - 2022-06-04, [0.9.8] - 2022-04-08, [0.9.7] - 2022-03-16, [0.9.6] - 2022-01-05, [0.9.5] - 2021-11-11, [0.9.4] - 2021-05-31, [0.9.3] - 2021-05-05, [0.9.2] - 2021-04-14, [0.9.1] - 2021-03-23, [0.9.0] - 2021-02-16, [0.8.5] - 2020-12-07, [0.8.4] - 2020-11-24, [0.8.3] - 2020-10-02, [0.8.2] - 2020-04-28, [0.8.1] - 2020-03-13, [0.8.0] - 2020-01-29) were removed from the changelog.

## Category Mapping

Each original subsection header was mapped to one of four new top-level categories:

| Original Section | New Category | Rationale |
|---|---|---|
| Fixed | Non-functional changes | Bug fixes do not add or modify API surface |
| Other | Non-functional changes | Documentation, performance, build system improvements |
| Acknowledgments | Non-functional changes | Credits do not affect functionality |
| Added | Added functionality | New functions, types, and features |
| Highlights | Added functionality | Summary of key new features |
| Changed | Modified functionality | Behavioral changes to existing API |
| Breaking changes | Modified functionality | API-breaking modifications |
| Finalized experimental functions | Modified functionality | Functions changed from experimental to stable |
| Release notes | Modified functionality | Version overview describing changes |
| Deprecated | Deprecated and removed functionality | Functions marked for future removal |
| Removed | Deprecated and removed functionality | Functions/features that were removed |
| (items with no subsection) | Modified functionality | Preamble items describing changes |

## Verification Summary

- **Original changelog**: 1182 total items across 36 versions
- **Versions included** (>= 1.0.0): 2 versions, 187 items
- **Versions excluded** (< 1.0.0): 34 versions, 995 items
- **New changelog items**: 187
- **Match**: ✓ All items from included versions are present

## Reassessment Findings

After a second thorough review of the reorganization:

1. **1 "Fixed" items contain behavioral language** (e.g., "now validates...", "now returns..."). These were kept in "Non-functional changes" because they describe corrections of incorrect behavior, not intentional API changes. Examples:

   - `- `igraph_community_spinglass_single()` now uses `igraph_real_t` for its `inner_links` and `outer_li`

2. **1 "Other" items describe performance improvements**. These are kept in "Non-functional changes" because they do not change the API contract, only the implementation speed. Examples:

   - `- Improved performance when creating graphs from dense adjacency matrices (`igraph_adjacency()` and `

4. **5 "Highlights" items** from version [1.0.0] were placed in "Added functionality". These are high-level summaries of new features and capabilities, so "Added functionality" is appropriate.

5. **1 "Finalized experimental functions" item(s)** placed in "Modified functionality". These describe a status change (experimental → stable) of existing functions, which is a modification.

**Conclusion**: The categorization is consistent with the mapping rules. Edge cases (validation fixes, performance improvements) stay in their mapped categories because the original section headers reflect the original authors' intent for how these changes should be classified.

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

Total items mapped: 187
