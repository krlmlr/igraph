# igraph_adjacent_triangles(), igraph_count_adjacent_triangles()

The deprecated `igraph_adjacent_triangles()` was removed. Use `igraph_count_adjacent_triangles()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_adjacent_triangles()` was removed. Use `igraph_count_adjacent_triangles()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0080-adjacent-triangles.md
   4    28     3     5  src/properties/triangles.c
   7    16     7    12  include/igraph_motifs.h
```

Notes on remaining differences:
- `src/properties/triangles.c`: del reduced 28→5. Remaining 3 add / 5 del are copyright/comment header changes and an `igraph_vector_int_order1` → `igraph_i_vector_int_order` rename from another entry.
- `include/igraph_motifs.h`: del reduced 16→12. Remaining diffs are copyright/license header changes, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, `void*` → `void *` formatting, and `const igraph_vs_t` → `igraph_vs_t` parameter change (all belong to other entries).
