# igraph_permute_vertices() and 3 others

**Category**: Core graph manipulation

As a consequence to the change in the semantics of the `igraph_permute_vertices()` permutation argument, the semantics of the permutations returned from `igraph_canonical_permutation()` and `igraph_canonical_permutation_bliss()` have also been inverted to maintain the invariant that the output of these functions can be fed into `igraph_permute_vertices()` directly.

---

**Original changelog wording:**

> As a consequence to the change in the semantics of the `igraph_permute_vertices()` permutation argument, the semantics of the permutations returned from `igraph_canonical_permutation()` and `igraph_canonical_permutation_bliss()` have also been inverted to maintain the invariant that the output of these functions can be fed into `igraph_permute_vertices()` directly.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0370-permute-vertices.md
  12    16     6    11  src/operators/permute.c
 154    19   136    23  src/isomorphism/bliss.cc
   5     2     1     1  tests/unit/igraph_isomorphic_vf2.c
  17     9     7     6  tests/unit/igraph_maximal_cliques.c
   9     6     5     5  examples/simple/igraph_isomorphic_vf2.c
```

Notes on remaining differences:
- `changelog/1-nfc/0370-permute-vertices.md`: 11→0 add, 0→0 del. Fully ported (the file now exists on main-dev). No remaining additions.
- `src/operators/permute.c`: 12→6 add, 16→11 del. Remaining diff is cosmetic (copyright header, license URL, include order, spacing) from later entries.
- `src/isomorphism/bliss.cc`: 154→136 add, 19→23 del. Remaining diff includes the rename to `_bliss` variants (entry 0680), new wrapper functions (entries 0660, 0670, 0680), and other unrelated changes. The increase in del (19→23) is because the static helper `igraph_i_canonical_permutation` on main-dev will be replaced by `igraph_i_canonical_permutation_bliss` on next; the 4 extra del lines account for the forward declaration and function signature differences that will be resolved when the rename happens.
- `tests/unit/igraph_isomorphic_vf2.c`: 5→1 add, 2→1 del. Remaining diff is a copyright header change.
- `tests/unit/igraph_maximal_cliques.c`: 17→7 add, 9→6 del. Remaining diff includes unrelated API changes (`IGRAPH_SIMPLE_SW`, `IGRAPH_UNLIMITED`, `RNG_INTEGER`, copyright header).
- `examples/simple/igraph_isomorphic_vf2.c`: 9→5 add, 6→5 del. Remaining diff includes unrelated changes (`igraph_setup()`, `igraph_int_t`, copyright header).
