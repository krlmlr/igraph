# `igraph_biadjacency()` accepts negative matrix entries with `multiple = false`

When `multiple = false`, `igraph_biadjacency()` now treats any
non-zero entry of the input matrix as an edge regardless of sign;
the up-front non-negativity check has been moved inside the
`if (multiple)` branch. This matters only when the caller relies
on `multiple = true` semantics, where the entry's integer part is
used as the number of parallel edges to create; those callers
still get `IGRAPH_EINVAL` on negative entries.
