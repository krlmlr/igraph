# igraph C library changelog

## Non-functional changes

This section lists API-breaking changes and other non-functional improvements, and provides guidance on adapting code written for igraph 0.10.x.

### Build system and compiler

- igraph now requires a C++ compiler that supports the C++14 standard.
- Projects that depend on igraph must only include the `<igraph.h>` header. While an igraph installation includes several sub-headers, these are for organizational purposes only, and their contents may change without notice. Only `#include <igraph.h>` is supported.

