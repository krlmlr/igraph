# igraph_community_leiden()

**Category**: Community detection

`igraph_community_leiden()` now takes two `vertex_out_weights` and `vertex_in_weights` parameters in order to support directed graphs, instead of the previous single `node_weights` parameter. To obtain the old behavior for undirected graphs, pass the vertex weights as `vertex_out_weights` and set `vertex_in_weights` to `NULL`.

---

**Original changelog wording:**

> `igraph_community_leiden()` now takes two `vertex_out_weights` and `vertex_in_weights` parameters in order to support directed graphs, instead of the previous single `node_weights` parameter. To obtain the old behavior for undirected graphs, pass the vertex weights as `vertex_out_weights` and set `vertex_in_weights` to `NULL`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0    11     0  changelog/1-nfc/0630-community-leiden.md
 762   313   231     0  src/community/leiden.c
  56    35    45    25  include/igraph_community.h
 127    14    56     1  tests/unit/community_leiden.c
  31    16     0     0  tests/unit/community_leiden.out
  68    24     3     0  examples/simple/igraph_community_leiden.c
   3     0     0     0  examples/simple/igraph_community_leiden.out
  14     7    13     6  fuzzing/community.cpp
   9     6     8     5  fuzzing/weighted_community.cpp
  23    10    22     9  tests/unit/null_communities.c
  14     6    13     5  tests/unit/community_indexing.c
   8     8     7     7  tests/benchmarks/community.c
 422   385   420   384  interfaces/functions.yaml
```

Notes on remaining differences:
- `src/community/leiden.c`: 231 add remaining — mostly the `igraph_community_leiden_simple()` function and the `igraph_leiden_objective_t` enum, which belong to a later changelog entry (2-added/0180).
- `include/igraph_community.h`: 45 add / 25 del remaining — other function signature changes (infomap, edge betweenness, label propagation, etc.) from separate changelog entries, plus `igraph_community_leiden_simple()` declaration.
- `tests/unit/community_leiden.c`: 56 add / 1 del remaining — `igraph_community_leiden_simple()` test calls and input validation tests that belong to 2-added/0180.
- `examples/simple/igraph_community_leiden.c`: 3 add remaining — `igraph_setup()` call from a separate entry.
- `changelog/1-nfc/0630-community-leiden.md`: 11 add remaining — this proof-of-work section (not present on next).
- `fuzzing/community.cpp`, `fuzzing/weighted_community.cpp`, `tests/unit/null_communities.c`, `tests/unit/community_indexing.c`, `tests/benchmarks/community.c`: minimal remaining differences are from other changelog entries (label_propagation variant, edge_betweenness lengths, etc.).
- `interfaces/functions.yaml`: 420 add / 384 del remaining — mostly other function entries being reformatted/updated in later entries.
