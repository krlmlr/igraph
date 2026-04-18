# igraph_correlated_game(), igraph_correlated_pair_game()

**Category**: Bug fixes

`igraph_correlated_game()` and `igraph_correlated_pair_game()` validate their `permutation` argument.

---

**Original changelog wording:**

> `igraph_correlated_game()` and `igraph_correlated_pair_game()` validate their `permutation` argument.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0890-correlated-game-3.md
```

Notes on remaining differences:
- `changelog/1-nfc/0890-correlated-game-3.md`: Fully ported (11→0 add). The file now exists on main-dev.
- No code changes were needed because the permutation validation in `igraph_correlated_game()` and `igraph_correlated_pair_game()` (length check and `igraph_invert_permutation()` call) was already present on `main-dev` from porting earlier entries (0510-correlated-game and 0520-correlated-game-2). This entry documents the validation behavior that was already in place.
