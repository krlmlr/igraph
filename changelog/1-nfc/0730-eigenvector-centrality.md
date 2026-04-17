# igraph_eigenvector_centrality(), igraph_centralization_eigenvector_centrality(), igraph_centralization_eigenvector_centrality_tmax()

**Category**: Centralities

`igraph_eigenvector_centrality()`, `igraph_centralization_eigenvector_centrality()` and `igraph_centralization_eigenvector_centrality_tmax()` now use a `mode` parameter with possible values `IGRAPH_OUT`, `IGRAPH_IN` or `IGRAPH_ALL` to control how edge directions are considered. Previously they used a boolean `directed` parameter.

---

**Original changelog wording:**

> `igraph_eigenvector_centrality()`, `igraph_centralization_eigenvector_centrality()` and `igraph_centralization_eigenvector_centrality_tmax()` now use a `mode` parameter with possible values `IGRAPH_OUT`, `IGRAPH_IN` or `IGRAPH_ALL` to control how edge directions are considered. Previously they used a boolean `directed` parameter.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0730-eigenvector-centrality.md
  57    71    57    71  include/igraph_centrality.h
 161    91   139    86  src/centrality/eigenvector.c
  37    76    20    47  src/centrality/centralization.c
  63    24     6    10  tests/unit/igraph_eigenvector_centrality.c
  30     0     0     0  tests/unit/igraph_eigenvector_centrality.out
   2     3     1     2  tests/unit/centralization.c
   6     4     6     4  examples/simple/eigenvector_centrality.c
   6     5     5     4  examples/simple/centralization.c
 399   380   399   380  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0730-eigenvector-centrality.md`: Now zero — fully ported (the original 11 added lines are now present on main-dev).
- `include/igraph_centrality.h`: Unchanged (57/71) — remaining diffs are from other changelog entries (hub/authority scores, pagerank, etc.).
- `src/centrality/eigenvector.c`: Reduced from 161/91 to 139/86 — remaining diffs belong to entries 0740 (removal of `scale` parameter) and 0870 (zero centrality warnings).
- `src/centrality/centralization.c`: Reduced from 37/76 to 20/47 — remaining diffs belong to entry 0740 (removal of `scale` parameter and its deprecation warnings) and cosmetic changes.
- `tests/unit/igraph_eigenvector_centrality.c`: Reduced from 63/24 to 6/10 — the new IN/OUT/ALL test cases were ported. Remaining diffs are cosmetic (`IGraph` → `igraph`, `#include <igraph.h>`, removal of `<math.h>`).
- `tests/unit/igraph_eigenvector_centrality.out`: Now zero — fully ported.
- `tests/unit/centralization.c`: Reduced from 2/3 to 1/2 — remaining diff is cosmetic (`IGraph` → `igraph`).
- `examples/simple/eigenvector_centrality.c`: Unchanged (6/4) — remaining diffs are from 0740 (scale removal) and cosmetic changes (igraph_setup(), copyright).
- `examples/simple/centralization.c`: Reduced from 6/5 to 5/4 — remaining diffs are cosmetic (igraph_setup(), `IGRAPH_UNDIRECTED`).
- `interfaces/functions.yaml`: Unchanged (399/380) — remaining diffs are from many other changelog entries.
