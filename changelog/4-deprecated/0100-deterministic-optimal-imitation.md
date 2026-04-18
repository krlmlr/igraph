# igraph_deterministic_optimal_imitation() and 3 others

The deprecated `igraph_deterministic_optimal_imitation()`, `igraph_moran_process()`, `igraph_roulette_wheel_imitation()` and `igraph_stochastic_imitation()` functions were removed.

---

**Original changelog wording:**

> The deprecated `igraph_deterministic_optimal_imitation()`, `igraph_moran_process()`, `igraph_roulette_wheel_imitation()` and `igraph_stochastic_imitation()` functions were removed.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0100-deterministic-optimal-imitation.md
   0  1197     0     0  src/misc/microscopic_update.c
   0    61     0     0  include/igraph_microscopic_update.h
  66    64    66    57  include/igraph_constants.h
   3     7     3     6  include/igraph.h
  11    10    11     9  src/CMakeLists.txt
 304   289   304   289  interfaces/functions.yaml
  31    51    31    41  interfaces/types.yaml
   0   172     0     0  examples/simple/igraph_deterministic_optimal_imitation.c
   0   213     0     0  examples/simple/igraph_roulette_wheel_imitation.c
   0   182     0     0  examples/simple/igraph_stochastic_imitation.c
```

Notes on remaining differences:
- `src/misc/microscopic_update.c`, `include/igraph_microscopic_update.h`, all 3 examples: fully removed (0/0), matching `next`.
- `include/igraph_constants.h`: del reduced 64→57. Remaining are copyright/license header changes and other enum changes from later entries.
- `include/igraph.h`: del reduced 7→6. Remaining are other header include changes.
- `src/CMakeLists.txt`: del reduced 10→9. Remaining are other source file removals.
- `interfaces/functions.yaml`: del reduced 317→289. Remaining are other function removals/changes.
- `interfaces/types.yaml`: del reduced 51→41. Remaining are other type changes.
