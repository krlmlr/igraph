# igraph_barabasi_game() and 3 others

**Category**: Graph generators

`igraph_barabasi_game()`, `igraph_barabasi_aging_game()`, `igraph_recent_degree_game()` and `igraph_recent_degree_aging_game()` no longer interprets an empty `outseq` vector as a missing out-degree sequence. Pass `NULL` if you don't wish to specify an out-degree sequence.

---

**Original changelog wording:**

> `igraph_barabasi_game()`, `igraph_barabasi_aging_game()`, `igraph_recent_degree_game()` and `igraph_recent_degree_aging_game()` no longer interprets an empty `outseq` vector as a missing out-degree sequence. Pass `NULL` if you don't wish to specify an out-degree sequence.
