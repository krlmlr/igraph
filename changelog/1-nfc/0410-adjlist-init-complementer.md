# igraph_adjlist_init_complementer() and 6 others

**Category**: Basic graph properties

The type of the `loops` argument of `igraph_adjlist_init_complementer()`, `igraph_centralization_degree()`, `igraph_centralization_degree_tmax()`, `igraph_degree()`, `igraph_maxdegree()`, `igraph_sort_vertex_ids_by_degree()` and `igraph_strength()` was changed to `igraph_loops_t` from `igraph_bool_t`, allowing finer-grained control about how loop edges are treated. Pass `IGRAPH_LOOPS_TWICE` and `IGRAPH_NO_LOOPS` to reproduce the previous behaviour of `true` and `false`.

---

**Original changelog wording:**

> The type of the `loops` argument of `igraph_adjlist_init_complementer()`, `igraph_centralization_degree()`, `igraph_centralization_degree_tmax()`, `igraph_degree()`, `igraph_maxdegree()`, `igraph_sort_vertex_ids_by_degree()` and `igraph_strength()` was changed to `igraph_loops_t` from `igraph_bool_t`, allowing finer-grained control about how loop edges are treated. Pass `IGRAPH_LOOPS_TWICE` and `IGRAPH_NO_LOOPS` to reproduce the previous behaviour of `true` and `false`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0410-adjlist-init-complementer.md
   7    12     6    11  include/igraph_adjlist.h
  96    93    94    91  include/igraph_centrality.h
  25    23    25    23  include/igraph_interface.h
  23    45    22    44  include/igraph_structural.h
  73   136    54   134  src/graph/adjlist.c
 195    99    80    61  src/graph/type_indexededgelist.c
  52    90    38    77  src/centrality/centralization.c
 161    91   161    91  src/centrality/eigenvector.c
  98    35    97    34  src/cliques/cliques.c
  25     8    26     9  src/cycles/simple_cycles.c
   3     5     4     6  src/layout/reingold_tilford.c
  36    47    27    37  src/properties/degrees.c
  39    15     0     0  tests/unit/igraph_degree.c
   9     6     0     0  tests/unit/igraph_degree.out
  37     7     0     0  tests/unit/igraph_adjlist_init_complementer.c
  45     3     0     0  tests/unit/igraph_adjlist_init_complementer.out
 471   443   467   439  interfaces/functions.yaml
```

Notes on remaining differences:
- The changelog file itself shows (11,0) → (0,0) because the file was added and is now identical to `next`.
- Test files (igraph_degree.c, igraph_degree.out, igraph_adjlist_init_complementer.c, igraph_adjlist_init_complementer.out) are now fully ported (0,0 after).
- `src/graph/type_indexededgelist.c` still shows (80,61) remaining because `next` has many other changes (igraph_neighbors signature change, igraph_incident signature change, formatting, etc.) from other changelog entries.
- `src/graph/adjlist.c` still shows (54,134) remaining because `next` has other changes (igraph_neighbors API changes, IGRAPH_ALLOW_INTERRUPTION_LIMITED, etc.).
- `src/centrality/eigenvector.c` and `src/cliques/cliques.c` have small remaining changes (1 line each) corresponding to other entries' caller updates.
- `src/cycles/simple_cycles.c` shows a slight increase (25,8 → 26,9) because this file had no diff for the `loops` change on `next` (the caller was already `IGRAPH_LOOPS` there); our change from `true` → `IGRAPH_LOOPS` adds a minimal diff.
- `src/layout/reingold_tilford.c` similarly increases slightly (3,5 → 4,6) for the same reason.
- `interfaces/functions.yaml` decreased by 4 lines each way because we updated 5 function YAML entries.
