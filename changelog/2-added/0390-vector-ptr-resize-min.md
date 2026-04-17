# igraph_vector_ptr_resize_min()

`igraph_vector_ptr_resize_min()` deallocates unused capacity of a pointer vector.

---

**Original changelog wording:**

> `igraph_vector_ptr_resize_min()` deallocates unused capacity of a pointer vector.

## Proof of work: `git diff --numstat HEAD..next` for modified files

```
BEFORE                   AFTER
add  del  file           add  del  file
  9    0  changelog/...0390-*.md                        (matches next)
  7   14  include/igraph_vector_ptr.h      15    7  include/igraph_vector_ptr.h
 37   29  src/core/vector_ptr.c            62   37  src/core/vector_ptr.c
```

### Remaining differences explained

- `include/igraph_vector_ptr.h` (15+/7-): Copyright header, __BEGIN_DECLS — unrelated.
- `src/core/vector_ptr.c` (62+/37-): Function placed at different position (after capacity vs before size on next), copyright header, igraph_vector_ptr_reserve doc comment changes — unrelated. Increase in diff is due to positional discrepancy; function content matches next exactly.
