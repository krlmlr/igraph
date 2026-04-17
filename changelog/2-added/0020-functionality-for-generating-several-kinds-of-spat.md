# Functionality for generating several kinds of spatial networks.

Functionality for generating several kinds of spatial networks.

---

**Original changelog wording:**

> Functionality for generating several kinds of spatial networks.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     9     0  changelog/2-added/0020-functionality-for-generating-several-kinds-of-spat.md
  91     0     2     2  include/igraph_spatial.h
   5     7     4     7  include/igraph.h
   5    29     5    27  include/igraph_nongraph.h
  22    14    14    12  src/CMakeLists.txt
 816     0     0     0  src/spatial/beta_skeleton.cpp
 188     0     0     0  src/spatial/convex_hull.c
 280     0     1    55  src/spatial/delaunay.c
 119     0     0     0  src/spatial/edge_lengths.c
 189     0     0     0  src/spatial/nearest_neighbor.cpp
 121     0     0     0  src/spatial/nanoflann_internal.hpp
  34     0     2     2  src/spatial/spatial_internal.h
   1   208     2    40  src/misc/other.c
  26    15    13    15  tests/CMakeLists.txt
 182     0     0     0  tests/unit/beta_skeletons.c
 338     0     0     0  tests/unit/beta_skeletons.out
 217     0     0     0  tests/unit/igraph_delaunay_graph.c
 713     0     0     0  tests/unit/igraph_delaunay_graph.out
 278     0     0     0  tests/unit/igraph_nearest_neighbor_graph.c
 809     0     0     0  tests/unit/igraph_nearest_neighbor_graph.out
  64     0     0     0  tests/unit/igraph_spatial_edge_lengths.c
   7     0     0     0  tests/unit/igraph_spatial_edge_lengths.out
 150     0     0     0  tests/benchmarks/beta_skeletons.c
  64     0     0     0  tests/benchmarks/igraph_delaunay_graph.c
  77     0     0     0  tests/benchmarks/igraph_nearest_neighbor_graph.c
 350   351   322   353  interfaces/functions.yaml
  36    41    31    41  interfaces/types.yaml
```

Notes on remaining differences:
- **include/igraph_spatial.h**: 2 add / 2 del remaining — adaptation from `IGRAPH_BEGIN_C_DECLS`/`IGRAPH_END_C_DECLS` to `__BEGIN_DECLS`/`__END_DECLS` (not yet renamed on main-dev).
- **src/spatial/spatial_internal.h**: Same `BEGIN_C_DECLS` → `__BEGIN_DECLS` adaptation.
- **src/spatial/delaunay.c**: 1 add / 55 del remaining — the `igraph_matrix_copy_to` row-major overload and `igraph_i_simplify_edge_list` utility are not yet on main-dev; a manual row-major loop and a local static implementation were used instead, adding 55 lines. These will be resolved when the corresponding utility changes are ported.
- **src/misc/other.c**: 2 add / 40 del remaining — the deprecated `igraph_convex_hull` wrapper remains (removal is a separate changelog entry 4-deprecated/0040). The `#include "igraph_spatial.h"` was added so the wrapper can find `igraph_convex_hull_2d`.
- **include/igraph_nongraph.h**: Reduced from 5/29 to 5/27 — `igraph_convex_hull_2d` declaration removed (moved to spatial header). Remaining diffs from other entries.
- **interfaces/functions.yaml**: Reduced from 350/351 to 322/353 — spatial function definitions added. Small increase in del count (2) from the new section header.
- **interfaces/types.yaml**: Reduced from 36/41 to 31/41 — `METRIC` type added.
- **changelog file**: 9 add before and after, as the file is copied from next. The proof-of-work section will add del lines in the after numstat since next doesn't have it.
