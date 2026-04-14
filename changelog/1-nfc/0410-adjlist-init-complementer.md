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
  11     0     0     0  changelog/1-nfc/0410-adjlist-init-complementer.md
   7    12     6    11  include/igraph_adjlist.h
  96    93    94    91  include/igraph_centrality.h
  23    45    22    44  include/igraph_structural.h
  20    18    20    18  include/igraph_interface.h
  73   136    52   134  src/graph/adjlist.c
  36    47    31    28  src/properties/degrees.c
 177    93    63    56  src/graph/type_indexededgelist.c
  52    90    47    87  src/centrality/centralization.c
  37     7     1     1  tests/unit/igraph_adjlist_init_complementer.c
  45     3     0     0  tests/unit/igraph_adjlist_init_complementer.out
  39    15     0     0  tests/unit/igraph_degree.c
   9     6     0     0  tests/unit/igraph_degree.out
```

Notes on remaining differences:
- `changelog/1-nfc/0410-adjlist-init-complementer.md`: Now 0/0 in `next` (which doesn't have the proof-of-work section). After appending proof-of-work, the file will differ from `next` by the added section only.
- `include/igraph_interface.h`: Unchanged 20/18 because `next` also changes `igraph_neighbors()` signature (adding `loops` and `multiple` parameters) and updates the copyright header — those belong to later changelog entries.
- `include/igraph_adjlist.h`: Remaining 6/11 — `next` also changes the copyright header and `__BEGIN_DECLS`/`__END_DECLS` to `IGRAPH_BEGIN_C_DECLS`/`IGRAPH_END_C_DECLS`.
- `include/igraph_centrality.h`: Remaining 94/91 — large file with many other function changes in `next`.
- `include/igraph_structural.h`: Remaining 22/44 — `next` also changes `igraph_density()`, `igraph_is_simple()`, `igraph_minimum_spanning_tree()`, removes deprecated functions, and updates copyright/macros.
- `src/graph/adjlist.c`: Remaining 52/134 — `next` has many additional changes (copyright header, `igraph_adjlist_init()` changes using `igraph_i_neighbors`).
- `src/properties/degrees.c`: Remaining 31/28 — `next` also removes `\experimental` from `igraph_degree_correlation_vector()` and updates `igraph_neighbors()` calls with new parameters.
- `src/graph/type_indexededgelist.c`: Remaining 63/56 — `next` also changes `igraph_incident()`, `igraph_neighbors()`, and error message formatting.
- `src/centrality/centralization.c`: Remaining 47/87 — `next` also changes `igraph_betweenness()` call signature and fixes a typo in a comment.
