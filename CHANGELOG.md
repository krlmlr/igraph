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

