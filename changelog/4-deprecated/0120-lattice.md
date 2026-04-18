# igraph_lattice(), igraph_square_lattice()

The deprecated `igraph_lattice()` was removed. Use `igraph_square_lattice()` instead.

---

**Original changelog wording:**

> The deprecated `igraph_lattice()` was removed. Use `igraph_square_lattice()` instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0120-lattice.md
   1    28     1     5  src/constructors/regular.c
   7    14     7    12  include/igraph_constructors.h
```

Notes on remaining differences:
- `src/constructors/regular.c`: del reduced 28→5. Remaining are copyright/comment header changes.
- `include/igraph_constructors.h`: del reduced 14→12. Remaining are copyright/license header changes and other declaration removals.
