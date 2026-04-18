# igraph_minimum_spanning_tree()

`igraph_minimum_spanning_tree()` takes a new `method` parameter that controls the algorithm used for finding the spanning tree. Kruskal's algorithm was added.

---

**Original changelog wording:**

> `igraph_minimum_spanning_tree()` takes a new `method` parameter that controls the algorithm used for finding the spanning tree. Kruskal's algorithm was added.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0270-minimum-spanning-tree.md
 308   178   206   201  src/misc/spanning_trees.c
  19    41    16    39  include/igraph_structural.h
  70    48    70    64  include/igraph_constants.h
 319   349   319   349  interfaces/functions.yaml
  31    46    31    51  interfaces/types.yaml
   8     5     6     3  examples/simple/igraph_minimum_spanning_tree.c
   1     1     0     0  examples/simple/igraph_minimum_spanning_tree.out
  88     0     0     0  tests/unit/minimum_spanning_tree.c
  14     0     0     0  tests/unit/minimum_spanning_tree.out
  13    15    13    16  tests/CMakeLists.txt
```

Notes on remaining differences:
- `src/misc/spanning_trees.c`: Large reduction (308→206 add, 178→201 del). The remaining adds are NFC refactoring (const, reserve, bitset, igraph_incident 5→4 arg adaptations) and deprecated function removals not yet ported. The del increase (178→201) is because deprecated functions remain on main-dev but are removed on next.
- `include/igraph_constants.h`: del increase (48→64) because MST enum added on main-dev but next also has other NFC changes (IGRAPH_END_C_DECLS).
- `interfaces/types.yaml`: del increase (46→51) because MST_ALGORITHM type added but next has additional type renames.
- Tests/example: Fully ported (88→0, 14→0).
