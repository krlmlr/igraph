# igraph_nearest_neighbor_graph()

`igraph_nearest_neighbor_graph()` computes a neighborhood graph of spatial points based on a neighbor count, cutoff distance, and chosen metric (experimental function). Thanks to Arnór Friðriksson @Zepeacedust for implementing this in #2788!

---

**Original changelog wording:**

> `igraph_nearest_neighbor_graph()` computes a neighborhood graph of spatial points based on a neighbor count, cutoff distance, and chosen metric (experimental function). Thanks to Arnór Friðriksson @Zepeacedust for implementing this in #2788!

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0080-nearest-neighbor-graph.md
```

Notes on remaining differences:
- The function was already ported in the spatial networks entry (2-added/0020). No additional code changes needed.
