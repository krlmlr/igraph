# igraph_incident(), igraph_es_incident(), igraph_inclist_init()

`igraph_incident()` and `igraph_es_incident()` gained an extra `igraph_loops_t loops` argument to specify what to do with loop edges. This makes their interfaces consistent with `igraph_inclist_init()`. Use `loops = IGRAPH_LOOPS_TWICE` to reproduce the previous behavior.

---

**Original changelog wording:**

> `igraph_incident()` and `igraph_es_incident()` gained an extra `igraph_loops_t loops` argument to specify what to do with loop edges. This makes their interfaces consistent with `igraph_inclist_init()`. Use `loops = IGRAPH_LOOPS_TWICE` to reproduce the previous behavior.
