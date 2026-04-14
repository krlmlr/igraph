# igraph_rewire()

**Category**: Graph generators

`igraph_rewire()` now takes an `igraph_edge_type_sw_t allowed_edge_types` parameter to specify whether to create self-loops. The `igraph_rewiring_t` enum type was removed. Instead of the old `IGRAPH_REWIRING_SIMPLE`, use `IGRAPH_SIMPLE_SW`. Instead of the old `IGRAPH_REWIRING_SIMPLE_LOOPS`, use `IGRAPH_LOOPS_SW`.

---

**Original changelog wording:**

> `igraph_rewire()` now takes an `igraph_edge_type_sw_t allowed_edge_types` parameter to specify whether to create self-loops. The `igraph_rewiring_t` enum type was removed. Instead of the old `IGRAPH_REWIRING_SIMPLE`, use `IGRAPH_SIMPLE_SW`. Instead of the old `IGRAPH_REWIRING_SIMPLE_LOOPS`, use `IGRAPH_LOOPS_SW`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0500-rewire.md
 111   105     2     4  src/operators/rewire.c
   7     5     2     2  src/operators/rewire_internal.h
  95    51    95    47  include/igraph_constants.h
  34    26    13    25  include/igraph_operators.h
   5    21     4    20  src/games/degree_sequence.c
   8     9     1     2  tests/unit/igraph_rewire.c
  77     0     0     0  tests/benchmarks/igraph_rewire.c
  30    16    29    16  tests/CMakeLists.txt
 443   434   442   433  interfaces/functions.yaml
  41    41    36    36  interfaces/types.yaml
  10     7     9     6  examples/simple/igraph_assortativity_nominal.c
   5     2     4     1  examples/simple/igraph_assortativity_degree.c
  12    12    11    11  tests/benchmarks/igraph_average_path_length_unweighted.c
```

Notes on remaining differences:
- `changelog/1-nfc/0500-rewire.md`: The `add-a` is 0 because the file now exists on `main-dev` (with the proof-of-work section added). The small `del-a` of 0 reflects this — the remaining diff is only the proof-of-work section itself which `next` does not have.
- `src/operators/rewire.c`: Reduced from 111/105 to 2/4, reflecting the main change was applied. Tiny residual from minor formatting differences (copyright header comment style).
- `src/operators/rewire_internal.h`: Reduced from 7/5 to 2/2, residual from `__BEGIN_DECLS` vs `IGRAPH_BEGIN_C_DECLS` (a different changelog entry).
- `include/igraph_constants.h`: Residual 95/47 reflects many other unrelated changes in that file (other enum removals, documentation additions) that belong to different changelog entries.
- `include/igraph_operators.h`: Reduced from 34/26 to 13/25. The remaining differences are copyright header style, `__BEGIN_DECLS` vs `IGRAPH_BEGIN_C_DECLS`, and `const igraph_vs_t` vs `igraph_vs_t` parameter changes that belong to other entries.
- `src/games/degree_sequence.c`: 5/21 → 4/20, minimal residual from other unrelated changes in that file.
- `tests/unit/igraph_rewire.c`: Reduced to 1/2, residual from copyright header style (`/* -*- mode: C -*- */`).
- `tests/benchmarks/igraph_rewire.c`: Now 0/0, fully ported (new file).
- `tests/CMakeLists.txt`: 30/16 → 29/16, the `igraph_rewire` benchmark entry was added; remaining differences are other CMakeLists additions not related to this entry.
- `interfaces/functions.yaml` and `interfaces/types.yaml`: Residual differences are from many other API changes in those files belonging to different changelog entries.
- Example files: Small residuals from other changes in those files.
- `tests/benchmarks/igraph_average_path_length_unweighted.c`: 12/12 → 11/11, one line updated, residual is other changes.
