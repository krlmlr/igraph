# igraph_bipartite_game_gnm(), igraph_bipartite_iea_game()

**Category**: Graph generators

`igraph_bipartite_game_gnm()` gained an `igraph_edge_type_sw_t allowed_edge_types` parameter, and can now uniformly sample not only simple graphs but also multigraphs. It also gained an `edge_labeled` Boolean parameter which controls whether to sample from the set of ordered edge lists (equivalent to `igraph_bipartite_iea_game()` for multigraphs).

---

**Original changelog wording:**

> `igraph_bipartite_game_gnm()` gained an `igraph_edge_type_sw_t allowed_edge_types` parameter, and can now uniformly sample not only simple graphs but also multigraphs. It also gained an `edge_labeled` Boolean parameter which controls whether to sample from the set of ordered edge lists (equivalent to `igraph_bipartite_iea_game()` for multigraphs).

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0420-bipartite-game-gnm.md
  45    45    32    41  include/igraph_bipartite.h
  95    50    95    51  include/igraph_constants.h
  12    11     3    11  include/igraph_decls.h
 472   444   464   445  interfaces/functions.yaml
 130     1   102     1  src/internal/utils.c
   8     1     6     1  src/internal/utils.h
 660   302   490   392  src/misc/bipartite.c
  24     6     3     4  src/misc/graphicality.c
  36     0     0     0  src/misc/graphicality.h
 265    86    85    44  tests/unit/igraph_bipartite_game.c
   7     6     6     5  tests/unit/coloring.c
   3     4     1     2  tests/unit/igraph_perfect.c
```

Notes on remaining differences:

- `include/igraph_bipartite.h`: Remaining diff (32 add, 41 del) is from other changelog entries not yet ported: new `igraph_weighted_biadjacency()`, updated `igraph_get_biadjacency()` signature, formatting changes, and copyright header updates.
- `include/igraph_constants.h`: Remaining diff (95 add, 51 del) is from other entries: many new type aliases, `IGRAPH_UNLIMITED` constant, and header modernization.
- `include/igraph_decls.h`: Remaining diff (3 add, 11 del) is from NFC header/license style updates in other entries.
- `interfaces/functions.yaml`: Remaining diff (464 add, 445 del) is from functions across many other changelog entries not yet ported.
- `src/internal/utils.c`: Remaining diff (102 add, 1 del) is from `igraph_i_simplify_edge_list()` and other functions added in later entries.
- `src/internal/utils.h`: Remaining diff (6 add, 1 del) is the `igraph_i_simplify_edge_list()` declaration for a later entry.
- `src/misc/bipartite.c`: Remaining diff (490 add, 392 del) is from other entries: `igraph_biadjacency()` refactoring, `igraph_bipartite_game_gnp()` new parameters, `igraph_weighted_biadjacency()`, `igraph_get_biadjacency()`, and other changes.
- `src/misc/graphicality.c`: Remaining diff (3 add, 4 del) is minor reformatting changes in other entries.
- `tests/unit/igraph_bipartite_game.c`: Remaining diff (85 add, 44 del) is from the `igraph_bipartite_game_gnp()` new parameters test (changelog entry 0430).
- `tests/unit/coloring.c` and `tests/unit/igraph_perfect.c`: Small remaining differences are from other NFC changes in those files.
