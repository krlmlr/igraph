# igraph_maximal_cliques_callback(), igraph_cliques_callback()

**Category**: Cliques and independent sets

`igraph_maximal_cliques_callback()` had its parameter ordering standardized: the `igraph_clique_handler_t *cliquehandler_fn, void *arg` parameter pair now comes at the end, making this function consistent with `igraph_cliques_callback()`.

---

**Original changelog wording:**

> `igraph_maximal_cliques_callback()` had its parameter ordering standardized: the `igraph_clique_handler_t *cliquehandler_fn, void *arg` parameter pair now comes at the end, making this function consistent with `igraph_cliques_callback()`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0770-maximal-cliques-callback.md
  83    59    79    56  include/igraph_cliques.h
 111    40   102    41  src/cliques/maximal_cliques.c
  96    34    94    32  src/cliques/cliques.c
   4     4     2     2  tests/unit/maximal_cliques_callback.c
 385   369   382   367  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0770-maximal-cliques-callback.md`: Fully absorbed (11→0 add, 0→0 del). The proof-of-work section added here causes del-after to remain 0 since `next` doesn't have this section.
- `include/igraph_cliques.h`: Decreased (83→79 add, 59→56 del). Remaining diffs are copyright/license header updates, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, formatting changes, and `max_results` parameters for other functions.
- `src/cliques/maximal_cliques.c`: Decreased add (111→102), del increased by 1 (40→41). The small del increase is due to the preprocessor rename approach (`#define`/`#undef` wrapper) which differs slightly from `next`'s full template refactoring; this will be resolved when later entries port the template rename.
- `src/cliques/cliques.c`: Decreased (96→94 add, 34→32 del). Remaining diffs are other function changes and copyright updates.
- `tests/unit/maximal_cliques_callback.c`: Decreased (4→2 add, 4→2 del). Remaining diffs are copyright header update and `IGRAPH_UNLIMITED` changes for `igraph_maximal_cliques()` call.
- `interfaces/functions.yaml`: Decreased (385→382 add, 369→367 del). Remaining diffs are parameter changes for other functions.
