# igraph_isomorphic_function_vf2(), igraph_get_isomorphisms_vf2_callback()

The deprecated `igraph_isomorphic_function_vf2()` was removed. Use `igraph_get_isomorphisms_vf2_callback()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_isomorphic_function_vf2()` was removed. Use `igraph_get_isomorphisms_vf2_callback()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0180-isomorphic-function-vf2.md
   2    43     2    23  src/isomorphism/vf2.c
  13    57    13    47  include/igraph_isomorphism.h
```

Notes on remaining differences:
- `src/isomorphism/vf2.c`: del reduced 43→23. Remaining are copyright/comment header changes and other deprecated function removals.
- `include/igraph_isomorphism.h`: del reduced 57→47. Remaining are copyright/license header changes, `__BEGIN_DECLS`/`__END_DECLS`, and other deprecated declaration removals.
