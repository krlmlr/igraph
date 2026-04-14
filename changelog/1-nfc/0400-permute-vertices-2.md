# igraph_permute_vertices(), igraph_topological_sorting(), igraph_permute_vertices()

**Category**: Core graph manipulation

The semantics of the `igraph_permute_vertices()` permutation argument has changed: the i-th element of the vector now contains the index of the _original_ vertex that will be mapped to the i-th vertex in the new graph. This is now consistent with how other igraph functions treat permutations and vertex index vectors; for instance, you can now pass the result of `igraph_topological_sorting()` directly to `igraph_permute_vertices()` to obtain a new graph where the vertices are sorted topologically.

---

**Original changelog wording:**

> The semantics of the `igraph_permute_vertices()` permutation argument has changed: the i-th element of the vector now contains the index of the _original_ vertex that will be mapped to the i-th vertex in the new graph. This is now consistent with how other igraph functions treat permutations and vertex index vectors; for instance, you can now pass the result of `igraph_topological_sorting()` directly to `igraph_permute_vertices()` to obtain a new graph where the vertices are sorted topologically.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0400-permute-vertices-2.md
  18    18    17    17  src/flow/st-cuts.c
```

Notes on remaining differences:
- `src/flow/st-cuts.c` (17 add / 17 del remaining): The remaining differences belong to other changelog entries: license header NFC ("IGraph library." → "igraph library.", emacs mode comment removal), `igraph_cycles.h` include addition, `igraph_isomorphism.h` removal, `IGRAPH_I_ATTRIBUTE_COPY` macro → `igraph_i_attribute_copy()` function change, `igraph_neighbors()` signature extension with loop/multi parameters, comment indentation NFC, and `igraph_vector_int_push_back` wrapped in `IGRAPH_CHECK`.
