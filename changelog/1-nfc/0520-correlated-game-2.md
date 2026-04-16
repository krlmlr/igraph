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
   11      0      0      0  changelog/1-nfc/0520-correlated-game-2.md
```

Notes on remaining differences:
- `changelog/1-nfc/0520-correlated-game-2.md`: Fully ported (11→0 add). The file now exists on main-dev.
- No code changes were needed because the permutation semantics change in `igraph_correlated_game()` and `igraph_correlated_pair_game()` was already implicitly applied when porting earlier entries: 0370-permute-vertices (which changed `igraph_permute_vertices()` semantics) and 0510-correlated-game (which reordered arguments and adapted the permutation handling in `src/games/correlated.c`). This entry documents the semantic change that was already covered by those prior ports.
