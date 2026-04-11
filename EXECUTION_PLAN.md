# Execution Plan: main → next commit series

## Overview

**Goal**: Create a series of commits from `main` to `next` where each commit
represents a logical unit, passes all tests, and can be grafted in parallel
where possible. Ordered by downstream R package impact (most work first).

**Total scope**: 1,305 files changed, 85,695 insertions, 29,789 deletions
(115,484 total lines affected).

## Commit dependency graph

```
                    ┌──────────────┐
                    │  C01: Core   │
                    │  types/infra │
                    │  (8,200 L)   │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────────┐
              │            │                │
              ▼            ▼                ▼
    ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
    │ C02: Attribs │ │ C03: Graph   │ │ C04: Depr.   │
    │ & data struc │ │ manipulation │ │ removals     │
    │ (6,400 L)    │ │ (5,500 L)    │ │ (5,600 L)    │
    └──────┬───────┘ └──────┬───────┘ └──────┬───────┘
           │                │                │
           └────────┬───────┘                │
                    │                        │
              ┌─────▼────────┐               │
              │ C05: Paths   │               │
              │ & distances  │               │
              │ (2,800 L)    │               │
              └──────┬───────┘               │
                     │                       │
    ┌────────────────┼───────────────────────┤
    │                │                       │
    ▼                ▼                       ▼
┌──────────────┐ ┌──────────────┐  ┌──────────────┐
│ C06: Central │ │ C07: Games   │  │ C08: Cliques │
│ & community  │ │ & generators │  │ iso, layout  │
│ (4,900 L)    │ │ (3,200 L)    │  │ & misc NFC   │
│              │ │              │  │ (3,000 L)    │
└──────┬───────┘ └──────┬───────┘  └──────┬───────┘
       │                │                 │
       ▼                │                 │
┌──────────────┐        │                 │
│ C09: Infomap │        │                 │
│ vendor+algo  │        │                 │
│ (16,700 L)   │        │                 │
└──────┬───────┘        │                 │
       │                │                 │
       └────────┬───────┘                 │
                │                         │
          ┌─────▼────────┐                │
          │ C10: Qhull + │                │
          │ spatial nets  │                │
          │ (34,700 L)   │                │
          └──────┬───────┘                │
                 │                        │
                 └────────────┬───────────┘
                              │
                        ┌─────▼────────┐
                        │ C11: IO,docs │
                        │ finalize,    │
                        │ tests, misc  │
                        │ (28,400 L)   │
                        └──────────────┘
```

## Commit details (ordered by downstream R package impact)

### C01: Core types, error codes, and infrastructure
**Lines**: ~8,200 · **Files**: ~120 · **Downstream R work**: HIGH
**Parallelism**: None (must be first — all other commits depend on this)

This is the foundation commit. Everything else builds on these changes.

**Changes**:
- `igraph_integer_t` → `igraph_int_t` rename (alias kept)
- Error code consolidation (`IGRAPH_EINVEVECTOR`, `IGRAPH_NONSQUARE`, `IGRAPH_EGLP`, `IGRAPH_ELAPACK`, `IGRAPH_CPUTIME`, `IGRAPH_EDIVZERO`, `IGRAPH_EATTRIBUTES`, `IGRAPH_ENEGLOOP` removed; `IGRAPH_EINVEID`, `IGRAPH_EARPACK` added)
- `igraph_multiple_t` enum removed
- Interruption handler signature change (`void *` removed, returns `igraph_bool_t`)
- `igraph_status()`/`igraph_statusf()` error forwarding change
- `igraph_setup()` introduction
- `RNG_BEGIN()`/`RNG_END()` removal
- `igraph_rng_set_default()` return value change
- Build system: C++14 requirement, single `<igraph.h>` header rule
- `igraph_topology.h` → `igraph_isomorphism.h` rename
- `IGRAPH_POSINFINITY`/`IGRAPH_NEGINFINITY` → `IGRAPH_INFINITY`
- `igraph_Calloc()`/`igraph_Realloc()`/`igraph_Free()` → macro forms
- Vendor updates: mini-gmp (117 L), plfit (56 L), f2c (9 L), cs (6 L), lapack (3 L)

**R package impact**: Every C-level binding that uses error codes, interruption,
or RNG needs updating. This is the single most disruptive commit for downstream.

---

### C02: Attributes and core data structures
**Lines**: ~6,400 · **Files**: ~80 · **Depends on**: C01

