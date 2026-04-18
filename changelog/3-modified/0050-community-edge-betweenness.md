# igraph_community_edge_betweenness()

`igraph_community_edge_betweenness()` now takes both a `weights` and a `lengths` parameter, and treats edges with large weights as strong connections. Edge weights (interpreted as connection strengths) are used to divide betweenness scores before selecting them for removal as well as for the modularity computation. Edge lengths are used for defining shortest path lengths during the betweenness computation.

---

**Original changelog wording:**

> `igraph_community_edge_betweenness()` now takes both a `weights` and a `lengths` parameter, and treats edges with large weights as strong connections. Edge weights (interpreted as connection strengths) are used to divide betweenness scores before selecting them for removal as well as for the modularity computation. Edge lengths are used for defining shortest path lengths during the betweenness computation.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     9     0  changelog/3-modified/0050-community-edge-betweenness.md
  99    63     1     3  src/community/edge_betweenness.c
  14    17    12    16  include/igraph_community.h
  35    23     1     2  tests/unit/igraph_community_edge_betweenness.c
   2     2     1     1  tests/unit/igraph_community_eb_get_merges.c
  17     7    16     6  tests/unit/null_communities.c
  11     3    10     2  tests/unit/community_indexing.c
  13     6    12     5  fuzzing/community.cpp
   8     5     7     4  fuzzing/weighted_community.cpp
  10     5     4     1  examples/simple/igraph_community_edge_betweenness.c
   7     4     0     0  examples/simple/igraph_community_edge_betweenness.out
 306   347   304   346  interfaces/functions.yaml
```

Notes on remaining differences:
- `src/community/edge_betweenness.c`: Nearly fully ported (99/63 → 1/3). Remaining differences are copyright header NFC changes from other entries.
- `include/igraph_community.h`: Remaining 12/16 are NFC changes (copyright, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, `const igraph_bool_t`→`igraph_bool_t`, `const igraph_real_t`→`igraph_real_t`, `EDGEWEIGHTS`→`EDGE_WEIGHTS`, `IGRAPH_EXPERIMENTAL` on `igraph_community_voronoi`) from other entries.
- `tests/unit/igraph_community_edge_betweenness.c`: Nearly fully ported (35/23 → 1/2). Remaining is copyright header NFC.
- `tests/unit/igraph_community_eb_get_merges.c`: Remaining 1/1 is unrelated NFC.
- `tests/unit/null_communities.c`, `community_indexing.c`: Remaining are unrelated changes from other entries.
- `fuzzing/community.cpp`, `fuzzing/weighted_community.cpp`: Remaining changes from other entries (label_propagation, leiden, assortativity_nominal API changes).
- `examples/simple/igraph_community_edge_betweenness.c`: Remaining 4/1 are copyright header + `igraph_setup()` call from other entries.
- `interfaces/functions.yaml`: Remaining 304/346 are from many other function entries.
- `changelog/3-modified/0050-community-edge-betweenness.md`: 9/0 after because proof-of-work section is not on next.
