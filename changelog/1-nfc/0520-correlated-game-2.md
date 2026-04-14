# igraph_correlated_game(), igraph_correlated_pair_game(), igraph_permute_vertices()

**Category**: Graph generators

The semantics of the `permutation` argument of `igraph_correlated_game()` and `igraph_correlated_pair_game()` has changed: the i-th element of the vector now contains the index of the _original_ vertex that will be mapped to the i-th vertex in the new graph. This is consistent with how `igraph_permute_vertices()` operates (which has also changed in igraph 1.0).

---

**Original changelog wording:**

> The semantics of the `permutation` argument of `igraph_correlated_game()` and `igraph_correlated_pair_game()` has changed: the i-th element of the vector now contains the index of the _original_ vertex that will be mapped to the i-th vertex in the new graph. This is consistent with how `igraph_permute_vertices()` operates (which has also changed in igraph 1.0).

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0520-correlated-game-2.md
```

Notes on remaining differences:
- `changelog/1-nfc/0520-correlated-game-2.md` (0/0): The file was fully ported from `next`. The proof-of-work section added here is not present on `next`, so in a subsequent pass the `del` count would increase by the number of these added lines.
- The permutation semantics code change (`igraph_invert_permutation` in `src/games/correlated.c`) was already applied during the porting of entry 0510-correlated-game.md, as both changes were in the same file and were ported together. No additional code changes are needed for this entry.
