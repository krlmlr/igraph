# Several functions that can generate a large number of results (cliques, cycle...

Several functions that can generate a large number of results (cliques, cycles, etc.) now have a feature to limit the number of returned results, or to return a single result only.

---

**Original changelog wording:**

> Several functions that can generate a large number of results (cliques, cycles, etc.) now have a feature to limit the number of returned results, or to return a single result only.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0010-several-functions-that-can-generate-a-large-number.md
  79    56     9    14  include/igraph_cliques.h
  95    47    85    48  include/igraph_constants.h
  33    15    30    11  include/igraph_cycles.h
   7     5     3     3  src/cliques/cliquer_internal.h
  21     8     2     2  src/cliques/cliquer_wrapper.c
  94    32     1     2  src/cliques/cliques.c
 102    41    64    62  src/cliques/maximal_cliques.c
  29    18     1     2  src/cliques/maximal_cliques_template.h
  26     9     2     2  src/cycles/simple_cycles.c
   6    25     5    24  src/cliques/glet.c
 370   357   350   351  interfaces/functions.yaml
   3     3     3     3  tests/benchmarks/igraph_cliques.c
   6     5     6     5  tests/benchmarks/igraph_maximal_cliques.c
   6     5     6     5  tests/unit/igraph_maximal_cliques.c
   6     5     6     5  tests/unit/igraph_maximal_cliques2.c
   3     3     3     3  tests/unit/igraph_maximal_cliques3.c
   7     5     7     5  tests/unit/igraph_maximal_cliques4.c
   5     5     1     1  tests/unit/igraph_maximal_cliques_file.c
   2     2     2     2  tests/unit/maximal_cliques_callback.c
   8     8     0     0  tests/unit/igraph_weighted_cliques.c
   7     7     1     1  tests/unit/igraph_simple_cycles.c
   2     3     1     2  tests/regression/bug_2150.c
  13    11    10     8  examples/simple/igraph_cliques.c
  11     9    11     9  examples/simple/igraph_maximal_cliques.c
  18    10    17     9  examples/simple/igraph_independent_sets.c
   6     3     6     3  examples/simple/igraph_vector_int_list_sort.c
```

Notes on remaining differences:
- `include/igraph_cliques.h`: Remaining diff (9+/14-) is cosmetic reformatting (copyright header, `IGraph`→`igraph`, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`) belonging to later entries.
- `include/igraph_constants.h`: Remaining diff (85+/48-) is unrelated refactoring of `igraph_loops_t`, `igraph_order_t`, and other type enums.
- `include/igraph_cycles.h`: Remaining diff (30+/11-) includes moving `igraph_topological_sorting`/`igraph_is_dag` declarations, adding `IGRAPH_EXPERIMENTAL`, and adding `igraph_feedback_arc_set`/`igraph_feedback_vertex_set`.
- `src/cliques/maximal_cliques.c`: After diff (64+/62-) increased vs before (102+/41-) in total — the increase in deletions is because we restructured the template inclusion pattern (functions moved before the template includes as forward declarations + wrappers). The overall structure now matches `next`.
- `interfaces/functions.yaml`: Remaining diff (350+/351-) is mostly type renames (`VERTEXSET_LIST`→`VERTEX_INDICES_LIST`, `EDGEWEIGHTS`→`EDGE_WEIGHTS`, etc.) throughout the file, belonging to later entries.
- `changelog/2-added/0010-...`: After diff now 0/0 (was 9/0) — file fully ported. Proof-of-work section exists only on `main-dev`, increasing the del-after for this file in future comparisons.
