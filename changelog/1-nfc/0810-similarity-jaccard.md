# igraph_similarity_jaccard(), igraph_similarity_dice()

**Category**: Other network analysis

`igraph_similarity_jaccard()` and `igraph_similarity_dice()` now take two sets of vertices (`to` and `from` parameters) to create vertex pairs of, instead of one. Pass the same vertex set to both parameters to recover the previous behaviour.

---

**Original changelog wording:**

> `igraph_similarity_jaccard()` and `igraph_similarity_dice()` now take two sets of vertices (`to` and `from` parameters) to create vertex pairs of, instead of one. Pass the same vertex set to both parameters to recover the previous behaviour.
