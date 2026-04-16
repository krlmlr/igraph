# igraph_erdos_renyi_game_gnp()

**Category**: Graph generators

`igraph_erdos_renyi_game_gnp()` uses a `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `igraph_bool_t loops`, and can now sample multigraphs from a maximum entropy model with a prescribed _expected_ edge multiplicity. It also gained an `edge_labeled` Boolean parameter which controls whether to sample from the set of ordered edge lists.

---

**Original changelog wording:**

> `igraph_erdos_renyi_game_gnp()` uses a `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `igraph_bool_t loops`, and can now sample multigraphs from a maximum entropy model with a prescribed _expected_ edge multiplicity. It also gained an `edge_labeled` Boolean parameter which controls whether to sample from the set of ordered edge lists.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0460-erdos-renyi-game-gnp.md
 300   246   154   212  src/games/erdos_renyi.c
  28    44    21    42  include/igraph_games.h
 451   441   447   440  interfaces/functions.yaml
 169    82     4     7  tests/unit/erdos_renyi_game_gnp.c
  22     3    20     0  examples/simple/igraph_erdos_renyi_game_gnp.c
   5     4     3     2  examples/simple/random_seed.c
  34    44    33    43  examples/simple/igraph_get_eids.c
  10     9     9     8  examples/simple/igraph_decompose.c
  52    35    50    33  src/games/correlated.c
   3     3     3     3  tests/unit/percolation.c
   7     7     3     3  tests/unit/isoclasses2.c
   4     4     3     3  tests/unit/igraph_maximal_cliques3.c
   8     6     7     5  tests/unit/igraph_maximal_cliques4.c
   7     6     6     5  tests/unit/igraph_maximal_cliques2.c
  11     3    10     2  tests/unit/igraph_correlated_game.c
   5     5     4     4  tests/unit/igraph_distances_floyd_warshall_speedup.c
   2     3     1     2  tests/unit/igraph_layout_merge3.c
   5     5     3     3  tests/unit/igraph_spanner.c
   3     4     1     2  tests/unit/igraph_local_transitivity.c
  18    18     2     2  tests/benchmarks/erdos_renyi.c
   3     3     2     2  tests/benchmarks/modularity.c
   5     5     1     1  tests/benchmarks/igraph_voronoi.c
 100   148   100   148  tests/benchmarks/igraph_distances.c
   2     2     1     1  tests/benchmarks/igraph_layout_umap.c
   3     3     1     1  tests/benchmarks/graphicality.c
```

Notes on remaining differences:
- `changelog/1-nfc/0460-erdos-renyi-game-gnp.md`: 0/0 after (was 11/0 before) — fully ported, proof-of-work section adds deletions since `next` doesn't have it.
- `src/games/erdos_renyi.c`: Large decrease (300→154 add, 246→212 del). Remaining diff is due to other changelog entries (gnm move, deprecated function removal, other section doc changes).
- `include/igraph_games.h`: Decrease (28→21 add). Remaining diff is from other function signature changes in later changelog entries.
- `interfaces/functions.yaml`: Decrease (451→447 add). Remaining diff from many other function entries.
- `tests/unit/erdos_renyi_game_gnp.c`: Large decrease (169→4 add, 82→7 del). Nearly fully ported; small remaining diff is from `igraph_is_simple` 3-arg signature change in a later entry.
- `examples/simple/igraph_erdos_renyi_game_gnp.c`: Decrease (22→20 add). Remaining is license header and `igraph_setup()` call from a later entry.
- Other caller files show small decreases of 1-2 lines each, with remaining diffs from unrelated changes (copyright headers, other function signature changes, etc.).
- `tests/benchmarks/igraph_distances.c`: Unchanged (100/148) — no gnp-related changes in this file; the diff is entirely from other entries.
