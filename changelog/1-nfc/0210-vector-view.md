# igraph_vector_view() and 3 others

**Category**: Core data structures

`igraph_vector_view()`, `igraph_matrix_view()`, `igraph_matrix_view_from_vector()`, and `igraph_vector_ptr_view()` now return their result as a return value instead of an output parameter. This allows assigning the value to a `const` variable without triggering warnings with modern compilers.

---

**Original changelog wording:**

> `igraph_vector_view()`, `igraph_matrix_view()`, `igraph_matrix_view_from_vector()`, and `igraph_vector_ptr_view()` now return their result as a return value instead of an output parameter. This allows assigning the value to a `const` variable without triggering warnings with modern compilers.
