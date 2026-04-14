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
```

Notes on remaining differences:
- `changelog/1-nfc/0440-degree-sequence-game.md`: The file now exists on `main-dev` but `next` does not have the proof-of-work section, hence the `del-a=0` (no remaining difference once the proof-of-work section is excluded from the count; the `add-b=11` lines are now present on `main-dev`).
- `src/games/degree_sequence.c` (+5/-21 remaining): The remaining diff consists of (1) the copyright header `IGraph library` → `igraph library` NFC change, (2) blank line removals throughout the static helper functions (`configuration`, `fast_heur_undirected`, `fast_heur_directed`, `configuration_simple_*`), (3) removal of `/* Start the RNG */`/`/* Finish the RNG */` placeholder comments and addition of `/* reserved */` annotations, and (4) the `igraph_rewire()` API update (`IGRAPH_REWIRING_SIMPLE` → `IGRAPH_SIMPLE_SW, NULL`) which belongs to entry `0470-rewire-edges.md`.
