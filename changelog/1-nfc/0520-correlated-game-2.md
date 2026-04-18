# igraph_correlated_game(), igraph_correlated_pair_game(), igraph_permute_vertices()

**Category**: Graph generators

The semantics of the `permutation` argument of `igraph_correlated_game()` and `igraph_correlated_pair_game()` has changed: the i-th element of the vector now contains the index of the _original_ vertex that will be mapped to the i-th vertex in the new graph. This is consistent with how `igraph_permute_vertices()` operates (which has also changed in igraph 1.0).

---

**Original changelog wording:**

> The semantics of the `permutation` argument of `igraph_correlated_game()` and `igraph_correlated_pair_game()` has changed: the i-th element of the vector now contains the index of the _original_ vertex that will be mapped to the i-th vertex in the new graph. This is consistent with how `igraph_permute_vertices()` operates (which has also changed in igraph 1.0).
