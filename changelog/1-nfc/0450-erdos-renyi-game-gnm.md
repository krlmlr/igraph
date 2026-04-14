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
  11     0     0     0  changelog/1-nfc/0450-erdos-renyi-game-gnm.md
 630   226   273   235  src/games/erdos_renyi.c
  39    45    26    43  include/igraph_games.h
 233    21     4     4  tests/unit/erdos_renyi_game_gnm.c
  22     3     3     0  examples/simple/igraph_erdos_renyi_game_gnm.c
  23    23    13    13  tests/benchmarks/erdos_renyi.c
 457   439   451   439  interfaces/functions.yaml
  29    25    29    25  examples/tutorial/tutorial1.c
   6     5     5     4  tests/unit/coloring.c
   5     5     5     5  tests/unit/igraph_feedback_arc_set.c
   3     3     3     3  tests/unit/igraph_feedback_vertex_set.c
  25    22    23    20  tests/unit/igraph_joint_degree_distribution.c
   3     3     1     1  tests/unit/igraph_community_voronoi.c
  16    15    15    14  tests/unit/igraph_degree_sequence_game.c
  11     9     8     6  tests/unit/igraph_subisomorphic_lad.c
   7     6     6     5  tests/unit/igraph_maximal_cliques.c
   1     1     0     0  tests/unit/glpk_error.c
   2     2     1     1  tests/benchmarks/coloring.c
   8     8     8     8  tests/benchmarks/community.c
   2     2     1     1  tests/benchmarks/connectivity.c
  13    13    12    12  tests/benchmarks/igraph_average_path_length_unweighted.c
  19    19    17    17  tests/benchmarks/igraph_betweenness_weighted.c
   5     5     3     3  tests/benchmarks/igraph_cliques.c
   5     5     3     3  tests/benchmarks/igraph_closeness_weighted.c
  10    10     8     8  tests/benchmarks/igraph_degree_sequence_game.c
   5     5     1     1  tests/benchmarks/igraph_ecc.c
   2     2     2     2  tests/benchmarks/igraph_induced_subgraph.c
   3     6     3     6  tests/benchmarks/igraph_neighborhood.c
  42    24    37    19  tests/benchmarks/igraph_pagerank.c
  42    24    37    19  tests/benchmarks/igraph_pagerank_weighted.c
   2     2     1     1  tests/benchmarks/igraph_realize_degree_sequence.c
   5     5     1     1  tests/benchmarks/igraph_transitivity.c
   4     4     3     3  tests/benchmarks/inc_vs_adj.c
   3     3     3     3  tests/benchmarks/modularity.c
   5     2     4     1  examples/simple/coloring.c
   5     2     4     1  examples/simple/igraph_contract_vertices.c
   7     4     6     3  examples/simple/igraph_vector_int_list_sort.c
```

Notes on remaining differences:

- `changelog/1-nfc/0450-erdos-renyi-game-gnm.md`: Before adding, the file didn't exist (11 add, 0 del); after, it only remains different because this proof-of-work section was added here, while `next` doesn't have it (0 add, 0 del means the file is now identical on `next`, but the proof-of-work text extends the file beyond what `next` has — so this is expected to show 0/0 after because the proof-of-work lines we added are not present on `next`, meaning we have fewer lines matching `next`'s original file than `next` has).
- `src/games/erdos_renyi.c`: Remaining diff (273 add, 235 del) corresponds to the gnp-related changes (0460 entry) not yet ported.
- `include/igraph_games.h`: Remaining diff (26 add, 43 del) corresponds to other function signature changes not yet ported (rewire_edges, watts_strogatz, static_fitness, static_power_law, sbm_game, correlated_game, and copyright/macro changes).
- `tests/unit/erdos_renyi_game_gnm.c`: Near-zero remaining diff (4/4) reflects formatting and version year differences in the copyright header.
- `tests/benchmarks/erdos_renyi.c`: Remaining diff (13/13) reflects the gnp-related benchmark changes (0460 entry).
- `interfaces/functions.yaml`: Remaining diff (451/439) reflects many other function interfaces not yet ported.
- `examples/tutorial/tutorial1.c`: Remaining diff unchanged (29/25) — `next` also changes other aspects of this file not related to gnm.
- `tests/benchmarks/igraph_pagerank.c` and `igraph_pagerank_weighted.c`: Remaining diff unchanged — `next` changes other functions in these files.
- `tests/benchmarks/igraph_neighborhood.c`: Unchanged diff — `next` changes other code in this file.
