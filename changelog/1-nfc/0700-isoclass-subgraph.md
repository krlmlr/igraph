# igraph_isoclass_subgraph(), igraph_vss_vector()

**Category**: Isomorphism functions and permutations

`igraph_isoclass_subgraph()` now takes a parameter of type `igraph_vs_t vids` instead of `igraph_vector_int_t vids`. Apply `igraph_vss_vector()` to the vector of vertex IDs to convert it to an `igraph_vs_t`.

---

**Original changelog wording:**

> `igraph_isoclass_subgraph()` now takes a parameter of type `igraph_vs_t vids` instead of `igraph_vector_int_t vids`. Apply `igraph_vss_vector()` to the vector of vertex IDs to convert it to an `igraph_vs_t`.
