# igraph_weighted_cliques()

**Category**: Cliques and independent sets

`igraph_weighted_cliques()` had its parameter ordering standardized: the `igraph_bool_t maximal` parameter now comes before the `min_weight` / `max_weight` parameters.

---

**Original changelog wording:**

> `igraph_weighted_cliques()` had its parameter ordering standardized: the `igraph_bool_t maximal` parameter now comes before the `min_weight` / `max_weight` parameters.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  83    58    83    59  include/igraph_cliques.h
  97    34    96    34  src/cliques/cliques.c
   8     8     8     8  tests/unit/igraph_weighted_cliques.c
   2     3     2     3  tests/regression/bug_2150.c
 386   369   385   369  interfaces/functions.yaml
```

Notes on remaining differences:
- `include/igraph_cliques.h`: del increased by 1 because our reordering puts `maximal` on its own line; next also adds `max_results` and reformats differently, so the line we added becomes a deletion against next.
- `src/cliques/cliques.c`: add decreased by 1 — the doc comment reordering brought us 1 line closer to next.
- `tests/unit/igraph_weighted_cliques.c` and `tests/regression/bug_2150.c`: No change in diff — remaining differences are due to `IGRAPH_UNLIMITED` (max_results) addition in next, which belongs to a later entry.
- `interfaces/functions.yaml`: add decreased by 1 — the parameter reordering brought us closer to next. Remaining differences are type renames (`VERTEXWEIGHTS` → `VERTEX_WEIGHTS`, `VERTEXSET_LIST` → `VERTEX_INDICES_LIST`), `max_results` addition, and default value changes that belong to later entries.
