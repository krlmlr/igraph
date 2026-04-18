# igraph_rewire()

`igraph_rewire()` now takes an optional `igraph_rewiring_stats_t *` output argument. You can pass the appropriate struct there to find out the number of successful swaps during the rewiring operation.

---

**Original changelog wording:**

> `igraph_rewire()` now takes an optional `igraph_rewiring_stats_t *` output argument. You can pass the appropriate struct there to find out the number of successful swaps during the rewiring operation.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0400-rewire.md
```

Notes on remaining differences:
- `igraph_rewire()` with `igraph_rewiring_stats_t` was already fully ported to main-dev
- Only the changelog entry was missing
