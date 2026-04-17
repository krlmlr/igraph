# Qhull was vendored as a required dependency for spatial geometry computation ...

**Category**: Documentation, performance, and vendor updates

Qhull was vendored as a required dependency for spatial geometry computation functions (Delaunay triangulation, convex hull).

---

**Original changelog wording:**

> Qhull was vendored as a required dependency for spatial geometry computation functions (Delaunay triangulation, convex hull).

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0910-qhull-was-vendored-as-a-required-dependency-for-sp.md
   2     0     1     0  vendor/CMakeLists.txt
  12     0     0     0  vendor/qhull/CHANGES.md
  48     0     0     0  vendor/qhull/CMakeLists.txt
  39     0     0     0  vendor/qhull/COPYING.txt
 720     0     0     0  vendor/qhull/README.txt
  69     0     0     0  vendor/qhull/libqhull_r/accessors_r.c
2302     0     0     0  vendor/qhull/libqhull_r/geom2_r.c
1284     0     0     0  vendor/qhull/libqhull_r/geom_r.c
 189     0     0     0  vendor/qhull/libqhull_r/geom_r.h
2268     0     0     0  vendor/qhull/libqhull_r/global_r.c
4128     0     0     0  vendor/qhull/libqhull_r/io_r.c
 166     0     0     0  vendor/qhull/libqhull_r/io_r.h
1754     0     0     0  vendor/qhull/libqhull_r/libqhull_r.c
1281     0     0     0  vendor/qhull/libqhull_r/libqhull_r.h
 566     0     0     0  vendor/qhull/libqhull_r/mem_r.c
 235     0     0     0  vendor/qhull/libqhull_r/mem_r.h
5589     0     0     0  vendor/qhull/libqhull_r/merge_r.c
 238     0     0     0  vendor/qhull/libqhull_r/merge_r.h
3959     0     0     0  vendor/qhull/libqhull_r/poly2_r.c
1448     0     0     0  vendor/qhull/libqhull_r/poly_r.c
 310     0     0     0  vendor/qhull/libqhull_r/poly_r.h
 161     0     0     0  vendor/qhull/libqhull_r/qhull_ra.h
1383     0     0     0  vendor/qhull/libqhull_r/qset_r.c
 515     0     0     0  vendor/qhull/libqhull_r/qset_r.h
 249     0     0     0  vendor/qhull/libqhull_r/random_r.c
  41     0     0     0  vendor/qhull/libqhull_r/random_r.h
 854     0     0     0  vendor/qhull/libqhull_r/rboxlib_r.c
 727     0     0     0  vendor/qhull/libqhull_r/stat_r.c
 563     0     0     0  vendor/qhull/libqhull_r/stat_r.h
 617     0     0     0  vendor/qhull/libqhull_r/user_r.c
1061     0     0     0  vendor/qhull/libqhull_r/user_r.h
 102     0     0     0  vendor/qhull/libqhull_r/usermem_r.c
  68     0     0     0  vendor/qhull/libqhull_r/userprintf_r.c
  53     0     0     0  vendor/qhull/libqhull_r/userprintf_rbox_r.c
```

Notes on remaining differences:
- All `vendor/qhull/` files: Fully ported (all add counts dropped from their original values to 0).
- `vendor/CMakeLists.txt`: Remaining 1 add is the `add_subdirectory(infomap)` line from a later changelog entry.
- `changelog/1-nfc/0910-...`: Fully ported (11→0 add).
