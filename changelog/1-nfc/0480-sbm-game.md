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
  18    40    12    36  include/igraph_games.h
  69    19     0     0  tests/unit/igraph_sbm_game.c
   0     1     0     0  tests/unit/igraph_sbm_game.out
   1     1     0     0  tests/unit/igraph_hsbm_game.c
   1     1     0     0  tests/unit/igraph_hsbm_list_game.c
 445   436   443   434  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0480-sbm-game.md`: Zero diff after porting; `del` increase (11→0 add, 0→0 del) — this file was added from `next`, so before it had 11 added lines (to port), now there are 0 remaining lines to add from `next`. The proof-of-work section added here increases `del` when comparing `main-dev` to `next` (since `next` doesn't have it), but that's expected.
- `src/games/sbm.c`: Fully ported; 0 remaining diff to `next`.
- `include/igraph_games.h`: Remaining diff (12 add, 36 del) corresponds to other unported changes (e.g., `igraph_correlated_game` parameter reordering in a later changelog entry).
- `tests/unit/igraph_sbm_game.c` and `.out`: Fully ported; 0 remaining diff.
- `tests/unit/igraph_hsbm_game.c` and `igraph_hsbm_list_game.c`: Fully ported; 0 remaining diff.
- `interfaces/functions.yaml`: Remaining diff (443 add, 434 del) reflects other unported function signature changes in later changelog entries.
