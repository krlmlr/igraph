# igraph_static_fitness_game()

**Category**: Graph generators

`igraph_static_fitness_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and `multiple`.

---

**Original changelog wording:**

> `igraph_static_fitness_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and `multiple`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
  11     0     0     0  changelog/1-nfc/0540-static-fitness-game.md
  15    13     3     5  src/games/static_fitness.c
  13    36    11    34  include/igraph_games.h
 440   433   437   430  interfaces/functions.yaml
  13    13     1     1  tests/unit/igraph_static_power_law_game.c
```

Notes on remaining differences:
- `changelog/1-nfc/0540-static-fitness-game.md`: Fully ported (11→0 add). The del-after stays 0 because `next` doesn't have the proof-of-work section.
- `src/games/static_fitness.c`: Reduced from 15/13 to 3/5. Remaining differences are cosmetic changes (header comment style, `/* reserved */` comments on push_back lines) that belong to other changelog entries.
- `include/igraph_games.h`: Reduced from 13/36 to 11/34. Remaining differences are unrelated changes (header boilerplate, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, `IGRAPH_EXPERIMENTAL` on `chung_lu_game`, removal of deprecated functions, etc.) belonging to other entries.
- `interfaces/functions.yaml`: Reduced from 440/433 to 437/430, reflecting the 3 lines changed for these two functions.
- `tests/unit/igraph_static_power_law_game.c`: Reduced from 13/13 to 1/1. The remaining 1/1 is the `IGraph`→`igraph` comment header change belonging to another entry.
