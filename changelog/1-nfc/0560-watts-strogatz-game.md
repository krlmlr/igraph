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
   9    33     7    31  include/igraph_games.h
   9    10     1     3  src/games/watts_strogatz.c
   6     6     2     2  tests/unit/watts_strogatz_game.c
 438   429   437   428  interfaces/functions.yaml
```

Notes on remaining differences:
- `include/igraph_games.h`: 7+/31- remain due to other not-yet-ported changelog entries.
- `src/games/watts_strogatz.c`: 1+/3- remain: the `next` branch removes the `/* -*- mode: C -*- */` / `/* vim:... */` header lines and changes `IGraph` → `igraph` in the copyright, which belong to separate NFC entries.
- `tests/unit/watts_strogatz_game.c`: 2+/2- remain: `next` adds `IGRAPH_DIRECTED` as a third argument to `igraph_is_simple()`, which belongs to a later changelog entry for that function.
- `interfaces/functions.yaml`: 437+/428- remain; this large file has many other pending changes for other entries. The 1+/1- reduction reflects the watts_strogatz_game entry being ported.
