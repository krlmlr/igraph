# igraph_random_edge_walk(), igraph_random_walk()

The deprecated `igraph_random_edge_walk()` was removed. Its functionality is incorporated in `igraph_random_walk()`.

---

**Original changelog wording:**

> The deprecated `igraph_random_edge_walk()` was removed. Its functionality is incorporated in `igraph_random_walk()`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/4-deprecated/0020-random-edge-walk.md
   1    53     1     6  src/paths/random_walk.c
  23    60    23    50  include/igraph_paths.h
 304   346   304   340  interfaces/functions.yaml
```

Notes on remaining differences:
- `src/paths/random_walk.c`: Remaining 1/6 are copyright header NFC changes.
- `include/igraph_paths.h`: Remaining 23/50 are from other entries (copyright, `__BEGIN_DECLS`/`__END_DECLS`, other API changes).
- `interfaces/functions.yaml`: Remaining 304/340 from many other entries. The function definition was removed (6 lines less in del).
- Changelog fully ported (0/0 after).
