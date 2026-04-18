# igraph_vector_append(), igraph_strvector_append(), igraph_vector_ptr_append()

**Category**: Core data structures

`igraph_vector_append()`, `igraph_strvector_append()` and `igraph_vector_ptr_append()` now use a different allocation strategy: if the `to` vector has insufficient capacity, they double its capacity. Previously they reserved precisely as much capacity as needed for appending the `from` vector.

---

**Original changelog wording:**

> `igraph_vector_append()`, `igraph_strvector_append()` and `igraph_vector_ptr_append()` now use a different allocation strategy: if the `to` vector has insufficient capacity, they double its capacity. Previously they reserved precisely as much capacity as needed for appending the `from` vector.
