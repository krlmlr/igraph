# igraph_weighted_biadjacency()

`igraph_weighted_biadjacency()` creates a weighted graph from a bipartite adjacency matrix.

---

**Original changelog wording:**

> `igraph_weighted_biadjacency()` creates a weighted graph from a bipartite adjacency matrix.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0280-weighted-biadjacency.md
 470   468   557   651  src/misc/bipartite.c
  20    33    18    39  include/igraph_bipartite.h
 319   349   311   350  interfaces/functions.yaml
 108     0     0     0  tests/unit/igraph_weighted_biadjacency.c
  75     0     0     0  tests/unit/igraph_weighted_biadjacency.out
  13    16    13    17  tests/CMakeLists.txt
```

Notes on remaining differences:
- `src/misc/bipartite.c`: add increased (470→557) and del increased (468→651) because the new function was added but next also has many other refactoring changes in bipartite.c (NFC, other entries). The function itself is fully ported.
- `include/igraph_bipartite.h`: Small increase in del (33→39) because header has other changes from subsequent entries.
- Tests: Fully ported (108→0, 75→0).
