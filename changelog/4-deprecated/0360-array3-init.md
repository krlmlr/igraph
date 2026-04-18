# igraph_array3_init(), igraph_array3_destroy()

The deprecated `igraph_array3_t` type and all associated functions (`igraph_array3_init()`, `igraph_array3_destroy()`, etc.) were removed, along with the `igraph_array.h` sub-header.

---

**Original changelog wording:**

> The deprecated `igraph_array3_t` type and all associated functions (`igraph_array3_init()`, `igraph_array3_destroy()`, etc.) were removed, along with the `igraph_array.h` sub-header.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
    9      0      -      -  changelog/4-deprecated/0360-array3-init.md
    3      6      3      5  include/igraph.h
    0     63      -      -  include/igraph_array.h
    0     54      -      -  include/igraph_array_pmt.h
   11      9     11      8  src/CMakeLists.txt
    0     50      -      -  src/core/array.c
    0    110      -      -  src/core/array.pmt
```

Notes on remaining differences:
- `changelog/4-deprecated/0360-array3-init.md`: Fully resolved. Proof-of-work section only present on main-dev.
- `include/igraph.h`: Deletions decreased 6→5. The 1-line decrease is the removed `#include "igraph_array.h"`. Remaining 3+/5- are copyright header updates — later entries.
- `include/igraph_array.h`, `include/igraph_array_pmt.h`, `src/core/array.c`, `src/core/array.pmt`: All fully resolved (files deleted on both branches).
- `src/CMakeLists.txt`: Deletions decreased 9→8. The 1-line decrease is the removed `core/array.c`. Remaining 11+/8- are from other source file additions/removals in later entries.
