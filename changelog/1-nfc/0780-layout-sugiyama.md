# igraph_layout_sugiyama()

**Category**: Layouts

`igraph_layout_sugiyama()` does not return an "extended graph" anymore. The bends in the edges of the layout are encoded in a list of matrices instead; each item in the list belongs to an edge of the original graph and contains the control points of the edge in a row-wise fashion. The matrix will have no rows if no control points are needed on the edge.

---

**Original changelog wording:**

> `igraph_layout_sugiyama()` does not return an "extended graph" anymore. The bends in the edges of the layout are encoded in a list of matrices instead; each item in the list belongs to an edge of the original graph and contains the control points of the edge in a row-wise fashion. The matrix will have no rows if no control points are needed on the edge.
