# igraph_maximal_independent_sets()

`igraph_maximal_independent_sets()` received `min_size` and `max_size` parameters that control the range of independent set sizes that are returned.

---

**Original changelog wording:**

> `igraph_maximal_independent_sets()` received `min_size` and `max_size` parameters that control the range of independent set sizes that are returned.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0230-maximal-independent-sets.md
```

Notes on remaining differences:
- `changelog/2-added/0230-maximal-independent-sets.md`: Fully ported (9→0). The `min_size`/`max_size` parameters were already ported in earlier entries. This adds the dedicated changelog file.
