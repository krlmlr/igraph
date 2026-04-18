# igraph_subgraph_edges(), igraph_subgraph_from_edges()

The deprecated `igraph_subgraph_edges()` was removed. Use `igraph_subgraph_from_edges()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_subgraph_edges()` was removed. Use `igraph_subgraph_from_edges()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0130-subgraph-edges.md
   5    20     5     6  src/operators/subgraph.c
  13    25    13    20  include/igraph_operators.h
```

Notes on remaining differences:
- `src/operators/subgraph.c`: del reduced 20→6. Remaining are copyright/comment header changes.
- `include/igraph_operators.h`: del reduced 25→20. Remaining are copyright/license header changes and `__BEGIN_DECLS`/`__END_DECLS` macro changes.
