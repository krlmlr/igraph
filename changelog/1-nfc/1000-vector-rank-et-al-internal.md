# Vector helpers consolidated (`_rank`, `_order2`, `_e_tol`)

Three internal helpers in `src/core/vector.c` have been cleaned
up:

- `igraph_vector_order2()` (heap-based sort, no longer called from
  anywhere) has been removed.
- `igraph_vector_rank()` (the `igraph_real_t` variant) has been
  removed; no callers in the codebase.
- `igraph_vector_int_rank()` has been renamed to
  `igraph_i_vector_int_rank()` to match the `_i_` prefix used for
  internal helpers. The sole caller,
  `src/flow/flow.c:igraph_all_st_mincuts_minimal()`, is updated
  accordingly.
- `igraph_vector_e_tol()` (deprecated absolute-tolerance
  comparison) has been removed. The relative-tolerance
  `igraph_vector_all_almost_e()` is the supported replacement.

Pure internal clean-up: none of these symbols were declared in a
public header.
