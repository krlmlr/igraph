# igraph_vector_ptr_capacity()

`igraph_vector_ptr_capacity()` returns the allocated capacity of a pointer vector.

---

**Original changelog wording:**

> `igraph_vector_ptr_capacity()` returns the allocated capacity of a pointer vector.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0380-vector-ptr-capacity.md
```

Notes on remaining differences:
- `igraph_vector_ptr_capacity()` was already fully present on main-dev
- Only the changelog entry was missing
