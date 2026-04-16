# igraph_degree_sequence_game()

**Category**: Graph generators

`igraph_degree_sequence_game()` no longer interprets an empty in-degree vector as a request for generating undirected graphs. To generate undirected graphs, pass `NULL` for in-degrees.

---

**Original changelog wording:**

> `igraph_degree_sequence_game()` no longer interprets an empty in-degree vector as a request for generating undirected graphs. To generate undirected graphs, pass `NULL` for in-degrees.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0440-degree-sequence-game.md
  21    44     5    21  src/games/degree_sequence.c
  16    15    10    10  tests/unit/igraph_degree_sequence_game.c
```

Notes on remaining differences:
- `changelog/1-nfc/0440-degree-sequence-game.md`: Went from 11 add / 0 del to 0/0 because the file now exists on main-dev. The after numstat shows 0/0 because the proof-of-work section added to main-dev doesn't exist on next, causing the del count to stay at 0 while add drops to 0.
- `src/games/degree_sequence.c`: Decreased from 21 add / 44 del to 5 add / 21 del. The remaining diff contains cosmetic changes (blank line removals, comment removals, `igraph_rewire` signature change) that belong to later changelog entries.
- `tests/unit/igraph_degree_sequence_game.c`: Decreased from 16 add / 15 del to 10 add / 10 del. The remaining diff contains `igraph_is_simple()` and `igraph_erdos_renyi_game_gnm()` signature changes that belong to later changelog entries.
