# igraph_distances() and 4 others

**Category**: Paths and cycles

`igraph_distances()`, `igraph_distances_cutoff()`, `igraph_get_shortest_path()`, `igraph_get_shortest_paths()` and `igraph_get_all_shortest_paths()` gained a `weights` argument. The functions now automatically select the appropriate implementation (unweighted, Dijkstra, Bellman-Ford or Johnson) algorithm based on whether weights are present and whether there are negative weights or not. You can still call the individual methods by their more specific names.

---

**Original changelog wording:**

> `igraph_distances()`, `igraph_distances_cutoff()`, `igraph_get_shortest_path()`, `igraph_get_shortest_paths()` and `igraph_get_all_shortest_paths()` gained a `weights` argument. The functions now automatically select the appropriate implementation (unweighted, Dijkstra, Bellman-Ford or Johnson) algorithm based on whether weights are present and whether there are negative weights or not. You can still call the individual methods by their more specific names.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0610-distances.md
  47    81    23    60  include/igraph_paths.h
 430   393   423   386  interfaces/functions.yaml
 119     0     4     6  src/paths/paths_internal.h
 128    44    18    25  src/paths/unweighted.c
 118   102    21    42  src/paths/dijkstra.c
  62    71     5    23  src/paths/bellman_ford.c
  82    70    11    23  src/paths/johnson.c
  14    12     2     4  src/paths/floyd_warshall.c
  35    17     7    11  src/paths/all_shortest_paths.c
   8    10     7     9  src/paths/shortest_paths.c
   2     7     1     6  src/layout/mds.c
 100   148   100   148  tests/benchmarks/igraph_distances.c
   6     6     1     1  tests/benchmarks/igraph_average_path_length_unweighted.c
   4     4     1     1  tests/unit/igraph_distances_floyd_warshall.c
   4     4     1     1  tests/unit/igraph_distances_floyd_warshall_speedup.c
   4     4     3     3  tests/unit/igraph_maxflow.c
   2     3     1     2  tests/unit/igraph_gomory_hu_tree.c
   5     6     1     2  tests/unit/single_target_shortest_path.c
   5     6     4     5  tests/unit/igraph_get_shortest_paths2.c
   8     8     5     5  tests/unit/all_shortest_paths.c
  45    17    45    17  tests/unit/igraph_distances_johnson.c
   2     2     1     1  tests/regression/bug_1760.c
  10    11     8     9  examples/simple/distances.c
  17    15    16    14  examples/simple/igraph_get_shortest_paths.c
```

Notes on remaining differences:
- `include/igraph_paths.h`: Remaining diff includes copyright/license header changes, `__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS`, removal of deprecated functions, removal of `const` from `igraph_vs_t` params, and removal of `igraph_random_edge_walk`. All are from later entries.
- `interfaces/functions.yaml`: Remaining large diff due to many other functions with type renames (`EDGEWEIGHTS` → `EDGE_WEIGHTS`, etc.) and added `FLAGS` fields. Not part of this entry.
- `src/paths/paths_internal.h`: Small remaining diff (4 add, 6 del) due to `__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS` style change on `next`.
- `src/paths/dijkstra.c`: Remaining (21 add, 42 del) is copyright header changes, removal of deprecated `igraph_shortest_paths_dijkstra`, and `igraph_incident` API changes from later entries.
- `src/paths/bellman_ford.c`, `src/paths/johnson.c`, `src/paths/floyd_warshall.c`, `src/paths/all_shortest_paths.c`: Similarly, remaining diffs are copyright/header changes and `igraph_incident`/`igraph_neighbors` API changes from later entries.
- `tests/benchmarks/igraph_distances.c`: Unchanged (100/148) - the remaining diff is from other changes in benchmarks.
- `tests/unit/igraph_distances_johnson.c`: Unchanged (45/17) - this test has other changes pending from later entries (likely the `IGRAPH_ENEGCYCLE` error code change).
