# igraph_community_optimal_modularity()

**Category**: Community detection

`igraph_community_optimal_modularity()` now takes a `resolution` parameter and its `weight` parameter was moved to the second place.

---

**Original changelog wording:**

> `igraph_community_optimal_modularity()` now takes a `resolution` parameter and its `weight` parameter was moved to the second place.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0    11     0  changelog/1-nfc/0650-community-optimal-modularity.md
  18     9     1     3  src/community/optimal_modularity.c
  44    24    40    21  include/igraph_community.h
  22    75     0     0  examples/simple/igraph_community_optimal_modularity.c
 169     0     1     1  tests/unit/igraph_community_optimal_modularity.c
  22     9    21     8  tests/unit/null_communities.c
  13     5    12     4  tests/unit/community_indexing.c
  28    16    27    16  tests/CMakeLists.txt
 419   383   418   382  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0650-community-optimal-modularity.md`: 11 add-after is due to the proof-of-work section appended to the changelog file, which doesn't exist on `next`.
- `src/community/optimal_modularity.c`: Reduced from 18+9 to 1+3. Remaining diff is cosmetic (comment header style changes that belong to a different entry).
- `include/igraph_community.h`: Reduced from 44+24 to 40+21. Remaining diff is from other unrelated function signature changes (spinglass, infomap, edge_betweenness, leiden, label_propagation, voronoi, modularity, etc.).
- `examples/simple/igraph_community_optimal_modularity.c`: Fully converged (0+0).
- `tests/unit/igraph_community_optimal_modularity.c`: Reduced from 169+0 to 1+1. The remaining 1+1 is from adapting `igraph_edge_betweenness()` call to `main-dev` API (different signature on `next`).
- `tests/unit/null_communities.c`: Reduced from 22+9 to 21+8. Remaining diff is from other unrelated changes (edge_betweenness, infomap, label_propagation).
- `tests/unit/community_indexing.c`: Reduced from 13+5 to 12+4. Remaining diff is from other unrelated changes (label_propagation, edge_betweenness, infomap).
- `tests/CMakeLists.txt`: Reduced from 28+16 to 27+16. Remaining diff is from other unrelated test additions/removals.
- `interfaces/functions.yaml`: Reduced from 419+383 to 418+382. Remaining diff is from many other unrelated function changes (no_rng flags, EDGE_WEIGHTS rename, etc.).
