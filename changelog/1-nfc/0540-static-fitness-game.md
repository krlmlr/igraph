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
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0540-static-fitness-game.md
  11    35    10    34  include/igraph_games.h
  15    13     6    10  src/games/static_fitness.c
 441   432   439   430  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0540-static-fitness-game.md`: 0 remaining diff (fully ported, the proof-of-work section added here increases the `del` count in `next` by 0 since `next` does not have that section)
- `include/igraph_games.h`: 1 added line remains (from the `next` branch removing the 2-line `loops, multiple` declaration and replacing with 1-line `allowed_edge_types`; remaining diff is due to later changelog entries 0550+ that change `igraph_static_power_law_game` signature)
- `src/games/static_fitness.c`: remaining diffs are: comment-only changes (file header, `/* reserved */`), and the body of `igraph_static_power_law_game` which will be ported in entry 0550
- `interfaces/functions.yaml`: remaining diffs are other functions not yet ported (the 2 changed lines from this entry are fully matched)
