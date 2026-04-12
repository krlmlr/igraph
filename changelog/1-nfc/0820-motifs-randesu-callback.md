# igraph_motifs_randesu_callback()

**Category**: Other network analysis

The `igraph_motifs_handler_t` callback type now takes a `const igraph_vector_int_t *vids` parameter. Previously this was not formally `const`, even though it was not allowed to modify `vids`. This affects uses of `igraph_motifs_randesu_callback()`.

---

**Original changelog wording:**

> The `igraph_motifs_handler_t` callback type now takes a `const igraph_vector_int_t *vids` parameter. Previously this was not formally `const`, even though it was not allowed to modify `vids`. This affects uses of `igraph_motifs_randesu_callback()`.
