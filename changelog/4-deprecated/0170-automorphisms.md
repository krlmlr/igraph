# igraph_automorphisms(), igraph_count_automorphisms(), igraph_count_automorphisms_bliss()

The deprecated `igraph_automorphisms()` was removed. Use `igraph_count_automorphisms()` or `igraph_count_automorphisms_bliss()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_automorphisms()` was removed. Use `igraph_count_automorphisms()` or `igraph_count_automorphisms_bliss()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0170-automorphisms.md
```

Notes on remaining differences:
- The function `igraph_automorphisms()` was already removed in a previous porting step. This entry only adds the changelog file to document the removal.
