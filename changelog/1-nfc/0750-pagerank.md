# igraph_pagerank(), igraph_personalized_pagerank(), igraph_personalized_pagerank_vs()

**Category**: Centralities

`igraph_pagerank()`, `igraph_personalized_pagerank()` and `igraph_personalized_pagerank_vs()` had their parameter ordering standardized.

---

**Original changelog wording:**

> `igraph_pagerank()`, `igraph_personalized_pagerank()` and `igraph_personalized_pagerank_vs()` had their parameter ordering standardized.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0750-pagerank.md
  40    50    16    32  include/igraph_centrality.h
  72    68     6     9  src/centrality/pagerank.c
 396   377   386   369  interfaces/functions.yaml
  73    74     1     2  tests/unit/igraph_pagerank.c
   6     3     3     0  examples/simple/igraph_pagerank.c
  15     8    13     7  fuzzing/centrality.cpp
  18     9    16     8  fuzzing/weighted_centrality.cpp
  37    19     1     1  tests/benchmarks/igraph_pagerank.c
  37    19     1     1  tests/benchmarks/igraph_pagerank_weighted.c
```

Notes on remaining differences:
- `changelog/1-nfc/0750-pagerank.md`: Fully resolved (11→0 add). The proof-of-work section added here causes the `del` to stay at 0 since `next` doesn't have it.
- `include/igraph_centrality.h`: Remaining diff (16 add, 32 del) is from other entries (copyright header, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, `const igraph_vs_t`→`igraph_vs_t`, deprecated function removal, formatting changes).
- `src/centrality/pagerank.c`: Remaining diff (6 add, 9 del) is from other entries (copyright header whitespace, blank line removals, comment typo fix).
- `interfaces/functions.yaml`: Remaining diff (386 add, 369 del) is from other entries (EDGEWEIGHTS→EDGE_WEIGHTS rename and many other function parameter reorderings).
- `tests/unit/igraph_pagerank.c`: Nearly fully resolved (73→1 add, 74→2 del). Remaining diff is copyright header change.
- `examples/simple/igraph_pagerank.c`: Remaining (3 add, 0 del) is from other entries (`igraph_setup()` call addition).
- `fuzzing/centrality.cpp`, `fuzzing/weighted_centrality.cpp`: Remaining diffs from other entries (betweenness_cutoff, betweenness_subset parameter changes, copyright header).
- `tests/benchmarks/igraph_pagerank.c`, `tests/benchmarks/igraph_pagerank_weighted.c`: Nearly fully resolved (37→1 each). Remaining diff is copyright header.
