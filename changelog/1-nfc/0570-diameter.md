# igraph_diameter() and 5 others

**Category**: Paths and cycles

The weighted variants of `igraph_diameter()`, `igraph_pseudo_diameter()`, `igraph_radius()`, `igraph_graph_center()`, `igraph_eccentricity()` and `igraph_average_path_length()` were merged into the undirected ones by adding a new argument named `weights` in the second position.

---

**Original changelog wording:**

> The weighted variants of `igraph_diameter()`, `igraph_pseudo_diameter()`, `igraph_radius()`, `igraph_graph_center()`, `igraph_eccentricity()` and `igraph_average_path_length()` were merged into the undirected ones by adding a new argument named `weights` in the second position.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0    11     0  changelog/1-nfc/0570-diameter.md
  94   157    63    97  include/igraph_paths.h
 130   155    24    27  src/paths/shortest_paths.c
 138   321    40    34  src/paths/distances.c
   4     6     3     5  src/layout/reingold_tilford.c
 436   429   435   396  interfaces/functions.yaml
   7    11     1     2  tests/unit/igraph_diameter.c
   4     5     1     2  tests/unit/igraph_diameter_dijkstra.c
   9     9     1     1  tests/unit/igraph_eccentricity.c
   5     5     1     1  tests/unit/igraph_eccentricity_dijkstra.c
   2     2     1     1  tests/unit/igraph_average_path_length.c
   4     4     1     1  tests/unit/igraph_average_path_length_dijkstra.c
   3     3     1     1  tests/unit/igraph_pseudo_diameter.c
   6     6     1     1  tests/unit/igraph_pseudo_diameter_dijkstra.c
  34    34    28    28  tests/unit/igraph_graph_center.c
  11    11     6     6  tests/benchmarks/igraph_average_path_length_unweighted.c
   4     1     3     0  examples/simple/igraph_regular_tree.c
   8     5     8     5  examples/simple/igraph_grg_game.c
  23     3    20     0  examples/simple/igraph_eccentricity.c
  34    23    34    23  examples/simple/igraph_diameter.c
   7     3     7     3  examples/simple/igraph_average_path_length.c
   7     5     4     2  examples/simple/igraph_radius.c
  29    25    29    25  examples/tutorial/tutorial1.c
  41    33    41    33  examples/tutorial/tutorial2.c
  33    43    33    43  examples/simple/igraph_get_eids.c
```

Notes on remaining differences:
- `changelog/1-nfc/0570-diameter.md`: 11 adds remain because the proof-of-work section is not in `next`.
- `include/igraph_paths.h`: Remaining diff (63 add, 97 del) is from other changelog entries (copyright/license header changes, `__BEGIN_DECLS` -> `IGRAPH_BEGIN_C_DECLS`, parameter changes in `igraph_distances`, `igraph_get_shortest_paths`, `igraph_get_shortest_path`, `igraph_get_all_shortest_paths`, `igraph_get_all_simple_paths`, efficiency functions, removal of deprecated functions).
- `src/paths/shortest_paths.c`: Remaining diff (24 add, 27 del) is from other entries (copyright changes, `igraph_get_shortest_path` signature changes, efficiency function signature changes, `igraph_neighbors`/`igraph_incident` parameter changes).
- `src/paths/distances.c`: Remaining diff (40 add, 34 del) is from other entries (copyright changes, `igraph_neighbors` calls gaining extra parameters).
- `interfaces/functions.yaml`: Remaining diff from `EDGEWEIGHTS` -> `EDGE_WEIGHTS` rename and other function entry changes.
- Test and example files: Small remaining diffs are copyright header changes and other unrelated modifications.
