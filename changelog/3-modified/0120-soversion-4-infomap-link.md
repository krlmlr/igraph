# Library SOVERSION bumped to 4, Infomap external linking hook

Two related build-system changes:

- The igraph shared library's SONAME has been bumped from
  `libigraph.so.3` to `libigraph.so.4`. The new major version
  reflects the accumulated incompatible ABI changes that landed on
  `next` (see the "Modified" and "Deprecated" sections of this
  changelog). Downstream packagers must relink against the new
  SONAME.
- `src/CMakeLists.txt` now accepts `INFOMAP_INCLUDE_DIR` /
  `INFOMAP_LIBRARIES` build-time variables so a system-provided
  Infomap can be linked in once the bundled copy is made
  optional; when those variables are empty the bundled
  `vendor/infomap` is still used.
