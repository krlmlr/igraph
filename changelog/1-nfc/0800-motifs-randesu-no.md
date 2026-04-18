# igraph_motifs_randesu_no(), igraph_motifs_randesu_estimate()

**Category**: Other network analysis

`igraph_motifs_randesu_no()` and `igraph_motifs_randesu_estimate()` now take an `igraph_real_t` as their `result` argument to prevent overflows when igraph is compiled with 32-bit integers.

---

**Original changelog wording:**

> `igraph_motifs_randesu_no()` and `igraph_motifs_randesu_estimate()` now take an `igraph_real_t` as their `result` argument to prevent overflows when igraph is compiled with 32-bit integers.
