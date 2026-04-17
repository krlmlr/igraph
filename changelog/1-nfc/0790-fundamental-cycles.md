# igraph_fundamental_cycles(), igraph_minimum_cycle_basis()

**Category**: Other network analysis

The experimental functions `igraph_fundamental_cycles()` and `igraph_minimum_cycle_basis()` now use the type `igraph_real_t` for their `bfs_cutoff` parameter, and had their `weights` parameter moved to the 2nd position.

---

**Original changelog wording:**

> The experimental functions `igraph_fundamental_cycles()` and `igraph_minimum_cycle_basis()` now use the type `igraph_real_t` for their `bfs_cutoff` parameter, and had their `weights` parameter moved to the 2nd position.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0790-fundamental-cycles.md
  38    24    33    15  include/igraph_cycles.h
   0     0     0     0  src/misc/cycle_bases.c
  14    14     2     2  tests/unit/cycle_bases.c
 381   365   377   364  interfaces/functions.yaml
   7     3     6     2  fuzzing/misc_algos.cpp
```

Notes on remaining differences:
- `changelog/1-nfc/0790-fundamental-cycles.md`: Fully ported (0/0 remaining). The proof-of-work section added to main-dev will increase del count in the final commit since next doesn't have it.
- `include/igraph_cycles.h`: Remaining diff (33/15) is from other changelog entries: copyright/license header changes, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, `IGRAPH_EXPERIMENTAL` annotations, new functions (`igraph_topological_sorting`, `igraph_is_dag`, `igraph_feedback_arc_set`, `igraph_feedback_vertex_set`), and `igraph_simple_cycles` signature changes.
- `src/misc/cycle_bases.c`: Shows 0/0 because git detects the rename to `src/cycles/cycle_bases.c` on `next`.
- `tests/unit/cycle_bases.c`: Remaining diff (2/2) is the copyright header change (`IGraph` → `igraph`).
- `interfaces/functions.yaml`: Remaining diff (377/364) is from many other function definition changes across the file.
- `fuzzing/misc_algos.cpp`: Remaining diff (6/2) includes copyright header change, addition of `igraph_transitive_closure` call, and `igraph_get_all_simple_paths` signature change.
