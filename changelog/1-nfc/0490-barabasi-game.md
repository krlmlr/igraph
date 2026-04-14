# igraph_barabasi_game() and 3 others

**Category**: Graph generators

`igraph_barabasi_game()`, `igraph_barabasi_aging_game()`, `igraph_recent_degree_game()` and `igraph_recent_degree_aging_game()` no longer interprets an empty `outseq` vector as a missing out-degree sequence. Pass `NULL` if you don't wish to specify an out-degree sequence.

---

**Original changelog wording:**

> `igraph_barabasi_game()`, `igraph_barabasi_aging_game()`, `igraph_recent_degree_game()` and `igraph_recent_degree_aging_game()` no longer interprets an empty `outseq` vector as a missing out-degree sequence. Pass `NULL` if you don't wish to specify an out-degree sequence.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0490-barabasi-game.md
  12    22     1    11  src/games/barabasi.c
  13    17     1     7  src/games/recent_degree.c
```

Notes on remaining differences:
- `src/games/barabasi.c` (1 add, 11 del): file-mode/vim modeline headers (2 deletions), "IGraph library." → "igraph library." comment (1 del + 1 add), and 8 blank-line removals inside internal helper functions — all cosmetic NFC belonging to other changelog entries.
- `src/games/recent_degree.c` (1 add, 7 del): same pattern — modeline headers (2 del), copyright comment (1 del + 1 add), and 4 blank-line removals — cosmetic NFC for later entries.
- The test `tests/unit/igraph_barabasi_game.c` calls `igraph_is_simple` with a new third argument (`IGRAPH_DIRECTED`) on `next`, which requires a future `igraph_is_simple` API change; that test change was intentionally excluded.
