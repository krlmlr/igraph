# igraph_beta_weighted_gabriel_graph()

`igraph_beta_weighted_gabriel_graph()` computes a Gabriel graph of a spatial point set, along with a threshold β value for each edge, at which the edge ceases to be part of the lune-based β-skeleton (experimental function). Thanks to Arnór Friðriksson @Zepeacedust for implementing this in #2827!

---

**Original changelog wording:**

> `igraph_beta_weighted_gabriel_graph()` computes a Gabriel graph of a spatial point set, along with a threshold β value for each edge, at which the edge ceases to be part of the lune-based β-skeleton (experimental function). Thanks to Arnór Friðriksson @Zepeacedust for implementing this in #2827!

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0130-beta-weighted-gabriel-graph.md
```

Notes on remaining differences:
- The function was already ported in the spatial networks entry (2-added/0020).
