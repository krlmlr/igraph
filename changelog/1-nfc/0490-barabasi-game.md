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
  12    22     1    10  src/games/barabasi.c
  13    17     1     5  src/games/recent_degree.c
```

Notes on remaining differences:
- `changelog/1-nfc/0490-barabasi-game.md`: After is 0/0 before adding the proof-of-work section; the section itself will increase the del count since `next` does not have it.
- `src/games/barabasi.c`: Remaining 1 add / 10 del are NFC changes (copyright header comment style `IGraph` → `igraph`, blank line removals) belonging to other changelog entries.
- `src/games/recent_degree.c`: Remaining 1 add / 5 del are NFC changes (copyright header comment style `IGraph` → `igraph`, blank line removals) belonging to other changelog entries.
