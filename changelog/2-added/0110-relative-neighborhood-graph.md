# igraph_relative_neighborhood_graph()

`igraph_relative_neighborhood_graph()` computes the relative neighborhood graph of a spatial point set (experimental function). Thanks to Arnór Friðriksson @Zepeacedust for implementing this in #2827!

---

**Original changelog wording:**

> `igraph_relative_neighborhood_graph()` computes the relative neighborhood graph of a spatial point set (experimental function). Thanks to Arnór Friðriksson @Zepeacedust for implementing this in #2827!

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0110-relative-neighborhood-graph.md
```

Notes on remaining differences:
- The function was already ported in the spatial networks entry (2-added/0020).
