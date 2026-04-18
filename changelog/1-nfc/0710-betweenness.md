# igraph_betweenness() and 5 others

**Category**: Centralities

All betweenness functions got a `normalized` parameter to support normalizing the result by the number of vertex pairs in the graph. At the same time, their parameter ordering was standardized. The following functions are affected: `igraph_betweenness()`, `igraph_betweenness_cutoff()`, `igraph_edge_betweenness()`, `igraph_edge_betweenness_cutoff()`, `igraph_betweenness_subset()`, `igraph_edge_betweenness_subset()`.

---

**Original changelog wording:**

> All betweenness functions got a `normalized` parameter to support normalizing the result by the number of vertex pairs in the graph. At the same time, their parameter ordering was standardized. The following functions are affected: `igraph_betweenness()`, `igraph_betweenness_cutoff()`, `igraph_edge_betweenness()`, `igraph_edge_betweenness_cutoff()`, `igraph_betweenness_subset()`, `igraph_edge_betweenness_subset()`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0    11     0  changelog/1-nfc/0710-betweenness.md
  94    91    57    71  include/igraph_centrality.h
 240   137     0     0  src/centrality/betweenness.c
  38    77    37    76  src/centrality/centralization.c
  34    35     0     0  tests/unit/igraph_betweenness.c
  99    17     0     0  tests/unit/igraph_edge_betweenness.c
  61    62     0     0  tests/unit/igraph_betweenness_subset.c
  56    58     0     0  tests/unit/igraph_edge_betweenness_subset.c
   1     1     0     0  tests/unit/igraph_community_voronoi.c
   2     2     1     1  tests/unit/igraph_voronoi.c
   1     1     0     0  tests/unit/igraph_community_optimal_modularity.c
  11    11     1     1  tests/benchmarks/igraph_betweenness.c
  17    17     1     1  tests/benchmarks/igraph_betweenness_weighted.c
  49    44    49    44  examples/tutorial/tutorial3.c
   9     6     8     5  examples/simple/igraph_minimum_spanning_tree.c
 409   389   400   380  interfaces/functions.yaml
   8     0     0     0  tests/unit/igraph_edge_betweenness.out
```

Notes on remaining differences:
- `changelog/1-nfc/0710-betweenness.md`: 11 add-after is this proof-of-work section which `next` doesn't have. Expected.
- `include/igraph_centrality.h`: Remaining 57/71 are non-betweenness changes (closeness, harmonic, pagerank, eigenvector centrality, hub_and_authority_scores, copyright/header changes, `__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS`).
- `src/centrality/centralization.c`: Remaining 37/76 are changes to other functions (closeness, eigenvector, degree centralization, copyright/formatting changes).
- `tests/unit/igraph_voronoi.c`: Remaining 1/1 is a copyright header change.
- `tests/benchmarks/igraph_betweenness.c`: Remaining 1/1 is a copyright header change.
- `tests/benchmarks/igraph_betweenness_weighted.c`: Remaining 1/1 is a copyright header change.
- `examples/tutorial/tutorial3.c`: Remaining 49/44 are unrelated tutorial changes.
- `examples/simple/igraph_minimum_spanning_tree.c`: Remaining 8/5 are unrelated changes (MST function changes).
- `interfaces/functions.yaml`: Remaining 400/380 are changes to other functions (EDGEWEIGHTS→EDGE_WEIGHTS rename, pagerank, eigenvector, closeness, community, etc.).
- `src/centrality/betweenness.c`, all test files: Reduced to 0/0, fully ported.
