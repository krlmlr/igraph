# igraph_cliques() and 6 others

`igraph_cliques()`, `igraph_weighed_cliques()`, `igraph_maximal_cliques()`, `igraph_maximal_cliques_file()`, `igraph_maximal_cliques_subset()`, `igraph_independent_sets()` and `igraph_maximal_independent_sets()` received a `max_results` parameter to limit the number of returned results. Pass `1` to return a single result, or `IGRAPH_UNLIMITED` to return all results.

---

**Original changelog wording:**

> `igraph_cliques()`, `igraph_weighed_cliques()`, `igraph_maximal_cliques()`, `igraph_maximal_cliques_file()`, `igraph_maximal_cliques_subset()`, `igraph_independent_sets()` and `igraph_maximal_independent_sets()` received a `max_results` parameter to limit the number of returned results. Pass `1` to return a single result, or `IGRAPH_UNLIMITED` to return all results.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0220-cliques.md
```

Notes on remaining differences:
- `changelog/2-added/0220-cliques.md`: Fully ported (9→0 additions remaining). The `max_results` parameter was already ported as part of earlier entries (0030, 0050). This entry adds only the dedicated changelog file.
