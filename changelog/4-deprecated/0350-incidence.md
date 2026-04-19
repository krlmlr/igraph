# Deprecated `igraph_incidence()` / `igraph_get_incidence()` removed

The two deprecated aliases `igraph_incidence()` and
`igraph_get_incidence()` have been removed. Use the canonical
`igraph_biadjacency()` / `igraph_get_biadjacency()` instead; the
deprecated wrappers only forwarded to these functions.
