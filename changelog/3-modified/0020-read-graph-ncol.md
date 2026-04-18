# igraph_read_graph_ncol(), igraph_read_graph_lgl()

`igraph_read_graph_ncol()` and `igraph_read_graph_lgl()` now uses a default edge weight of 1 instead of 0 for files that do not contain edge weights for at least some of the edges.

---

**Original changelog wording:**

> `igraph_read_graph_ncol()` and `igraph_read_graph_lgl()` now uses a default edge weight of 1 instead of 0 for files that do not contain edge weights for at least some of the edges.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/3-modified/0020-read-graph-ncol.md
   3     3     2     2  src/io/ncol-parser.y
   3     3     2     2  src/io/lgl-parser.y
```

Notes on remaining differences:
- Parser files: 2 add / 2 del remaining are copyright header changes (IGraph → igraph)
