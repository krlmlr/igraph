# Changelog Rewrite — Proof of Work

This document records the decisions and analysis behind the rewritten `CHANGELOG.md`.

## Decision Rules Applied

1. **NFC priority over Modified**: "Non-functional changes" takes priority over "Modified functionality." A change is listed under NFC if it does not alter graph algorithm behavior, even if it modifies function signatures, parameter types, or API conventions.

2. **Modified = algorithm behavior changes only**: Reserved for changes that alter how a graph algorithm computes its core results (different treatment of weights, different rounding, different output for the same input).

3. **Version merging**: 1.0.0 and 1.0.1 are treated as a single release. 1.0.1 regression/bug fixes are omitted.

4. **NFC dependency ordering**: Items arranged from foundational (build system) to high-level (documentation), following the dependency structure of the codebase.

## Items Dropped from 1.0.1

These are all regressions or bugs introduced in 1.0.0, so they are omitted in the merged changelog:

| Item | Rationale |
|------|-----------|
| Eliminated references to `exit()` from shared library (Qhull/Infomap) | Regression: accidentally introduced into 1.0.0 through Qhull and Infomap |
| Eliminated references to `std::cout` from shared library | Regression: introduced via Infomap update in 1.0.0 |
| Fixed `igraph_hub_and_authority_scores()` warning threshold bug | Regression: warning system was newly added in 1.0.0 |
| Fixed compilation/tests when Infomap support is disabled | Regression: Infomap was updated in 1.0.0 |
| Fixed Apple compilation issues with `_POSIX_C_SOURCE` | Regression: related to C++14 requirement introduced in 1.0.0 |
| Fixed inconsistent libf2c prototypes for `s_copy()`/`s_cat()` | Regression: broken compatibility introduced in 1.0.0 |
| "Documentation improvements" | Subsumed by 1.0.0's "Various documentation improvements" |

### Kept from 1.0.1

| Item | Rationale |
|------|-----------|
| nanoflann updated to version 1.9.0 | Not a regression; genuine vendor update |

## Items Moved from Modified to NFC

These items were previously in "Modified functionality" but moved to NFC because they don't change graph algorithm behavior. They modify function signatures, parameter types, or API conventions, but the underlying algorithms produce the same results (or old behavior is reproducible with specific parameter values).

### Build system and compiler (2 items)
- C++14 requirement → build infrastructure
- Single `<igraph.h>` header requirement → build infrastructure

### Core infrastructure (13 items)
- `igraph_setup()` recommendation → infrastructure
- Interruption handler `void *` removal → HLI interface change
- Interruption handler return type change → HLI interface change
- `igraph_status()` error code handling → infrastructure
- All error code changes (9 items) → error code infrastructure, not algorithms

### Random number generation (2 items)
- `igraph_rng_set_default()` changes → RNG infrastructure
- `RNG_BEGIN()`/`RNG_END()` removal → RNG infrastructure

### Core types and naming (2 items)
- `igraph_integer_t` → `igraph_int_t` rename → naming convention
- `igraph_multiple_t` removal → type simplification

### Core data structures (12 items)
- All `igraph_strvector_*`, `igraph_vector_*`, `igraph_matrix_*` API changes → data structure interface, not algorithms
- `igraph_vector_append()` allocation strategy → internal optimization
- `igraph_vector_difference_sorted()` multiset handling → utility function fix

### Attribute handling (5 items)
- All `igraph_attribute_*` changes → attribute infrastructure, not algorithms

### Core graph manipulation (7 items)
- `igraph_delete_vertices_map()` mapping → interface consistency
- `igraph_edges()` bycol argument → parameter addition, old behavior preserved
- `igraph_neighbors()`/`igraph_vs_adj()` new arguments → old behavior with `IGRAPH_LOOPS_TWICE`/`true`
- `igraph_incident()`/`igraph_es_incident()` new argument → old behavior with `IGRAPH_LOOPS_TWICE`
- Edge order changes in adjacency/biadjacency → implementation detail, no order guaranteed
- `igraph_permute_vertices()` semantics → convention change, same algorithm
- `igraph_canonical_permutation()` semantics inversion → consequence of above

### Basic graph properties (4 items)
- `igraph_density()` weights parameter → parameter addition
- `igraph_is_simple()` extra argument → parameter addition
- `igraph_loops_t` type changes → type refinement, old behavior preserved
- `igraph_get_biadjacency()` weights parameter → parameter addition

### Graph generators (17 items)
- All `igraph_edge_type_sw_t` parameter changes → parameter restructuring
- `igraph_lcf()` rename → naming
- `igraph_rewire()` parameter changes → API restructuring
- `igraph_correlated_game()` argument order and permutation semantics → convention alignment

### Paths and cycles (8 items)
- All `weights` parameter additions → parameter additions, auto-selection
- Parameter reorderings and consolidations → API consistency
- `max_results` additions → parameter additions

### Community detection (5 items)
- `igraph_community_infomap()` regularization → new optional parameters, default preserved
- `igraph_community_label_propagation()` variant → new parameter, old behavior with `DOMINANCE`
- `igraph_community_leiden()` directed support → new parameters, old behavior with `NULL`
- `igraph_community_leading_eigenvector()` history type → type change
- `igraph_community_optimal_modularity()` resolution → parameter addition/reorder

### Isomorphism functions (5 items)
- Automorphism function renames → naming
- `igraph_subisomorphic_lad()` CPU time removal → API cleanup
- `igraph_isoclass_subgraph()` type change → type change

