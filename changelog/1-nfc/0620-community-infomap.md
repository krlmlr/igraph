# igraph_community_infomap()

**Category**: Community detection

`igraph_community_infomap()` parameter names were standardized: `e_weights` is now `edge_weights` and `v_weights` is now `vertex_weights`.

---

**Original changelog wording:**

> `igraph_community_infomap()` parameter names were standardized: `e_weights` is now `edge_weights` and `v_weights` is now `vertex_weights`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
11	0	-	-	changelog/1-nfc/0620-community-infomap.md
58	37	56	35	include/igraph_community.h
423	386	422	385	interfaces/functions.yaml
0	323	0	323	src/community/infomap/infomap.cc
105	61	105	61	tests/unit/igraph_community_infomap.c
```

Notes on remaining differences:
- `changelog/1-nfc/0620-community-infomap.md`: Gone from diff (was 11+/0-) — file now matches `next` except for this proof-of-work section (which increases del count since `next` doesn't have it).
- `include/igraph_community.h`: Decreased by 2+/2- — the two renamed parameters now match `next`.
- `interfaces/functions.yaml`: Decreased by 1+/1- — the parameter names and DEPS now match `next`.
- `src/community/infomap/infomap.cc`: Unchanged (0+/323-) — `next` deletes this entire file (replaced by `src/community/infomap.cpp`), so internal parameter renames don't affect the numstat.
- `tests/unit/igraph_community_infomap.c`: Unchanged (105+/61-) — remaining diff is from other changelog entries (regularization parameters, new test cases, style changes).
