# Deprecated `igraph_i_set_attribute_table()` removed

The long-deprecated `igraph_i_set_attribute_table()` alias has been
removed; use `igraph_set_attribute_table()` directly. The `_i_`
prefixed name existed only as a compatibility shim that called
`igraph_set_attribute_table()` after emitting a deprecation
warning.
