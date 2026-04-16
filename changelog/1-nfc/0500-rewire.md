# igraph_rewire()

**Category**: Graph generators

`igraph_rewire()` now takes an `igraph_edge_type_sw_t allowed_edge_types` parameter to specify whether to create self-loops. The `igraph_rewiring_t` enum type was removed. Instead of the old `IGRAPH_REWIRING_SIMPLE`, use `IGRAPH_SIMPLE_SW`. Instead of the old `IGRAPH_REWIRING_SIMPLE_LOOPS`, use `IGRAPH_LOOPS_SW`.

---

**Original changelog wording:**

> `igraph_rewire()` now takes an `igraph_edge_type_sw_t allowed_edge_types` parameter to specify whether to create self-loops. The `igraph_rewiring_t` enum type was removed. Instead of the old `IGRAPH_REWIRING_SIMPLE`, use `IGRAPH_SIMPLE_SW`. Instead of the old `IGRAPH_REWIRING_SIMPLE_LOOPS`, use `IGRAPH_LOOPS_SW`.

---

**Proof of work: `git diff --numstat HEAD..next` for modified files**

```
File                                                     BEFORE(+/-)  AFTER(+/-)
include/igraph_constants.h                                     95/51       95/47
include/igraph_operators.h                                     34/26       13/25
src/operators/rewire.c                                       111/105         1/3
src/operators/rewire_internal.h                                  7/5         2/2
src/games/degree_sequence.c                                     5/21        4/20
examples/simple/igraph_assortativity_degree.c                    5/2         4/1
examples/simple/igraph_assortativity_nominal.c                  10/7         9/6
fuzzing/linear_algos_directed.cpp                              13/13       12/12
fuzzing/linear_algos_undirected.cpp                            53/14       52/13
tests/benchmarks/igraph_average_path_length_unweighted.c       12/12       11/11
tests/unit/igraph_rewire.c                                       8/9         1/2
interfaces/types.yaml                                          41/41       36/36
interfaces/functions.yaml                                    443/436     442/435
tests/benchmarks/igraph_rewire.c                                77/0           -
tests/CMakeLists.txt                                           30/16       29/16
changelog/1-nfc/0500-rewire.md                                  11/0           -
```

Remaining differences are unrelated to this change:
- `include/igraph_constants.h` (95/47): other enum removals, doc comments, formatting
- `include/igraph_operators.h` (13/25): `const` removal from params, `IGRAPH_EXPERIMENTAL`, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, license
- `src/operators/rewire.c` (1/3): license header cosmetics
- `src/operators/rewire_internal.h` (2/2): `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`
- `src/games/degree_sequence.c` (4/20): unrelated changes
- Other files: license headers, unrelated refactors, formatting
