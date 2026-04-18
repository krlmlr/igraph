# igraph_rng_get_dirichlet()

The deprecated `igraph_rng_get_dirichlet()` function was removed.

---

**Original changelog wording:**

> The deprecated `igraph_rng_get_dirichlet()` function was removed.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   6     14     7     12  include/igraph_random.h
  11     45    11     16  src/random/random.c
```

Notes on remaining differences:
- `include/igraph_random.h`: del reduced 14→12 (2 lines for declaration + blank line). add increased 6→7 from context shift. Remaining diff is from other changelog entries (copyright/license header, `__BEGIN_DECLS`/`__END_DECLS` changes, other function changes).
- `src/random/random.c`: del reduced 45→16 (29 lines: function body). Remaining diff (11 add, 16 del) is from other changelog entries (copyright/header changes, other deprecated function removals).
