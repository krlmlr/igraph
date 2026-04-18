# igraph_average_path_length() and 3 others

**Category**: Paths and cycles

The `weights` parameter of `igraph_average_path_length()`, `igraph_global_efficiency()`, `igraph_local_efficiency()` and `igraph_average_local_efficiency()` were moved to the second position, after the `graph` itself, for consistency with other functions.

---

**Original changelog wording:**

> The `weights` parameter of `igraph_average_path_length()`, `igraph_global_efficiency()`, `igraph_local_efficiency()` and `igraph_average_local_efficiency()` were moved to the second position, after the `graph` itself, for consistency with other functions.

---

**Proof of work** (`git diff --numstat HEAD..next`, before → after):

| Before +/- | After +/- | File |
|------------|-----------|------|
| 11/0 → | 0/0 | changelog/1-nfc/0580-average-path-length.md |
| 17/10 → | 15/8 | fuzzing/centrality.cpp |
| 20/11 → | 18/9 | fuzzing/weighted_centrality.cpp |
| 63/97 → | 51/87 | include/igraph_paths.h |
| 435/396 → | 434/395 | interfaces/functions.yaml |
| 24/27 → | 8/10 | src/paths/shortest_paths.c |
| 22/23 → | 1/1 | tests/unit/efficiency.c |

Remaining differences in modified files are due to unrelated changes on `next`
(e.g. header/copyright cleanup, `igraph_neighbors`/`igraph_incident` extra params,
`igraph_get_shortest_path` weights param, `igraph_distances` signature, betweenness/
pagerank changes, `EDGEWEIGHTS`→`EDGE_WEIGHTS` rename, `FLAGS: no_rng`, etc.).
