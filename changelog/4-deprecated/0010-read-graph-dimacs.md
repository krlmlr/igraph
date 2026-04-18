# igraph_read_graph_dimacs() and 3 others

The deprecated `igraph_read_graph_dimacs()` and `igraph_write_graph_dimacs()` were removed. These names may be re-used in the future. Use `igraph_read_graph_dimacs_flow()` and `igraph_write_graph_dimacs_flow()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_read_graph_dimacs()` and `igraph_write_graph_dimacs()` were removed. These names may be re-used in the future. Use `igraph_read_graph_dimacs_flow()` and `igraph_write_graph_dimacs_flow()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0010-read-graph-dimacs.md
   1    32     1     2  src/io/dimacs.c
   5    20     5    10  include/igraph_foreign.h
```

Notes on remaining differences:
- `src/io/dimacs.c`: Remaining 1/2 is copyright header NFC change.
- `include/igraph_foreign.h`: Remaining 5/10 are NFC changes from other entries (copyright header, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, `IGRAPH_DEPRECATED` removal on other functions).
- Changelog fully ported (0/0 after).
