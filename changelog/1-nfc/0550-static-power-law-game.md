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
  11     0     0     0  changelog/1-nfc/0550-static-power-law-game.md
```

Notes on remaining differences:
- `changelog/1-nfc/0550-static-power-law-game.md`: Fully ported (11→0 add). The code change for `igraph_static_power_law_game()` was already ported as part of the `0540-static-fitness-game` entry, since both functions share the same source file (`src/games/static_fitness.c`) and were changed together. Only the changelog file itself needed to be added.
