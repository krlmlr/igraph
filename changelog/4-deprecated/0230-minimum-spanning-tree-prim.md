# igraph_minimum_spanning_tree_prim(), igraph_minimum_spanning_tree(), igraph_subgraph_from_edges()

The deprecated `igraph_minimum_spanning_tree_prim()` was removed. Use `igraph_minimum_spanning_tree()` in conjunction with `igraph_subgraph_from_edges()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_minimum_spanning_tree_prim()` was removed. Use `igraph_minimum_spanning_tree()` in conjunction with `igraph_subgraph_from_edges()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  16     38    16     36  include/igraph_structural.h
 304    286   304    282  interfaces/functions.yaml
 204    199   204    133  src/misc/spanning_trees.c
```

Notes on remaining differences:
- `include/igraph_structural.h`: del reduced 38→36 (2 lines for declaration). Remaining diff (16 add, 36 del) is from other changelog entries (copyright/license header, `__BEGIN_DECLS`/`__END_DECLS` changes, removal of other deprecated functions, signature changes).
- `interfaces/functions.yaml`: del reduced 286→282 (4 lines for entry). Remaining diff is from many other changelog entries.
- `src/misc/spanning_trees.c`: del reduced 199→133 (66 lines: function body + doc comment + `\sa` reference line). Remaining diff (204 add, 133 del) is from other changelog entries (major restructuring of `igraph_minimum_spanning_tree` and related functions, removal of `igraph_minimum_spanning_tree_unweighted`, copyright/header changes, doc improvements).
