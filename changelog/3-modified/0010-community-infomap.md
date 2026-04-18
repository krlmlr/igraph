# igraph_community_infomap()

The implementation of the Infomap algorithm behind `igraph_community_infomap()` has been updated with a more recent version (2.8.0). Isolated vertices are now supported.

---

**Original changelog wording:**

> The implementation of the Infomap algorithm behind `igraph_community_infomap()` has been updated with a more recent version (2.8.0). Isolated vertices are now supported.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/3-modified/0010-community-infomap.md
 275     0     0     0  src/community/infomap.cpp
   0   328     0     0  src/community/infomap/infomap.cc
   0   382     0     0  src/community/infomap/infomap_FlowGraph.cc
   0    81     0     0  src/community/infomap/infomap_FlowGraph.h
   0   520     0     0  src/community/infomap/infomap_Greedy.cc
   0    74     0     0  src/community/infomap/infomap_Greedy.h
   0    52     0     0  src/community/infomap/infomap_Node.h
  14    13    11    10  src/CMakeLists.txt
   1     0     0     0  vendor/CMakeLists.txt
   1     0     0     0  etc/cmake/features.cmake
  12     4     0     1  etc/cmake/dependencies.cmake
   1     0     1     1  src/config.h.in
   1     1     0     0  CMakeLists.txt
 105    62     0     0  tests/unit/igraph_community_infomap.c
  45     8     0     0  tests/unit/igraph_community_infomap.out
```

Notes on remaining differences:
- All infomap source files now show 0/0: old files deleted, new wrapper and vendor/infomap copied from next
- `src/CMakeLists.txt`: 11 add / 10 del remaining from other entries
- `etc/cmake/dependencies.cmake`: 0 add / 1 del remaining - minor whitespace
- `src/config.h.in`: 1 add / 1 del remaining from other config changes
- Test files: 0/0 - identical to next
