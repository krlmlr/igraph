# igraph_hub_and_authority_scores()

**Category**: Warnings and behavioral refinements

`igraph_hub_and_authority_scores()` now warns when a large fraction of centrality scores are zero, as this indicates a non-unique solution, and thus the returned result may not be meaningful.

---

**Original changelog wording:**

> `igraph_hub_and_authority_scores()` now warns when a large fraction of centrality scores are zero, as this indicates a non-unique solution, and thus the returned result may not be meaningful.
