# `igraph_vector_int_order1()` renamed to internal `igraph_i_vector_int_order()`

The private-but-exported helper `igraph_vector_int_order1()` is now
named `igraph_i_vector_int_order()` (and stays under
`IGRAPH_PRIVATE_EXPORT`). The `_i_` prefix follows the project
convention for internal-use helpers: it was not intended as a public
API and its only callers live inside `src/`
(`core/vector.c`, `connectivity/separators.c`,
`operators/rewire_edges.c`, `properties/triangles.c` and the
`triangles_template.h` include). The signature is unchanged, so no
real ABI impact for downstream users.
