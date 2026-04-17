# name

**Category**: Foreign formats

The Pajek format reader and writer now map vertex labels to the `name` vertex attribute in igraph. The `id` attribute is no longer used.

---

**Original changelog wording:**

> The Pajek format reader and writer now map vertex labels to the `name` vertex attribute in igraph. The `id` attribute is no longer used.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0830-the-pajek-format-reader-and-writer-now-map-vertex.md
```

Notes on remaining differences:
- `changelog/1-nfc/0830-the-pajek-format-reader-and-writer-now-map-vertex.md`: Fully resolved (11→0). The code change (mapping vertex labels to `name` instead of `id`) was already present on main-dev. Only the changelog file was missing.
