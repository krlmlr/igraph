# igraph_rewire_edges()

**Category**: Graph generators

`igraph_rewire_edges()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and `multiple`.

---

**Original changelog wording:**

> `igraph_rewire_edges()` uses an `igraph_edge_type_sw_t allowed_edge_types` parameter instead of `loops` and `multiple`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0470-rewire-edges.md
  21    42    20    41  include/igraph_games.h
  13    19     5    13  src/operators/rewire_edges.c
   9    10     9    10  src/games/watts_strogatz.c
   5     4     4     3  tests/unit/coloring.c
 447   440   445   438  interfaces/functions.yaml
```

Notes on remaining differences:
- `changelog/1-nfc/0470-rewire-edges.md`: Fully ported (0/0 remaining). The proof-of-work section exists only on `main-dev`.
- `include/igraph_games.h`: Remaining differences (20/41) are unrelated changes (copyright header, `__BEGIN_DECLS`→`IGRAPH_BEGIN_C_DECLS`, other function signature changes from later entries like `igraph_watts_strogatz_game`, `igraph_static_fitness_game`, `igraph_sbm_game`, `igraph_correlated_game`, removed deprecated functions).
- `src/operators/rewire_edges.c`: Remaining differences (5/13) are unrelated NFC changes (vim modeline removal, copyright header, `igraph_vector_int_order1`→`igraph_i_vector_int_order` rename, `IGRAPH_I_ATTRIBUTE_COPY` macro→function call, blank line removals).
- `src/games/watts_strogatz.c`: Unchanged (9/10) because the `igraph_watts_strogatz_game` signature change is a separate entry (0560). The internal call was adapted to convert booleans to `igraph_edge_type_sw_t`.
- `tests/unit/coloring.c`: Remaining differences (4/3) are unrelated (copyright header, `igraph_lcf`→`igraph_lcf_small` rename, `igraph_bipartite_game_gnm` signature change).
- `interfaces/functions.yaml`: Remaining differences (445/438) are from many other function entries across the file.
