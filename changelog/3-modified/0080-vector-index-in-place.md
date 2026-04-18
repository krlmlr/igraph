# igraph_vector_index_in_place()

The in-place variant of `igraph_vector_index()` was renamed from
`igraph_vector_index_int()` to `igraph_vector_index_in_place()`. The
new name is clearer: the `_int` suffix was historically used because
the function took an integer index vector, but that also applies to
the out-of-place `igraph_vector_index()`, so the suffix was
misleading. The new suffix makes the in-place nature of the
operation explicit.

The change applies to all type variants generated from
`src/core/vector.pmt` (`igraph_vector_index_in_place`,
`igraph_vector_int_index_in_place`, etc.). The signature is
unchanged; callers only need to adjust the function name.
