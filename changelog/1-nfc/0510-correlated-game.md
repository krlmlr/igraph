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
  50    33     2     4  src/games/correlated.c
  12    36    11    35  include/igraph_games.h
 442   433   441   432  interfaces/functions.yaml
  10     2     0     0  tests/unit/igraph_correlated_game.c
```

Notes on remaining differences:
- `src/games/correlated.c` (2/4): The remaining diff is (a) the `igraph_is_simple` call gaining an `IGRAPH_DIRECTED` argument (part of a later changelog entry adding a `directed` parameter to `igraph_is_simple`), and (b) the file header comment changes (removal of vim/emacs modelines, "IGraph library." → "igraph library.") — both from other entries.
- `include/igraph_games.h` (11/35): The remaining differences are from other changelog entries (other function signature changes and removals in this header).
- `interfaces/functions.yaml` (441/432): The remaining differences are from other changelog entries (many other function changes in this file).
- `changelog/1-nfc/0510-correlated-game.md` (0/0): The file was fully ported; the proof-of-work section added here is not present on `next`, so the `del-a` count will increase by the number of these added lines in the next pass.
