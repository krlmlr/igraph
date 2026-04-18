# igraph_incident(), igraph_es_incident(), igraph_inclist_init()

`igraph_incident()` and `igraph_es_incident()` gained an extra `igraph_loops_t loops` argument to specify what to do with loop edges. This makes their interfaces consistent with `igraph_inclist_init()`. Use `loops = IGRAPH_LOOPS_TWICE` to reproduce the previous behavior.

---

**Original changelog wording:**

> `igraph_incident()` and `igraph_es_incident()` gained an extra `igraph_loops_t loops` argument to specify what to do with loop edges. This makes their interfaces consistent with `igraph_inclist_init()`. Use `loops = IGRAPH_LOOPS_TWICE` to reproduce the previous behavior.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
   9     0     0     0  changelog/2-added/0330-incident.md
  37    28    36    26  src/graph/type_indexededgelist.c
  17    89    12    89  src/graph/iterators.c
  13    17    12    16  tests/CMakeLists.txt
   0     0     0     0  tests/unit/igraph_i_incident.c
   0     0     0     0  tests/unit/igraph_i_incident.out
   0     0     0     0  tests/unit/igraph_incident.c
   0     0     0     0  tests/unit/igraph_incident.out
```

Notes on remaining differences:
- `src/graph/type_indexededgelist.c`: Remaining diffs (36 add, 26 del) are from other changelog entries (formatting, memset, attribute macros, error message punctuation changes, etc.)
- `src/graph/iterators.c`: Remaining diffs (12 add, 89 del) are mostly from removal of deprecated `igraph_vs_seq`/`igraph_es_seq` functions and other entries
- `tests/CMakeLists.txt`: Remaining diff (12 add, 16 del) is from `igraph_i_neighbors` → `igraph_neighbors` rename (different entry)
- `changelog/2-added/0330-incident.md`: Went from 9 add → 0 add because the file now exists on main-dev; the proof-of-work section causes del to stay at 0 since next doesn't have it
- Test files show 0/0 in both before and after because the rename was applied identically
