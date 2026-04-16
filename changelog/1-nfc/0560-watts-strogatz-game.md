# igraph_watts_strogatz_game()

**Category**: Graph generators

`igraph_watts_strogatz_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and `multiple`.

---

**Original changelog wording:**

> `igraph_watts_strogatz_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and `multiple`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0560-watts-strogatz-game.md
  11    34     9    32  include/igraph_games.h
   9    10     1     3  src/games/watts_strogatz.c
   6     6     2     2  tests/unit/watts_strogatz_game.c
 437   430   436   429  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0560-watts-strogatz-game.md`: Fully ported, no remaining diff (0/0). The file no longer appears in the diff.
- `include/igraph_games.h`: Remaining 9 add / 32 del are unrelated changes (copyright header updates, include reordering, `__BEGIN_DECLS` -> `IGRAPH_BEGIN_C_DECLS`, whitespace, and other function signatures from later entries).
- `src/games/watts_strogatz.c`: Remaining 1 add / 3 del are copyright/vim modeline header changes belonging to later entries.
- `tests/unit/watts_strogatz_game.c`: Remaining 2 add / 2 del are the `igraph_is_simple()` 3-arg API change (a different changelog entry).
- `interfaces/functions.yaml`: Remaining 436 add / 429 del are changes for other functions across many other entries.
