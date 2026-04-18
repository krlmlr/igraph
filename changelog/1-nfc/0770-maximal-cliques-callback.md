# igraph_maximal_cliques_callback(), igraph_cliques_callback()

**Category**: Cliques and independent sets

`igraph_maximal_cliques_callback()` had its parameter ordering standardized: the `igraph_clique_handler_t *cliquehandler_fn, void *arg` parameter pair now comes at the end, making this function consistent with `igraph_cliques_callback()`.

---

**Original changelog wording:**

> `igraph_maximal_cliques_callback()` had its parameter ordering standardized: the `igraph_clique_handler_t *cliquehandler_fn, void *arg` parameter pair now comes at the end, making this function consistent with `igraph_cliques_callback()`.
