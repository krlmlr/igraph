# `igraph_strvector_swap()`

A new `igraph_strvector_swap(v1, v2)` helper has been added. It
swaps the entire contents of two string vectors in O(1) time by
swapping their internal book-keeping fields, mirroring
`igraph_vector_swap()` for numeric vectors.