**Changes**:
- `igraph_attribute_handler_t` typed argument (`igraph_attribute_record_list_t`)
- `igraph_attribute_table_t.gettype` → `get_type`
- Attribute retrieval: append instead of clear
- `IGRAPH_ATTRIBUTE_DEFAULT` removed
- `igraph_attribute_record_t.value` union
- `igraph_vector_view()`/`igraph_matrix_view()` return value change
- `igraph_vector_swap()`, `igraph_matrix_swap()`, `igraph_vector_reverse()`, `igraph_vector_shuffle()`, `igraph_vector_swap_elements()` no longer return error codes
- `igraph_vector_append()`/`igraph_strvector_append()` allocation strategy
- `igraph_vector_difference_sorted()` multiset handling
- `igraph_strvector_push_back_len()` size_t parameter
- `igraph_strvector_print()` file parameter removed
- `igraph_vector_list_swap()`/`igraph_graph_list_swap()` no error code
- New: `igraph_vector_ptr_capacity()`, `igraph_vector_ptr_resize_min()`
- New: `igraph_strvector_fprint()`
- New: `igraph_matrix_copy_to()` storage parameter
- New: `igraph_vector_difference_and_intersection_sorted()`
- New: `igraph_edges()` `bycol` argument
- `igraph_array3_t` and all 3D array functions removed

**R package impact**: HIGH — C attribute handler must be rewritten; vector/matrix
API changes affect nearly every binding.

---

### C03: Core graph manipulation and basic properties
**Lines**: ~5,500 · **Files**: ~60 · **Depends on**: C01

**Changes**:
- `igraph_permute_vertices()` semantics inversion
- `igraph_canonical_permutation()`/`igraph_canonical_permutation_bliss()` semantics change
- `igraph_delete_vertices_map()` (was `igraph_delete_vertices_idx()`) mapping change
- Edge order in `igraph_(weighted_)adjacency()`/`igraph_biadjacency()`
- `igraph_loops_t` type for `loops` arguments (was `igraph_bool_t`) across 7 functions
- `igraph_neighbors()`/`igraph_vs_adj()` gain `loops` + `multiple` args
- `igraph_incident()`/`igraph_es_incident()` gain `loops` arg
- `igraph_density()` gains `weights` parameter
- `igraph_is_simple()` gains direction argument
- `igraph_delete_vertices_idx()` deprecated in favor of `igraph_delete_vertices_map()`
- `IGRAPH_UNLIMITED` constant

**R package impact**: HIGH — permutation semantics change is subtle and easy to
get wrong; loops_t change touches many functions.

---

### C04: Deprecated function removals
**Lines**: ~5,600 · **Files**: ~70 · **Depends on**: C01
**Parallelism**: Can run in parallel with C02 and C03

**Changes** (all removals):
- `igraph_read_graph_dimacs()`/`igraph_write_graph_dimacs()`
- `igraph_random_edge_walk()`
- `igraph_erdos_renyi_game()`/`igraph_bipartite_game()`
- `igraph_convex_hull()`
- `igraph_hub_score()`/`igraph_authority_score()`
- `igraph_vector_copy()`/`igraph_matrix_copy()`
- `igraph_vector_e()`/`igraph_vector_e_ptr()`/`igraph_matrix_e()`/`igraph_matrix_e_ptr()`
- `igraph_adjacent_triangles()`
- `igraph_are_connected()`
- `igraph_deterministic_optimal_imitation()`/`igraph_moran_process()`/etc. (microscopic update: 1,209 L)
- `igraph_tree()`/`igraph_lattice()`/`igraph_subgraph_edges()`
- `igraph_vector_qsort_ind()`/`igraph_vector_binsearch2()`/`igraph_vector_move_interval2()`
- `igraph_automorphisms()`/`igraph_isomorphic_function_vf2()`/etc.
- `igraph_decompose_destroy()`/`igraph_transitive_closure_dag()`
- `igraph_minimum_spanning_tree_prim()`/`igraph_minimum_spanning_tree_unweighted()`
- Sparsemat removals (6 functions + view)
- `igraph_laplacian()` / `igraph_rng_get_dirichlet()`
- `igraph_vs_seq()`/`igraph_vss_seq()`/`igraph_es_seq()`/`igraph_ess_range()`/`igraph_vector_init_seq()`
- `igraph_clusters()`
- `igraph_zeroin()`
- `igraph_sample_dirichlet()`/`igraph_sample_sphere_surface()`/`igraph_sample_sphere_volume()`
- `igraph_fileformat_type_t`
- `igraph_scalar_function_t`/`igraph_vector_function_t`

**R package impact**: MEDIUM-HIGH — each removed function needs its R binding
updated to point to the replacement. Straightforward but many functions.

---

### C05: Paths, distances, and cycles
**Lines**: ~2,800 · **Files**: ~30 · **Depends on**: C01, C03

**Changes**:
- `igraph_distances()` family gains `weights` argument (auto-selects algorithm)
- Weighted path functions merged into base functions (diameter, radius, eccentricity, etc.)
- `igraph_average_path_length()` `weights` parameter moved to 2nd position
- `igraph_get_all_simple_paths()` returns `igraph_vector_int_list_t`, gains `max_results`, mode moved
- `igraph_distances_johnson()` gains `mode` parameter
- `igraph_fundamental_cycles()`/`igraph_minimum_cycle_basis()` parameter changes
- `igraph_simple_cycles()` gains `max_results`

