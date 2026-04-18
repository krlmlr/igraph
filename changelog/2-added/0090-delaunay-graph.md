# igraph_delaunay_graph()

`igraph_delaunay_graph()` computes a Delaunay graph of a spatial point set (experimental function). Thanks to Arnór Friðriksson @Zepeacedust for implementing this in #2806!

---

**Original changelog wording:**

> `igraph_delaunay_graph()` computes a Delaunay graph of a spatial point set (experimental function). Thanks to Arnór Friðriksson @Zepeacedust for implementing this in #2806!

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0090-delaunay-graph.md
```

Notes on remaining differences:
- The function was already ported in the spatial networks entry (2-added/0020). No additional code changes needed.
