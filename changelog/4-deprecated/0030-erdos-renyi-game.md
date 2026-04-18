# igraph_erdos_renyi_game(), igraph_bipartite_game()

The deprecated `igraph_erdos_renyi_game()` and `igraph_bipartite_game()` were removed. Use the corresponding functions with `_gnm()` and `_gnp()` in the name instead.

---

**Original changelog wording:**

> The deprecated `igraph_erdos_renyi_game()` and `igraph_bipartite_game()` were removed. Use the corresponding functions with `_gnm()` and `_gnp()` in the name instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0030-erdos-renyi-game.md
 154   212   154   156  src/games/erdos_renyi.c
 557   651   557   586  src/misc/bipartite.c
   9    32     9    25  include/igraph_games.h
  18    39    18    31  include/igraph_bipartite.h
 304   340   304   335  interfaces/functions.yaml
```

Notes on remaining differences:
- `src/games/erdos_renyi.c`: del decreased (212→156), the deprecated function was removed. Remaining 154/156 are from other entries (copyright, NFC changes, other API modifications).
- `src/misc/bipartite.c`: del decreased (651→586), the deprecated function was removed. Remaining diffs are from other entries.
- `include/igraph_games.h`, `include/igraph_bipartite.h`: del decreased; remaining are from other entries (copyright, `__END_DECLS`, other deprecated function removals).
- `interfaces/functions.yaml`: del decreased by 5 (the bipartite_game entry).
- Changelog fully ported (0/0 after).
