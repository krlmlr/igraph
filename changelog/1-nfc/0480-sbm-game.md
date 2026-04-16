# igraph_sbm_game()

**Category**: Graph generators

`igraph_sbm_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `igraph_bool_t loops` and now supports generating graphs with multi-edges. The parameter determining the total number of vertices (`n`) was removed as it was redundant.

---

**Original changelog wording:**

> `igraph_sbm_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `igraph_bool_t loops` and now supports generating graphs with multi-edges. The parameter determining the total number of vertices (`n`) was removed as it was redundant.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0480-sbm-game.md
  71    60     0     0  src/games/sbm.c
  20    41    14    37  include/igraph_games.h
 445   438   443   436  interfaces/functions.yaml
  69    19     0     0  tests/unit/igraph_sbm_game.c
   0     1     0     0  tests/unit/igraph_sbm_game.out
```

Notes on remaining differences:
- `src/games/sbm.c`: Fully ported (0 add, 0 del remaining).
- `tests/unit/igraph_sbm_game.c`: Fully ported (0 add, 0 del remaining).
- `tests/unit/igraph_sbm_game.out`: Fully ported (0 add, 0 del remaining).
- `changelog/1-nfc/0480-sbm-game.md`: Fully ported (0 remaining); was 11 add before due to being a new file on next.
- `include/igraph_games.h`: Remaining diff (14 add, 37 del) is from other unported changes (header copyright, `__BEGIN_DECLS`/`IGRAPH_BEGIN_C_DECLS`, `igraph_watts_strogatz_game`, `igraph_static_fitness_game`, `igraph_static_power_law_game`, `igraph_chung_lu_game`, `igraph_correlated_game`, removal of deprecated functions, etc.).
- `interfaces/functions.yaml`: Remaining diff (443 add, 436 del) is from many other unported function interface changes (reduced by 2 add, 2 del from this change).
