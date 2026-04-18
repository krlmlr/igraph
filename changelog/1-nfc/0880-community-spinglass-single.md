# igraph_community_spinglass_single()

**Category**: Bug fixes

`igraph_community_spinglass_single()` now uses `igraph_real_t` for its `inner_links` and `outer_links` output parameters, as these return not simply edge counts, but the sum of the weights of some edges. Thus these results are no longer incorrectly rounded.

---

**Original changelog wording:**

> `igraph_community_spinglass_single()` now uses `igraph_real_t` for its `inner_links` and `outer_links` output parameters, as these return not simply edge counts, but the sum of the weights of some edges. Thus these results are no longer incorrectly rounded.
