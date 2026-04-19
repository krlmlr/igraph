# `igraph_i_simplify_edge_list()` extracted to `src/internal/utils.c`

The static `simplify_edge_list()` helper that the Delaunay graph
constructor used locally to drop self-loops and duplicate edges
from an edge list has been promoted to a non-static
`igraph_i_simplify_edge_list()` function living in
`src/internal/utils.c`. The declaration now lives in
`src/internal/utils.h` and is available to any igraph translation
unit that needs the same in-place edge-list simplification, not
just Delaunay.

Pure code re-organisation; no behaviour change and no public-API
change.
