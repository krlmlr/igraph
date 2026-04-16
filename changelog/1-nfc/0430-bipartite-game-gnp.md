# igraph_bipartite_game_gnp()

**Category**: Graph generators

`igraph_bipartite_game_gnp()` gained an `igraph_edge_type_sw_t allowed_edge_types` parameter, and can now sample multigraphs from a maximum entropy model with a prescribed _expected_ edge multiplicity. It also gained an `edge_labeled` Boolean parameter which controls whether to sample from the set of ordered edge lists.

---

**Original changelog wording:**

> `igraph_bipartite_game_gnp()` gained an `igraph_edge_type_sw_t allowed_edge_types` parameter, and can now sample multigraphs from a maximum entropy model with a prescribed _expected_ edge multiplicity. It also gained an `edge_labeled` Boolean parameter which controls whether to sample from the set of ordered edge lists.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0430-bipartite-game-gnp.md
  32    41    25    37  include/igraph_bipartite.h
 463   365   475   465  src/misc/bipartite.c
  83    39     0     0  tests/unit/igraph_bipartite_game.c
 459   440   456   438  interfaces/functions.yaml
```

Notes on remaining differences:
- **changelog file**: Fully ported (11→0 additions). The proof-of-work section adds deletions since `next` doesn't have it.
- **igraph_bipartite.h**: Decreased on both sides. Remaining diff is from other changelog entries (copyright header, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, removal of deprecated functions, `igraph_biadjacency`/`igraph_get_biadjacency` signature changes, `igraph_weighted_biadjacency`).
- **bipartite.c**: Small increase (+12 add, +100 del) because `bipartite_gnp_edge_labeled` is placed before `igraph_bipartite_game_gnp` with a forward declaration of `bipartite_iea_game`, whereas on `next` it's placed after `bipartite_iea_game` (which precedes `igraph_bipartite_game_gnp` on `next`). The function ordering on `main-dev` differs from `next`. Remaining diff includes many other unrelated changes.
- **tests**: Fully ported (83+39→0+0).
- **functions.yaml**: Slightly decreased. Remaining diff includes other function entries.
