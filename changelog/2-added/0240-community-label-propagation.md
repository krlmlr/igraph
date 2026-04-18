# igraph_community_label_propagation()

`igraph_community_label_propagation()` gained the `igraph_lpa_variant_t lpa_variant` parameter to allow specification of label propagation algorithm (LPA) variants. A new fast label propagation variant was added. Set `lpa_variant=DOMINANCE` to select the algorithm used up to igraph 0.10.

---

**Original changelog wording:**

> `igraph_community_label_propagation()` gained the `igraph_lpa_variant_t lpa_variant` parameter to allow specification of label propagation algorithm (LPA) variants. A new fast label propagation variant was added. Set `lpa_variant=DOMINANCE` to select the algorithm used up to igraph 0.10.
