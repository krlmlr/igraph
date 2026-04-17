# igraph_layout_sugiyama()

**Category**: Layouts

`igraph_layout_sugiyama()` does not return an "extended graph" anymore. The bends in the edges of the layout are encoded in a list of matrices instead; each item in the list belongs to an edge of the original graph and contains the control points of the edge in a row-wise fashion. The matrix will have no rows if no control points are needed on the edge.

---

**Original changelog wording:**

> `igraph_layout_sugiyama()` does not return an "extended graph" anymore. The bends in the edges of the layout are encoded in a list of matrices instead; each item in the list belongs to an edge of the original graph and contains the control points of the edge in a row-wise fashion. The matrix will have no rows if no control points are needed on the edge.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0    11     0  changelog/1-nfc/0780-layout-sugiyama.md
 114   129    14     8  src/layout/sugiyama.c
  13    19     9    15  include/igraph_layout.h
   3     6     1     3  src/layout/layout_bipartite.c
  81    29     0     0  tests/unit/igraph_layout_sugiyama.c
 169    87     0     0  tests/unit/igraph_layout_sugiyama.out
  67    31    39    27  tests/unit/test_utilities.c
  13     3     9     3  tests/unit/test_utilities.h
 382   367   381   365  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0780-layout-sugiyama.md`: 11 add / 0 del remains because the proof-of-work section is not on `next`.
- `src/layout/sugiyama.c`: Remaining 14 add / 8 del are unrelated changes (copyright header update, `feedback_arc_set.h` → `feedback_sets.h` rename, `igraph_incident`/`igraph_neighbors` extra parameters from later changelog entries).
- `include/igraph_layout.h`: Remaining 9 add / 15 del are cosmetic header changes (`__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS`, copyright, `IGRAPH_EXPERIMENTAL` on umap functions).
- `src/layout/layout_bipartite.c`: Remaining 1 add / 3 del are cosmetic changes (modeline removal, copyright header).
- `tests/unit/igraph_layout_sugiyama.c` and `.out`: Fully converged (0/0).
- `tests/unit/test_utilities.c`: Remaining 39 add / 27 del are other utility function changes unrelated to this entry (e.g., `edge_compare` signature change, `print_weighted_graph_canon`).
- `tests/unit/test_utilities.h`: Remaining 9 add / 3 del are other function declarations unrelated to this entry.
- `interfaces/functions.yaml`: Remaining 381 add / 365 del are from many other unrelated changes across the file (only the sugiyama entry and EDGEWEIGHTS→EDGE_WEIGHTS rename were relevant; the latter was left as-is since it belongs to a different entry).
