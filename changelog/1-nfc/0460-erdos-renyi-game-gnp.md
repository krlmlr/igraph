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
 273   235   152   209  src/games/erdos_renyi.c
  26    43    19    41  include/igraph_games.h
  52    35    50    33  src/games/correlated.c
 169    82     2     2  tests/unit/erdos_renyi_game_gnp.c
   2     3     1     2  tests/unit/igraph_layout_merge3.c
   7     6     6     5  tests/unit/igraph_maximal_cliques2.c
   3     3     1     1  tests/unit/percolation.c
   5     5     4     4  tests/unit/igraph_distances_floyd_warshall_speedup.c
   7     7     3     3  tests/unit/isoclasses2.c
   5     5     3     3  tests/unit/igraph_spanner.c
   8     6     7     5  tests/unit/igraph_maximal_cliques4.c
  11     3    10     2  tests/unit/igraph_correlated_game.c
   4     4     3     3  tests/unit/igraph_maximal_cliques3.c
   3     4     1     2  tests/unit/igraph_local_transitivity.c
  13    13     1     1  tests/benchmarks/erdos_renyi.c
   3     3     2     2  tests/benchmarks/modularity.c
 100   148   100   148  tests/benchmarks/igraph_distances.c
   3     3     1     1  tests/benchmarks/graphicality.c
   2     2     1     1  tests/benchmarks/igraph_layout_umap.c
   5     5     1     1  tests/benchmarks/igraph_voronoi.c
  22     3    20     0  examples/simple/igraph_erdos_renyi_game_gnp.c
  34    44    33    43  examples/simple/igraph_get_eids.c
   5     4     3     2  examples/simple/random_seed.c
  10     9     9     8  examples/simple/igraph_decompose.c
 451   439   447   438  interfaces/functions.yaml
```

Notes on remaining differences:

- `changelog/1-nfc/0460-erdos-renyi-game-gnp.md`: The `add-b=11` column reflects the proof-of-work section that was added to this file (which is not present on `next`).
- `src/games/erdos_renyi.c`: Remaining diff (152/209) reflects other changelog entries not yet ported, including `igraph_erdos_renyi_game()` deprecated function removal and other unrelated changes.
- `include/igraph_games.h`: Remaining diff reflects many other function signature changes (`igraph_rewire_edges`, `igraph_watts_strogatz_game`, `igraph_static_fitness_game`, etc.) belonging to future entries.
- `src/games/correlated.c`: Remaining diff (50/33) reflects the `igraph_correlated_game()` parameter order change (a separate changelog entry), plus NFC header changes.
- `tests/unit/igraph_correlated_game.c`: Remaining diff (10/2) reflects the parameter order change of `igraph_correlated_game()` call (separate changelog entry).
- `examples/simple/igraph_erdos_renyi_game_gnp.c`: The `add-a=20` reflects a copyright header and `igraph_setup()` call on `next` not yet ported.
- `interfaces/functions.yaml`: Remaining diff reflects many other function signature changes not yet ported.
- `tests/benchmarks/igraph_distances.c`: No change in numstat (100/148 both before and after) — this file has changes in `next` that are unrelated to `igraph_erdos_renyi_game_gnp` (other refactoring).
