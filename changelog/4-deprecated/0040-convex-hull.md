# igraph_convex_hull(), igraph_convex_hull_2d()

The deprecated `igraph_convex_hull()` was removed. Use `igraph_convex_hull_2d()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_convex_hull()` was removed. Use `igraph_convex_hull_2d()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0040-convex-hull.md
   2    40     2     5  src/misc/other.c
   5    27     5    23  include/igraph_nongraph.h
```

Notes on remaining differences:
- `src/misc/other.c`: Remaining 2/5 are copyright header NFC changes.
- `include/igraph_nongraph.h`: Remaining 5/23 are from other entries (copyright, `__BEGIN_DECLS`/`__END_DECLS`, `igraph_zeroin` removal).
- Changelog fully ported (0/0 after).
