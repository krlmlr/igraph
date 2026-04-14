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
 490   392   335   318  src/misc/bipartite.c
  85    44     0     0  tests/unit/igraph_bipartite_game.c
 460   441   457   439  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0430-bipartite-game-gnp.md`: Fully matched after porting; the proof-of-work section appended here does not exist on `next`, so add-a=del-a=0 reflects a perfect content match before the proof-of-work lines.
- `include/igraph_bipartite.h`: Remaining 25 added / 37 deleted come from removal of deprecated declarations (`igraph_incidence`, `igraph_get_incidence`, `igraph_bipartite_game`) belonging to other changelog entries.
- `src/misc/bipartite.c`: Remaining 335 added / 318 deleted include removal of `igraph_incidence` function, doc changes to `igraph_biadjacency`, and other changes belonging to later entries.
- `tests/unit/igraph_bipartite_game.c`: Fully matched — diff goes to zero.
- `interfaces/functions.yaml`: Tiny decrease; remaining 457/439 are unrelated function changes throughout the file.
