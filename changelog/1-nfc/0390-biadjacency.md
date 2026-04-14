# igraph_biadjacency()

**Category**: Core graph manipulation

The order of edges in the graph returned by `igraph_(weighted_)adjacency()` and `igraph_biadjacency()` has changed. Note that these functions do not guarantee any specific edge order.

---

**Original changelog wording:**

> The order of edges in the graph returned by `igraph_(weighted_)adjacency()` and `igraph_biadjacency()` has changed. Note that these functions do not guarantee any specific edge order.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0390-biadjacency.md
 241   142     0     0  src/constructors/adjacency.c
 660   302   660   302  src/misc/bipartite.c
  67    31     0     0  tests/unit/test_utilities.c
  13     3     0     0  tests/unit/test_utilities.h
   7     7     0     0  tests/unit/igraph_adjacency.c
  19     4     0     0  tests/unit/igraph_adjacency.out
  13    22     0     0  tests/unit/igraph_weighted_adjacency.c
  85    92     0     0  tests/unit/igraph_weighted_adjacency.out
  37    22     0     0  examples/simple/igraph_weighted_adjacency.c
   5     5     0     0  examples/simple/igraph_weighted_adjacency.out
```

Notes on remaining differences:

- `src/misc/bipartite.c` still has 660 added / 302 deleted lines remaining vs `next`. Only the loop order change in `igraph_biadjacency()` was ported here (NFC: column-major instead of row-major iteration). The remaining diff corresponds to later changelog entries: removal of deprecated `igraph_incidence()` and `igraph_bipartite_game()` (`2-added/`, `3-modified/` entries), parameter rename from `input` to `biadjmatrix`, truncation vs rounding of non-integer entries, and other improvements.
- `changelog/1-nfc/0390-biadjacency.md` now has zero remaining diff because it was fully copied from `next`. The `del` column is 0 since `next` does not include the proof-of-work section added here (which increases the file on `main-dev` relative to `next`).
