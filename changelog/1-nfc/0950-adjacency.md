# igraph_adjacency(), igraph_weighted_adjacency()

**Category**: Documentation, performance, and vendor updates

Improved performance when creating graphs from dense adjacency matrices (`igraph_adjacency()` and `igraph_weighted_adjacency()`).

---

**Original changelog wording:**

> Improved performance when creating graphs from dense adjacency matrices (`igraph_adjacency()` and `igraph_weighted_adjacency()`).

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0950-adjacency.md
 241   142     0     0  src/constructors/adjacency.c
   7     7     0     0  tests/unit/igraph_adjacency.c
  19     4     0     0  tests/unit/igraph_adjacency.out
  13    22     0     0  tests/unit/igraph_weighted_adjacency.c
  85    92     0     0  tests/unit/igraph_weighted_adjacency.out
  39    27     0     0  tests/unit/test_utilities.c
   9     3     5     0  tests/unit/test_utilities.h
 100     0     0     0  tests/benchmarks/igraph_adjacency.c
  27    16    26    15  tests/CMakeLists.txt
   0     0     0     0  examples/simple/igraph_adjacency.c
  37    22     0     0  examples/simple/igraph_weighted_adjacency.c
   5     5     0     0  examples/simple/igraph_weighted_adjacency.out
```

Notes on remaining differences:
- All adjacency-related source, test, and example files fully ported (0/0 after).
- `tests/unit/test_utilities.h`: Remaining 5 add are unrelated doc comments for `print_matrix_format_indent` and `print_matrix_list` from other entries.
- `tests/CMakeLists.txt`: Remaining 26/15 are test/benchmark registrations for other changelog entries.
- This change also includes the closely intertwined behavioral change from `3-modified/0040-adjacency.md` (`IGRAPH_LOOPS_TWICE` treated as `IGRAPH_LOOPS_ONCE` for DIRECTED/UPPER/LOWER modes) as the performance improvements and behavioral changes cannot be cleanly separated in the code.
