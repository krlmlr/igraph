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
  18    11     9    11  include/igraph_decls.h
 660   302   463   365  src/misc/bipartite.c
  24     6     3     4  src/misc/graphicality.c
  36     0     2     2  src/misc/graphicality.h
 130     1   102     1  src/internal/utils.c
   8     1     6     1  src/internal/utils.h
 467   439   459   440  interfaces/functions.yaml
   2     6     1     6  doc/bipartite.xxml
 265    86    83    39  tests/unit/igraph_bipartite_game.c
   7     6     6     5  tests/unit/coloring.c
   3     4     1     2  tests/unit/igraph_perfect.c
```

Notes on remaining differences:
- **changelog/1-nfc/0420-bipartite-game-gnm.md**: Reduced from 11/0 to 0/0 — the changelog file is now present on main-dev. The proof-of-work section adds deletions vs next (which doesn't have it), but this is expected.
- **include/igraph_bipartite.h**: Reduced from 45/45 to 32/41. The `igraph_bipartite_game_gnm` signature and `igraph_bipartite_iea_game` declaration are ported. Remaining diff is from `igraph_bipartite_game_gnp` signature changes (separate entry) and other unrelated header reformatting (deprecated functions removal, etc.).
- **include/igraph_constants.h**: Minimal change (50→51 del) — `IGRAPH_EDGE_UNLABELED`/`IGRAPH_EDGE_LABELED` added; remaining diff is from other entries.
- **include/igraph_decls.h**: Reduced from 18/11 to 9/11. `IGRAPH_EXPERIMENTAL` macro ported; remaining diff is `__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS` rename (separate entry).
- **src/misc/bipartite.c**: Significantly reduced from 660/302 to 463/365. The bipartite_gnm and iea_game functions are ported. Remaining diff includes `igraph_bipartite_game_gnp` changes (separate entry), attribute copy refactoring, and other unrelated changes.
- **src/misc/graphicality.c**: Reduced from 24/6 to 3/4. The `igraph_i_edge_type_to_loops_multiple` function and internal header inclusion are ported. Remaining diff is minor formatting.
- **src/misc/graphicality.h**: Reduced from 36/0 to 2/2. The internal header is now present. Remaining diff is `__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS` rename.
- **src/internal/utils.c**: Reduced from 130/1 to 102/1. The `igraph_i_vector_int_shuffle_pairs` function ported. Remaining diff includes `igraph_i_simplify_edge_list` and other functions from later entries.
- **src/internal/utils.h**: Reduced from 8/1 to 6/1. Declaration added; remaining diff is unrelated.
- **interfaces/functions.yaml**: Reduced from 467/439 to 459/440. `igraph_bipartite_game_gnm` and `igraph_bipartite_iea_game` entries ported. Remaining diff covers many other function changes.
- **doc/bipartite.xxml**: Reduced from 2/6 to 1/6. `igraph_bipartite_iea_game` doc reference added. Remaining deletions are from removing deprecated functions section (later entry).
- **tests/unit/igraph_bipartite_game.c**: Significantly reduced from 265/86 to 83/39. gnm and iea tests ported. Remaining diff is gnp test updates (separate entry).
- **tests/unit/coloring.c** and **tests/unit/igraph_perfect.c**: Small reductions — callers updated to new signature.
