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
  19    41    18    40  include/igraph_games.h
  13    19     5    13  src/operators/rewire_edges.c
   9    10     9    10  src/games/watts_strogatz.c
   5     4     4     3  tests/unit/coloring.c
 447   438   445   436  interfaces/functions.yaml
```

Notes on remaining differences:
- `src/games/watts_strogatz.c` (9/10 → 9/10, unchanged): `igraph_watts_strogatz_game()` still takes separate `loops` and `multiple` parameters (that signature change belongs to entry 0560). The updated call to `igraph_rewire_edges` uses an inline conversion `(multiple ? IGRAPH_MULTI_SW : ...) | (loops ? IGRAPH_LOOPS_SW : ...)` rather than `allowed_edge_types` directly, so the call-site diff persists until entry 0560 is ported.
- `include/igraph_games.h` (19/41 → 18/40): One line reduced; remaining diff is from other header-level changes (copyright, `__BEGIN_DECLS`, removed deprecated functions, etc.) belonging to later entries.
- `src/operators/rewire_edges.c` (13/19 → 5/13): Remaining diff consists of unrelated cleanup (`igraph_vector_int_order1` → `igraph_i_vector_int_order`, `IGRAPH_I_ATTRIBUTE_COPY/DESTROY` → `igraph_i_attribute_copy`) from later entries.
- `tests/unit/coloring.c` (5/4 → 4/3): Remaining diff is `igraph_lcf` → `igraph_lcf_small` (entry 0530) and `igraph_bipartite_game_gnm` change (entry 0420).
- `interfaces/functions.yaml` (447/438 → 445/436): Two lines reduced; the `igraph_watts_strogatz_game` params change (entry 0560) and other entries account for the remainder.
- The `del` counts for `changelog/1-nfc/0470-rewire-edges.md` increase from 0 to 0 (the proof-of-work section added here does not appear on `next`, so it shows as additional `del` when diffing HEAD→next; however since the file is new on main-dev and absent on next, it does not appear in the diff at all after porting).
