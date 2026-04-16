# igraph_correlated_game()

**Category**: Graph generators

`igraph_correlated_game()` now takes the graph being constructed as the _first_ argument to remain consistent with other graph constructors. Earlier versions used to take the original graph as the first argument.

---

**Original changelog wording:**

> `igraph_correlated_game()` now takes the graph being constructed as the _first_ argument to remain consistent with other graph constructors. Earlier versions used to take the original graph as the first argument.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0510-correlated-game.md
  14    37    13    36  include/igraph_games.h
  50    33     2     4  src/games/correlated.c
  10     2     1     1  tests/unit/igraph_correlated_game.c
 442   435   441   434  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0510-correlated-game.md`: Fully ported (11→0 add). The file now exists on main-dev.
- `include/igraph_games.h`: Decreased by 1/1 (14→13 add, 37→36 del). Remaining diff is unrelated header/copyright changes and other function signature changes from later entries.
- `src/games/correlated.c`: Large decrease (50→2 add, 33→4 del). Remaining 2 add / 4 del are unrelated changes: header copyright/license reformatting and `igraph_is_simple()` gaining a third argument (from a later entry).
- `tests/unit/igraph_correlated_game.c`: Decreased (10→1 add, 2→1 del). Remaining diff is the copyright header change ("IGraph" → "igraph").
- `interfaces/functions.yaml`: Decreased by 1/1 (442→441 add, 435→434 del). Remaining diff is from other function changes in later entries.
