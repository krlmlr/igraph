# igraph_rewire()

**Category**: Graph generators

`igraph_rewire()` now takes an `igraph_edge_type_sw_t allowed_edge_types` parameter to specify whether to create self-loops. The `igraph_rewiring_t` enum type was removed. Instead of the old `IGRAPH_REWIRING_SIMPLE`, use `IGRAPH_SIMPLE_SW`. Instead of the old `IGRAPH_REWIRING_SIMPLE_LOOPS`, use `IGRAPH_LOOPS_SW`.

---

**Original changelog wording:**

> `igraph_rewire()` now takes an `igraph_edge_type_sw_t allowed_edge_types` parameter to specify whether to create self-loops. The `igraph_rewiring_t` enum type was removed. Instead of the old `IGRAPH_REWIRING_SIMPLE`, use `IGRAPH_SIMPLE_SW`. Instead of the old `IGRAPH_REWIRING_SIMPLE_LOOPS`, use `IGRAPH_LOOPS_SW`.
