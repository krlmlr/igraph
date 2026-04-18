# igraph_transitive_closure_dag(), igraph_transitive_closure()

The deprecated `igraph_transitive_closure_dag()` was removed. Use `igraph_transitive_closure()` instead, which works for all graphs, not just DAGs.

---

**Original changelog wording:**

> The deprecated `igraph_transitive_closure_dag()` was removed. Use `igraph_transitive_closure()` instead, which works for all graphs, not just DAGs.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  13     31    13     29  include/igraph_isomorphism.h
 304    289   304    286  interfaces/functions.yaml
  15    116    15     21  src/properties/dag.c
```

Notes on remaining differences:
- `include/igraph_isomorphism.h`: del reduced 31→29 (2 lines for declaration). Remaining diff (13 add, 29 del) is from other changelog entries (copyright/license header, `__BEGIN_DECLS`/`__END_DECLS` changes, DAG section header + `igraph_topological_sorting`/`igraph_is_dag` move, function reorderings, typo fix).
- `interfaces/functions.yaml`: del reduced 289→286 (3 lines for entry). Remaining diff is from many other changelog entries affecting this file.
- `src/properties/dag.c`: del reduced 116→21 (95 lines: function body + unused includes). Remaining diff (15 add, 21 del) is from other changelog entries (copyright/comment header changes, `#include` change from `igraph_isomorphism.h` to `igraph_cycles.h`, `0`→`IGRAPH_NO_LOOPS`, `true`→`IGRAPH_LOOPS`, `false`→`\c false` doc change).
