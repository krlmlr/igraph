# igraph_subisomorphic_lad()

**Category**: Isomorphism functions and permutations

`igraph_subisomorphic_lad()` does not have a CPU time limit parameter any more. If you wish to stop the calculation from another thread or a higher level interface, use igraph's interruption mechanism.

---

**Original changelog wording:**

> `igraph_subisomorphic_lad()` does not have a CPU time limit parameter any more. If you wish to stop the calculation from another thread or a higher level interface, use igraph's interruption mechanism.

## Proof of work

`git diff --numstat HEAD..next` for modified files, before and after:

| before+  | before-  | after+   | after-   | file                                         |
|---------:|---------:|---------:|---------:|----------------------------------------------|
|        9 |        7 |        6 |        4 | examples/simple/igraph_subisomorphic_lad.c   |
|       16 |       59 |       15 |       58 | include/igraph_isomorphism.h                 |
|      411 |      391 |      410 |      390 | interfaces/functions.yaml                    |
|        5 |       10 |        5 |        2 | src/isomorphism/lad.c                        |
|        4 |        5 |        2 |        3 | src/properties/perfect.c                     |
|        2 |        2 |        1 |        1 | tests/benchmarks/lad.c                       |
|        1 |        1 |        1 |        1 | tests/unit/igraph_subisomorphic.c            |
|        8 |        6 |        6 |        4 | tests/unit/igraph_subisomorphic_lad.c        |

### Remaining differences explained

- `examples/simple/igraph_subisomorphic_lad.c` (6+/4-): Comment style changes (`IGraph` -> `igraph`), `igraph_integer_t` -> `igraph_int_t`, and `igraph_setup()` addition — these belong to other changelog entries.
- `include/igraph_isomorphism.h` (15+/58-): Other entries remove deprecated functions (`igraph_transitive_closure_dag`, `igraph_isomorphic_function_vf2`, `igraph_subisomorphic_function_vf2`), add new declarations, and rename existing ones.
- `interfaces/functions.yaml` (410+/390-): Bulk type renames and other function signature changes unrelated to this entry.
- `src/isomorphism/lad.c` (5+/2-): Remaining comment style changes (`IGraph` -> `igraph`, mode line removal).
- `src/properties/perfect.c` (2+/3-): Comment style changes and `igraph_is_simple()` signature change (added `IGRAPH_DIRECTED` parameter) from another entry.
- `tests/benchmarks/lad.c` (1+/1-): Comment style change (`IGraph` -> `igraph`).
- `tests/unit/igraph_subisomorphic.c` (1+/1-): Comment style change (`IGraph` -> `igraph`).
- `tests/unit/igraph_subisomorphic_lad.c` (6+/4-): Comment style change and formatting adjustments from other entries.
