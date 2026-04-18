# igraph_neighbors(), igraph_vs_adj(), igraph_adjlist_init()

`igraph_neighbors()` and `igraph_vs_adj()` gained two extra arguments, `igraph_loops_t loops` and `igraph_bool_t multiple` to specify what to do with loop and multiple edges. This makes their interfaces consistent with `igraph_adjlist_init()`. Use `loops = IGRAPH_LOOPS_TWICE` and `multiple = true` to reproduce the previous behavior.

---

**Original changelog wording:**

> `igraph_neighbors()` and `igraph_vs_adj()` gained two extra arguments, `igraph_loops_t loops` and `igraph_bool_t multiple` to specify what to do with loop and multiple edges. This makes their interfaces consistent with `igraph_adjlist_init()`. Use `loops = IGRAPH_LOOPS_TWICE` and `multiple = true` to reproduce the previous behavior.
