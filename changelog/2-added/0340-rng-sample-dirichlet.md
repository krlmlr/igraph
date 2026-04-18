# igraph_rng_sample_dirichlet(), igraph_rng_sample_sphere_volume(), igraph_rng_sample_sphere_surface()

`igraph_rng_sample_dirichlet()`, `igraph_rng_sample_sphere_volume()` and `igraph_rng_sample_sphere_surface()` samples vectors from a Dirichlet distribution or from the volume or surface of a sphere while allowing the user to specify the random number generator to use.

---

**Original changelog wording:**

> `igraph_rng_sample_dirichlet()`, `igraph_rng_sample_sphere_volume()` and `igraph_rng_sample_sphere_surface()` samples vectors from a Dirichlet distribution or from the volume or surface of a sphere while allowing the user to specify the random number generator to use.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0340-rng-sample-dirichlet.md
  45     0     2     2  include/igraph_sampling.h
   4     7     3     7  include/igraph.h
 192     0     0     0  src/random/sampling.c
  14    12    14    13  src/CMakeLists.txt
  12    16    10    16  tests/CMakeLists.txt
   0     0     0     0  tests/unit/igraph_rng_sample_dirichlet.c
   0     0     0     0  tests/unit/igraph_rng_sample_dirichlet.out
   0     0     0     0  tests/unit/igraph_rng_sample_sphere.c
```

Notes on remaining differences:
- `include/igraph_sampling.h`: 2 add / 2 del remaining because main-dev uses `__BEGIN_DECLS`/`__END_DECLS` while next uses `IGRAPH_BEGIN_C_DECLS`/`IGRAPH_END_C_DECLS`; will be resolved when that NFC rename is ported
- `include/igraph.h`: Remaining diff (3 add, 7 del) from other header changes and copyright updates
- `src/CMakeLists.txt`: Remaining diff (14 add, 13 del) from other file additions/removals across entries
- `tests/CMakeLists.txt`: Remaining diff (10 add, 16 del) from test renames in other entries
- `changelog/2-added/0340-rng-sample-dirichlet.md`: Went to 0 add since file now exists; proof-of-work section adds to del since next doesn't have it
- New source, test, and output files: 0/0 on both sides — identical to next
