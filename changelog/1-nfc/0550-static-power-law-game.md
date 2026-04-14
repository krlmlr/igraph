# igraph_static_power_law_game()

**Category**: Graph generators

`igraph_static_power_law_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and `multiple`.

---

**Original changelog wording:**

> `igraph_static_power_law_game()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and `multiple`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0550-static-power-law-game.md
  10    34     9    33  include/igraph_games.h
   6    10     1     3  src/games/static_fitness.c
  13    13     0     0  tests/unit/igraph_static_power_law_game.c
 439   430   438   429  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0550-static-power-law-game.md`: Fully resolved; file is identical to `next`. The proof-of-work section appended here does not appear on `next`, so in the final count `del-a=0` confirms no extra differences.
- `include/igraph_games.h`: Remaining 9 add / 33 del are from other changelog entries not yet ported (e.g., `IGRAPH_EXPERIMENTAL` on `igraph_chung_lu_game`, removal of `igraph_sample_sphere_surface`, and other unrelated API changes).
- `src/games/static_fitness.c`: Remaining 1 add / 3 del are minor NFC differences in the file unrelated to this entry.
- `tests/unit/igraph_static_power_law_game.c`: Fully resolved.
- `interfaces/functions.yaml`: Reduced by 1/1 for this entry. Remaining 438 add / 429 del are from other not-yet-ported changes in the interfaces file.