**R package impact**: HIGH — distance function API redesign requires updating
many R functions that call weighted/unweighted variants.

---

### C06: Centralities and community detection
**Lines**: ~4,900 · **Files**: ~45 · **Depends on**: C01, C05
**Parallelism**: Can run in parallel with C07 and C08

**Changes**:
- Betweenness functions: `normalized` parameter, standardized ordering (6 functions)
- `igraph_hub_and_authority_scores()` `scale` removed, warnings added
- `igraph_eigenvector_centrality()` family: `mode` replaces `directed`, `scale` removed, warning
- `igraph_pagerank()` family: parameter ordering standardized
- `igraph_edge_betweenness()` gains `eids` parameter
- `igraph_community_leiden()`: two weight params for directed graphs
- `igraph_community_leading_eigenvector()`: `history` type change
- `igraph_community_optimal_modularity()`: `resolution` param, `weight` moved
- `igraph_community_infomap()` parameter renames (`e_weights`→`edge_weights`, etc.)
- `igraph_community_label_propagation()` gains LPA variant parameter
- `igraph_community_edge_betweenness()` gains `weights`+`lengths`
- `igraph_community_spinglass_single()` uses `igraph_real_t` for outputs
- New: `igraph_community_leiden_simple()`

**R package impact**: HIGH — many centrality functions change signatures;
community detection widely used.

---

### C07: Random graph generators
**Lines**: ~3,200 · **Files**: ~35 · **Depends on**: C01
**Parallelism**: Can run in parallel with C06 and C08

**Changes**:
- `igraph_edge_type_sw_t` replaces `loops`/`multiple` booleans across 10 functions
- `igraph_degree_sequence_game()` NULL in-degree for undirected
- `igraph_barabasi_game()` family: NULL outseq for missing sequence
- `igraph_correlated_game()` first-arg change, permutation semantics
- `igraph_lcf()` ↔ `igraph_lcf_small()` rename swap
- `igraph_rewire()` gains `allowed_edge_types`, `igraph_rewiring_stats_t`, enum removed
- New: `igraph_iea_game()`, `igraph_bipartite_iea_game()`
- New: `igraph_rng_sample_dirichlet()`/sphere functions
- `igraph_minimum_spanning_tree()` gains `method` parameter

**R package impact**: MEDIUM-HIGH — `igraph_edge_type_sw_t` is a pattern change
that affects many generator bindings.

---

### C08: Cliques, isomorphism, layouts, and misc NFC
**Lines**: ~3,000 · **Files**: ~50 · **Depends on**: C01
**Parallelism**: Can run in parallel with C06 and C07

**Changes**:
- Cliques: `igraph_weighted_cliques()` param ordering, `igraph_maximal_cliques_callback()` ordering
- Cliques: `max_results` parameter across 7 functions
- `igraph_maximal_independent_sets()` gains `min_size`/`max_size`
- Isomorphism: `igraph_count_automorphisms()`/`igraph_automorphism_group()`/`igraph_canonical_permutation()` BLISS split
- `igraph_subisomorphic_lad()` CPU time limit removed
- `igraph_isoclass_subgraph()` `igraph_vs_t` parameter
- Layout: `igraph_layout_sugiyama()` no extended graph
- Motifs: `igraph_motifs_randesu_no()`/`igraph_motifs_randesu_estimate()` igraph_real_t
- Similarity: `igraph_similarity_jaccard()`/`igraph_similarity_dice()` two vertex sets
- Foreign: Pajek `name` attribute mapping
- `igraph_get_stochastic_sparse()` zero-sum behavior
- `igraph_minimum_size_separators()` complete graph behavior
- `igraph_adjacency()` LOOPS_TWICE → LOOPS_ONCE for directed
- New: `igraph_weighted_biadjacency()`
- `igraph_biadjacency()` truncation change
- IO changes (graphml, ncol, lgl)

**R package impact**: MEDIUM — each change is self-contained; many are simple
parameter additions or renames.

---

### C09: Infomap vendor update
**Lines**: ~16,700 · **Files**: ~60 · **Depends on**: C06
**Parallelism**: Can run in parallel with C10 (after C06)

**Changes**:
- Vendor: Infomap updated to 2.8.0 (14,959 lines in vendor/infomap/)
- Algorithm: Infomap C wrapper updated (1,709 lines in src/community/infomap/)
- New: `igraph_community_infomap()` regularization parameters
- Isolated vertices now supported

**R package impact**: LOW — mostly vendored code; R binding just needs the
new `is_regularized`/`regularization_strength` parameters.

