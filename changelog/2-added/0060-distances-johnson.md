# igraph_distances_johnson()

`igraph_distances_johnson()` now takes an `igraph_neimode_t mode` parameter to determine in which direction paths should be followed.

---

**Original changelog wording:**

> `igraph_distances_johnson()` now takes an `igraph_neimode_t mode` parameter to determine in which direction paths should be followed.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0060-distances-johnson.md
```

Notes on remaining differences:
- The `mode` parameter for `igraph_distances_johnson()` was already ported as part of an earlier NFC entry. No additional code changes needed.
