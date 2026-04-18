# igraph_minimum_spanning_tree_unweighted(), igraph_minimum_spanning_tree(), igraph_subgraph_from_edges()

The deprecated `igraph_minimum_spanning_tree_unweighted()` was removed. Use `igraph_minimum_spanning_tree()` in conjunction with `igraph_subgraph_from_edges()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_minimum_spanning_tree_unweighted()` was removed. Use `igraph_minimum_spanning_tree()` in conjunction with `igraph_subgraph_from_edges()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  16     36    16     34  include/igraph_structural.h
 304    282   304    279  interfaces/functions.yaml
 204    133   209     85  src/misc/spanning_trees.c
```

Notes on remaining differences:
- `include/igraph_structural.h`: del reduced 36→34 (2 lines for declaration). Remaining diff is from other changelog entries.
- `interfaces/functions.yaml`: del reduced 282→279 (3 lines for entry). Remaining diff is from many other changelog entries.
- `src/misc/spanning_trees.c`: del reduced 133→85 (48 lines: function body + doc comment). add increased 204→209 because removing the `#include "igraph_operators.h"` line makes the diff baseline shift. Remaining diff (209 add, 85 del) is from other changelog entries (major restructuring of `igraph_minimum_spanning_tree`, copyright/header, doc improvements, code reformatting).