---

### C10: Qhull vendor and spatial networks
**Lines**: ~34,700 · **Files**: ~40 · **Depends on**: C01
**Parallelism**: Can run in parallel with C09 (after C01)

**Changes**:
- Vendor: Qhull vendored (32,999 lines — all new files)
- New: `igraph_delaunay_graph()`, `igraph_gabriel_graph()`, `igraph_relative_neighborhood_graph()`
- New: `igraph_lune_beta_skeleton()`, `igraph_circle_beta_skeleton()`
- New: `igraph_beta_weighted_gabriel_graph()`
- New: `igraph_spatial_edge_lengths()`
- New: `igraph_nearest_neighbor_graph()`
- nanoflann updated to 1.9.0 (2,813 lines)

**R package impact**: LOW — all new functions, no existing bindings affected.
Downstream just needs to add new R wrappers.

---

### C11: Documentation, tests, examples, finalization
**Lines**: ~28,400 · **Files**: ~700+ · **Depends on**: ALL previous commits

**Changes**:
- Test updates across all changed functions (~13,530 lines in tests/)
- Example updates (~2,860 lines in examples/)
- Documentation reorganization (~552 lines in doc/)
- Fuzzing updates (~332 lines)
- `interfaces/functions.yaml` updates (~1,007 lines)
- `igraph_motifs_handler_t` const parameter
- Finalized experimental functions (35 functions)
- VERSIONING.md (58 L)
- Sampling uniformity test tool (111 L)
- Build system tweaks (CMakeLists.txt changes)

**R package impact**: LOW — mostly test/doc/build; `functions.yaml` is
machine-consumed.

---

## Parallelism matrix

```
Phase 1:  C01 ─────────────────────────────────►
Phase 2:  C02 ──────► C03 ──────► C04 ─────────►  (all 3 parallel)
Phase 3:  C05 ──────────────────────────────────►
Phase 4:  C06 ──────► C07 ──────► C08 ─────────►  (all 3 parallel)
Phase 5:  C09 ──────► C10 ─────────────────────►  (both parallel)
Phase 6:  C11 ─────────────────────────────────►
```

**Maximum parallelism**: 3 concurrent streams in phases 2 and 4.

## Estimated timeline

| Phase | Commits | Lines   | Calendar time (est.) | Notes                             |
|-------|---------|---------|----------------------|-----------------------------------|
| 1     | C01     | 8,200   | 2-3 days             | Foundation; needs careful testing  |
| 2     | C02-C04 | 17,500  | 3-5 days (parallel)  | 3 streams; longest is C02         |
| 3     | C05     | 2,800   | 1-2 days             | Path API redesign                 |
| 4     | C06-C08 | 11,100  | 3-4 days (parallel)  | 3 streams; longest is C06         |
| 5     | C09-C10 | 51,400  | 2-3 days (parallel)  | Mostly vendor drops, fast         |
| 6     | C11     | 28,400  | 3-4 days             | Tests/docs for all prior commits  |
| **Total** |     | 119,400 | **14-21 days**       | With full parallelism             |

## R package downstream work estimate

| Priority | Commit(s) | R functions affected | Effort    |
|----------|-----------|---------------------|-----------|
| 1 (do first) | C01  | All C bindings      | 3-5 days  |
| 2        | C02       | Attribute handler, vector API | 2-3 days |
| 3        | C03       | Permutation, loops_t, neighbors | 2-3 days |
| 4        | C04       | 24 removed function bindings | 1-2 days |
| 5        | C05       | Distance/path functions | 1-2 days |
| 6        | C06       | Centrality + community | 2-3 days |
| 7        | C07       | Game generators     | 1-2 days  |
| 8        | C08       | Cliques, iso, layout, misc | 1-2 days |
| 9        | C09       | Infomap (2 new params) | 0.5 days |
| 10       | C10       | New spatial wrappers | 1-2 days  |
| 11       | C11       | tests/docs only     | 0.5 days  |
| **Total** |          |                     | **15-25 days** |

## Risks and mitigations

1. **Cross-cutting header changes**: `include/igraph.h` and sub-headers touch
   multiple commits. Mitigation: C01 handles the header infrastructure; later
   commits only add/modify individual function declarations.

2. **Test interdependencies**: A test file may exercise functions from multiple
   commits. Mitigation: C11 handles test updates; intermediate commits may
   have some test failures that are resolved in C11.

3. **Interface file conflicts**: `interfaces/functions.yaml` is a single file
   changed by multiple logical units. Mitigation: Changes are additive/removal
   per function, so conflicts should be resolvable mechanically.

4. **Vendor drops are large but low-risk**: Qhull (33K lines) and Infomap
   (15K lines) are wholesale directory additions/replacements. They don't
   interact with other changes and can be trivially verified.
