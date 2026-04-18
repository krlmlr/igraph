# Header guards renamed to `IGRAPH_{BEGIN,END}_C_DECLS`

The helper macros `__BEGIN_DECLS` / `__END_DECLS` that wrap
`extern "C" { ... }` in public and internal igraph headers were
renamed to `IGRAPH_BEGIN_C_DECLS` / `IGRAPH_END_C_DECLS`. Identifiers
beginning with two underscores are reserved for the C/C++
implementation (system headers frequently define `__BEGIN_DECLS`
differently on different platforms), so the new names avoid any
potential clash.

The rename touches 115 public and internal headers/source files
under `include/` and `src/`, plus the definition in
`include/igraph_decls.h` itself (which now only defines
`IGRAPH_BEGIN_C_DECLS` / `IGRAPH_END_C_DECLS`). Vendored libraries
under `vendor/plfit/` still use `__BEGIN_DECLS` internally via
their own independent `plfit_decls.h`; they are unaffected.

This is a pure source-level rename; the ABI and behaviour of every
exported igraph function are unchanged.