### Centralities (6 items)
- Betweenness `normalized` parameter → parameter addition
- `igraph_edge_betweenness()` eids → parameter addition
- Eigenvector centrality `mode` parameter → parameter type change
- Scale parameter removals → post-processing normalization, not algorithm change
- PageRank ordering → parameter reordering

### Cliques and independent sets (4 items)
- `max_results`, `min_size`/`max_size` additions → parameter additions
- Parameter ordering standardizations → API consistency

### Layouts (1 item)
- `igraph_layout_sugiyama()` output format → output representation, not algorithm

### Other network analysis (5 items)
- `igraph_similarity_*` two vertex sets → parameter change, old behavior reproducible
- `igraph_minimum_spanning_tree()` method → parameter addition
- Motif function type changes → overflow prevention
- `igraph_motifs_handler_t` const → API cleanup
- `igraph_fundamental_cycles()`/`igraph_minimum_cycle_basis()` parameter changes → type/reorder

### Foreign formats (1 item)
- Pajek format `name` attribute → I/O convention, not algorithm

### Warnings and behavioral refinements (4 items)
- Eigenvector centrality zero warning → warning only, no result change
- Hub/authority scores zero warning → warning only, no result change
- Hub/authority scores undirected warning → warning only, falls back to equivalent computation
- `igraph_get_stochastic_sparse()` zero handling → error handling change, not algorithm

### Bug fixes (2 items)
- `igraph_community_spinglass_single()` `igraph_real_t` → precision fix, not algorithm change
- `igraph_correlated_game()` permutation validation → input validation

### Finalized experimental functions (1 item)
- Status change only, no algorithm change

### Documentation, performance, vendor (4 items)
- Documentation reorganization/improvements → documentation
- Adjacency matrix performance → optimization
- nanoflann 1.9.0 → vendor update

## Items Kept in Modified

These items remain in "Modified functionality" because they genuinely change graph algorithm behavior or output:

| Item | Rationale |
|------|-----------|
| `igraph_community_edge_betweenness()` weights/lengths + strong connections | Changes how the algorithm uses weights: weights now divide betweenness scores, lengths define shortest paths. Fundamentally changes algorithm behavior. |
| `igraph_adjacency()` LOOPS_TWICE treatment | Changes graph construction: LOOPS_TWICE treated as LOOPS_ONCE for directed/upper/lower modes. Same input, different graph output. |
| `igraph_biadjacency()` truncation vs rounding | Changes output: truncation instead of rounding up. Same input, different graph. |
| `igraph_minimum_size_separators()` complete graphs | Changes output: no longer returns separating sets for complete graphs. |
| `igraph_read_graph_ncol()`/`igraph_read_graph_lgl()` default weight | Changes output: default weight 1 instead of 0. Same file, different graph weights. |
| Infomap updated to 2.8.0 | Algorithm implementation change. Different community detection results possible. |

## Duplicate Resolution

`igraph_community_spinglass_single()` appeared in both the original NFC section (as a bug fix) and the Modified section (as a breaking change). These described the same change from two angles: API type change to `igraph_real_t` (NFC) and precision improvement (bug fix). Combined into a single NFC > Bug fixes entry.

`igraph_community_edge_betweenness()` appeared in both Breaking changes (API: new `weights`/`lengths` parameters) and Changed (behavior: strong connections). Merged into a single Modified entry since the API change enables the behavioral change.

## NFC Dependency Structure Rationale

The NFC section is ordered by dependency layer, from most foundational to most specialized:

1. **Build system and compiler** — Everything depends on these
2. **Core infrastructure** — Error codes, interruption, status used by all functions
3. **Random number generation** — Used by stochastic algorithms
4. **Core types and naming** — Type definitions used everywhere
5. **Core data structures** — Vectors, matrices used by all algorithms
6. **Attribute handling** — Builds on data structures
7. **Core graph manipulation** — Builds on data structures and attributes
8. **Basic graph properties** — Uses graph manipulation
9. **Graph generators** — Uses graph manipulation and RNG
10. **Paths and cycles** — Uses graph properties
11. **Community detection** — Uses paths and graph properties
12. **Isomorphism functions** — Uses graph manipulation
13. **Centralities** — Uses paths and graph properties
14. **Cliques and independent sets** — Uses graph properties
15. **Layouts** — Uses graph properties
16. **Other network analysis** — Uses graph properties
17. **Foreign formats** — I/O layer, uses graph manipulation and attributes
18. **Warnings and behavioral refinements** — Post-computation output
19. **Bug fixes** — Corrections to specific functions
20. **Finalized experimental functions** — Status metadata change
21. **Documentation, performance, vendor** — Non-code changes

This ordering mirrors the igraph/igraph upstream changelog's subsection structure (General changes → Error codes → Core data structures → ... → Foreign formats) and allows readers to understand foundational changes before encountering the API changes that build on them.

## Verification Counts

### Upstream igraph/igraph 1.0.0 section item counts:
- Breaking changes: ~96 items across 15 subsections
- Added: 16 items + 5 highlights
- Changed: 12 items
- Finalized: 1 item (listing ~33 functions)
- Fixed: 2 items
- Removed: ~37 items
- Deprecated: 1 item

### Upstream igraph/igraph 1.0.1 section item counts:
- Fixed: 6 items
- Other: 2 items

### Rewritten changelog section counts:
- NFC: ~103 items across 21 subsections (includes items moved from Modified + original NFC)
- Added: 16 items + 5 highlights (unchanged)
- Modified: 6 items (only algorithm-behavior-changing items)
- Deprecated and removed: ~38 items (unchanged)
- Dropped: 7 items (1.0.1 regressions/bugs from 1.0.0)
