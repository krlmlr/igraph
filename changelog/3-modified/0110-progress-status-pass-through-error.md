# Progress and status handlers: pass handler errors through verbatim

`igraph_progress()`, `igraph_progressf()`, `igraph_status()` and
`igraph_statusf()` used to coerce any non-`IGRAPH_SUCCESS` error
code returned by the user-installed progress/status handler into
`IGRAPH_INTERRUPTED`. They now return the handler's error code
verbatim.

The companion macros `IGRAPH_PROGRESS()`, `IGRAPH_PROGRESSF()`,
`IGRAPH_STATUS()` and `IGRAPH_STATUSF()` are simplified to a plain
`IGRAPH_CHECK(...)` call, so they likewise propagate the handler's
actual error code (after freeing the caller's `IGRAPH_FINALLY`
allocations).

Custom handlers that relied on `IGRAPH_INTERRUPTED` always being
the return value can now inspect the actual error code to
distinguish, e.g. `IGRAPH_INTERRUPTED` from a user-defined code
indicating a non-interruption failure.
