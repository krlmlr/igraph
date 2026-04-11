# igraph C library changelog

## Non-functional changes

This section lists API-breaking changes and other non-functional improvements, and provides guidance on adapting code written for igraph 0.10.x.

### Build system and compiler

- igraph now requires a C++ compiler that supports the C++14 standard.
- Projects that depend on igraph must only include the `<igraph.h>` header. While an igraph installation includes several sub-headers, these are for organizational purposes only, and their contents may change without notice. Only `#include <igraph.h>` is supported.

### Core infrastructure

- `IGRAPH_EINVEVECTOR` error code was removed in favour of `IGRAPH_EINVAL`.
- `IGRAPH_NONSQUARE` error code was removed in favour of `IGRAPH_EINVAL`. The numeric value 8 is now used by `IGRAPH_EINVEID`.
- `IGRAPH_EGLP` and all `IGRAPH_GLP_*` error codes were removed in favour of `IGRAPH_FAILURE`.
- `IGRAPH_ELAPACK` error code was removed in favour of `IGRAPH_FAILURE`.
- `IGRAPH_CPUTIME` error code was removed in favour of the interruption mechanism.
- `IGRAPH_EDIVZERO` error code was removed in favour of `IGRAPH_EINVAL`.
- `IGRAPH_EATTRIBUTES` error code was removed in favour of `IGRAPH_EINTERNAL`.
- `IGRAPH_ENEGLOOP`, a deprecated alias of `IGRAPH_ENEGCYCLE`, was removed.
- All `IGRAPH_ARPACK_*` error codes have been replaced by the single `IGRAPH_EARPACK` error code. The previous `IGRAPH_ARPACK_*` codes have been moved to the new `igraph_arpack_error_t` enum. Use `igraph_arpack_get_last_error()` to retrieve the specific ARPACK error code.
- `IGRAPH_EINVEID` was added for invalid edge IDs, analogous to `IGRAPH_EINVVID`.
- The interruption handler type (`igraph_interruption_handler_t`) no longer takes a `void*` parameter and now returns `igraph_bool_t` instead of `igraph_error_t`. Correspondingly, `igraph_allow_interruption()` no longer takes a `void*` parameter.
- Added `igraph_setup()` function to initialize the igraph library with a random seed.

### Random number generation

- `igraph_rng_set_default()` now returns a pointer to the previous default RNG. Furthermore, this function now only stores a pointer to the `igraph_rng_t` struct passed to it, instead of copying the struct. Thus the `igraph_rng_t` object must continue to exist for as long as it is used as the default RNG.
- The `RNG_BEGIN()` and `RNG_END()` macros were removed. You are now responsible for seeding the RNG before using any igraph function that may use random numbers by calling `igraph_rng_seed(igraph_rng_default(), ...)`, or by simply ensuring that `igraph_setup()` was called before the first use of the library.

## Remaining differences from the `next` branch (proof of work)

The following differences remain in the files changed by this PR compared to the `next` branch. Each difference is justified by a later changelog entry that has not yet been implemented.

### `igraph_integer_t` → `igraph_int_t` rename (later "Core types and naming" changelog entry)

Affects: `include/igraph_arpack.h`, `src/linalg/arpack.c`, `src/constructors/basic_constructors.c`, `src/constructors/adjacency.c`, `src/core/sparsemat.c`, `src/games/sbm.c`, `src/graph/type_indexededgelist.c`, `src/linalg/lapack.c`, `src/linalg/eigen.c`, `src/misc/bipartite.c`, `src/isomorphism/lad.c`, `src/isomorphism/bliss.cc`, `src/community/leading_eigenvector.c`, `src/core/interruption.h`, `src/graph/iterators.c`, and many other files

### `__BEGIN_DECLS`/`__END_DECLS` → `IGRAPH_BEGIN_C_DECLS`/`IGRAPH_END_C_DECLS` (later macro cleanup)

Affects: `include/igraph_error.h`, `include/igraph_arpack.h`, `include/igraph_interrupt.h`, `include/igraph_setup.h`, `include/igraph_random.h`, `src/core/interruption.h`, `src/internal/glpk_support.h`

### Copyright header modernization (later cosmetic changes)

Affects: all files — `/* IGraph library */` → `/* igraph library */`, address removal, license URL update

### `void *attr` → `const igraph_attribute_record_list_t *attr` (later "Attribute handler" changes)

Affects: `src/graph/type_indexededgelist.c` (`igraph_empty_attrs`, `igraph_add_edges`, `igraph_add_vertices`)

### `igraph_topology.h` → `igraph_isomorphism.h` (later header reorganization)

Affects: `src/isomorphism/lad.c`, `src/isomorphism/bliss.cc`

### Documentation improvements (later doc changes)

Affects: `src/games/sbm.c` (SBM doc expansion), `src/linalg/lapack.c` (non-square matrix error messages), `src/misc/bipartite.c` (parameter descriptions), `src/isomorphism/bliss.cc` (canonical permutation doc)

### `igraph_vector_view` API change (later core data structure changes)

Affects: `src/linalg/eigen.c`

### Removal of deprecated functions (later deprecation cleanup)

Affects: `src/core/sparsemat.c` (`igraph_sparsemat_copy` removal), `src/constructors/basic_constructors.c` (`about_generators` section removal), `src/graph/iterators.c` (`igraph_vs_seq` removal)

### Directed graph `IGRAPH_LOOPS_TWICE` → `IGRAPH_LOOPS_ONCE` conversion (later adjacency/graph behavior changes)

Affects: `src/constructors/adjacency.c`, `src/graph/type_indexededgelist.c`

### SBM game edge type handling changes (later game function refactoring)

Affects: `src/games/sbm.c`, `tests/unit/igraph_sbm_game.c`

### Bipartite game function changes (later bipartite function refactoring)

Affects: `src/misc/bipartite.c`

### `igraph_i_adjacency_directed` → `igraph_i_adjacency_directed_or_plus` (later adjacency refactoring)

Affects: `src/constructors/adjacency.c`

### Test changes for new function signatures (later API changes)

Affects: `tests/unit/glpk_error.c` (erdos_renyi_game_gnm signature change), `tests/unit/igraph_adjacency.c`, `tests/unit/igraph_weighted_adjacency.c`

### `(size_t) index` cast in `igraph_arpack_error_to_string` (defensive coding)

Affects: `src/linalg/arpack.c` — our version has `(size_t) index < ...` while next has `index < ...`. This is a defensive cast we added to avoid a signed/unsigned comparison warning. Not present in next but is a correct safeguard.

### `igraph_rng_get_dirichlet()` deprecation removal (later deprecation cleanup)

Affects: `include/igraph_random.h`

### Additional RNG header differences (later macro and include cleanup)

Affects: `include/igraph_random.h` — `RNG_GAMMA` macro not yet added, `__BEGIN_DECLS`/`__END_DECLS` not yet replaced

### `stdbool.h` include addition (later cleanup)

Affects: `src/random/random.c`

