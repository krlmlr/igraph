# igraph_erdos_renyi_game_gnm(), igraph_iea_game()

**Category**: Graph generators

`igraph_erdos_renyi_game_gnm()` uses a `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `igraph_bool_t loops`, and can now uniformly sample not only simple graphs but also multigraphs. It also gained an `edge_labeled` Boolean parameter which controls whether to sample from the set of ordered edge lists (equivalent to `igraph_iea_game()` for multigraphs).

---

**Original changelog wording:**

> `igraph_erdos_renyi_game_gnm()` uses a `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `igraph_bool_t loops`, and can now uniformly sample not only simple graphs but also multigraphs. It also gained an `edge_labeled` Boolean parameter which controls whether to sample from the set of ordered edge lists (equivalent to `igraph_iea_game()` for multigraphs).

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   11      0      -      -  changelog/1-nfc/0450-erdos-renyi-game-gnm.md
    5      2      4      1  examples/simple/coloring.c
    5      2      4      1  examples/simple/igraph_contract_vertices.c
   22      3     20      0  examples/simple/igraph_erdos_renyi_game_gnm.c
    7      4      6      3  examples/simple/igraph_vector_int_list_sort.c
   29     25     29     25  examples/tutorial/tutorial1.c
   39     45     28     44  include/igraph_games.h
  456    438    451    441  interfaces/functions.yaml
  630    226    300    246  src/games/erdos_renyi.c
    2      2      1      1  tests/benchmarks/coloring.c
    8      8      8      8  tests/benchmarks/community.c
    2      2      1      1  tests/benchmarks/connectivity.c
   23     23     18     18  tests/benchmarks/erdos_renyi.c
   13     13     12     12  tests/benchmarks/igraph_average_path_length_unweighted.c
   19     19     17     17  tests/benchmarks/igraph_betweenness_weighted.c
    5      5      3      3  tests/benchmarks/igraph_cliques.c
    5      5      3      3  tests/benchmarks/igraph_closeness_weighted.c
   10     10      8      8  tests/benchmarks/igraph_degree_sequence_game.c
    5      5      1      1  tests/benchmarks/igraph_ecc.c
    2      2      1      1  tests/benchmarks/igraph_induced_subgraph.c
    3      6      2      5  tests/benchmarks/igraph_neighborhood.c
   42     24     37     19  tests/benchmarks/igraph_pagerank.c
   42     24     37     19  tests/benchmarks/igraph_pagerank_weighted.c
    2      2      1      1  tests/benchmarks/igraph_realize_degree_sequence.c
    5      5      1      1  tests/benchmarks/igraph_transitivity.c
    4      4      3      3  tests/benchmarks/inc_vs_adj.c
    3      3      3      3  tests/benchmarks/modularity.c
    6      5      5      4  tests/unit/coloring.c
  233     21      5      5  tests/unit/erdos_renyi_game_gnm.c
    1      1      -      -  tests/unit/glpk_error.c
    3      3      1      1  tests/unit/igraph_community_voronoi.c
   10     10      9      9  tests/unit/igraph_degree_sequence_game.c
    5      5      5      5  tests/unit/igraph_feedback_arc_set.c
    3      3      3      3  tests/unit/igraph_feedback_vertex_set.c
   25     22     23     20  tests/unit/igraph_joint_degree_distribution.c
    7      6      6      5  tests/unit/igraph_maximal_cliques.c
   11      9      8      6  tests/unit/igraph_subisomorphic_lad.c
```

Notes on remaining differences:
- `changelog/1-nfc/0450-erdos-renyi-game-gnm.md`: Fully ported (dash means no remaining diff). Will increase after adding this proof-of-work section since `next` lacks it.
- `src/games/erdos_renyi.c`: add 630→300 (large reduction). Remaining 300 adds are mostly the gnp changes (entry 0460) and the section documentation rewrite. The del increase (226→246) is because the old gnm code was replaced with gnm_simple/gnm_multi/iea_game which are now closer to next's version, but the gnp code still uses `floor()` instead of `trunc()` and lacks the `multiple` parameter.
- `include/igraph_games.h`: add 39→28 (gnm and iea_game declarations ported). Remaining diffs are gnp signature change (entry 0460), other function signature changes, and copyright/macro changes.
- `tests/unit/erdos_renyi_game_gnm.c`: add 233→5, del 21→5 (nearly fully converged). Remaining 5 add/del are the `igraph_is_simple` 3-arg calls (a separate entry) vs 2-arg on main-dev.
- `tests/unit/glpk_error.c`: Fully converged (dash means no remaining diff for gnm).
- `tests/benchmarks/community.c`: 8/8→8/8 (unchanged — these are `false`/`false` calls which mapped to `IGRAPH_SIMPLE_SW, IGRAPH_EDGE_UNLABELED`, but the remaining diff is from other unrelated changes in the file).
- `tests/benchmarks/erdos_renyi.c`: add 23→18, del 23→18 (gnm callers updated, remaining diffs are gnp callers from entry 0460).
- `interfaces/functions.yaml`: add 456→451, del 438→441 (gnm + iea_game entries added, remaining diffs are gnp and other function changes).
- Most benchmark and test files: reduced by 1-2 add/del each, representing the mechanical gnm caller update. Remaining diffs are from other function changes (gnp, etc.) not yet ported.
- `examples/tutorial/tutorial1.c`: 29/25→29/25 (unchanged — this file has `igraph_setup()` and other non-gnm changes).
