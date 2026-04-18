# igraph_sparsemat_view()

Removed `igraph_sparsemat_view()` as its design was broken and required the user to reach into the internals of `igraph_sparmsemat_t` to destroy it properly.

---

**Original changelog wording:**

> Removed `igraph_sparsemat_view()` as its design was broken and required the user to reach into the internals of `igraph_sparmsemat_t` to destroy it properly.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   5     14     5     11  include/igraph_sparsemat.h
  31     94    32     26  src/core/sparsemat.c
   0     47     -      -  tests/unit/igraph_sparsemat_view.c  (deleted)
   9     15     9     14  tests/CMakeLists.txt
```

Notes on remaining differences:
- `include/igraph_sparsemat.h`: del reduced 14→11 (3 lines for declaration). Remaining diff (5 add, 11 del) is from other changelog entries (copyright/license header, `__BEGIN_DECLS`/`__END_DECLS` changes).
- `src/core/sparsemat.c`: del reduced 94→26, add increased 31→32. Remaining diff is from other changelog entries (copyright/header, other deprecated function removals, code changes).
- `tests/unit/igraph_sparsemat_view.c`: fully deleted (47 lines).
- `tests/CMakeLists.txt`: del reduced 15→14 (1 line for test entry). Remaining diff is from other changelog entries.
