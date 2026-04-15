# igraph_attribute_handler_t

**Category**: Attribute handling

`igraph_attribute_handler_t` members that formerly took an untyped `igraph_vector_ptr_t` argument are now taking a typed `igraph_attribute_record_list_t` argument instead.

---

**Original changelog wording:**

> `igraph_attribute_handler_t` members that formerly took an untyped `igraph_vector_ptr_t` argument are now taking a typed `igraph_attribute_record_list_t` argument instead.

---

**Proof of work (`git diff --numstat HEAD..next`):**

```
Before:  1452 files changed, 81828 insertions(+), 21956 deletions(-)
After:   1441 files changed, 79543 insertions(+), 18535 deletions(-)

add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0320-attribute-handler-t.md
   0     0    20    10  examples/simple/igraph_write_graph_pajek.out
 223   151   157   148  include/igraph_attributes.h
  46    30    32    24  include/igraph_interface.h
  10     9     3     8  include/igraph_pmt.h
   5    30     5    23  include/igraph_sparsemat.h
  12    21    12    23  include/igraph_strvector.h
 472   444   472   441  interfaces/functions.yaml
  44    45    43    44  interfaces/types.yaml
  31   341     0    39  src/core/sparsemat.c
  62    66    62    87  src/core/strvector.c
  35     2     1     2  src/core/typed_list.pmt
 614    23     2     8  src/graph/attributes.c
  19    23     4    17  src/graph/attributes.h
 810  2417     2     2  src/graph/cattributes.c
 223   134   209   127  src/graph/type_indexededgelist.c
  13    22     4    14  src/hrg/hrg.cc
   2     2     0     0  src/io/dl-parser.y
  23    19     0     0  src/io/dl.c
   2     2     0     0  src/io/gml-parser.y
  80   110     0     0  src/io/gml.c
 144   283     0     0  src/io/graphml.c
   3     3     0     0  src/io/lgl-parser.y
  30    25     2     2  src/io/lgl.c
   3     3     0     0  src/io/ncol-parser.y
  29    25     2     2  src/io/ncol.c
 162    82     0     0  src/io/pajek-parser.y
  25    76     7     7  src/io/pajek.c
   0     0     0    83  tests/regression/pajek_bipartite2.out
   0     0     0    56  tests/regression/pajek_signed.out
  20    21     0     0  tests/unit/cattributes6.c
  99    99     0     0  tests/unit/cattributes6.out
  32    40     0     0  tests/unit/constructor-failure.c
  30    30     0     0  tests/unit/pajek_bipartite2.out
  10    10     0     0  tests/unit/pajek_signed.out
```

Remaining differences explained:
- `examples/simple/igraph_write_graph_pajek.out`: Expected output changed due to pajek parser no longer generating `id` attribute (20 add-a / 10 del-a remaining is from unrelated later changes)
- `include/igraph_sparsemat.h`, `src/core/sparsemat.c`: Residual diff from `igraph_sparsemat` removal (later entries); `igraph_sparsemat_view` and `igraph_sparsemat_copy` kept
- `include/igraph_strvector.h`, `src/core/strvector.c`: `igraph_strvector_update` added as prerequisite; residual diff from later entries
- `include/igraph_pmt.h`, `src/core/typed_list.pmt`: Residual from typed list additions not yet ported (later entries)
- `include/igraph_attributes.h`: Residual from entries 0350 (IGRAPH_ATTRIBUTE_DEFAULT), 0360 (record struct further changes)
- `src/graph/type_indexededgelist.c`: Residual from later API changes
- `src/io/lgl.c`, `src/io/ncol.c`, `src/io/pajek.c`: Small residual from `gettype` -> `get_type` rename (entry 0330)
- `src/graph/attributes.h`: Residual from `gettype` -> `get_type` and later macro changes
- `src/hrg/hrg.cc`: Residual from unrelated API changes on next
- `tests/regression/pajek_*.out`: New expected output files; residual diff is from later test changes
- `interfaces/functions.yaml`, `interfaces/types.yaml`: ATTRIBUTES CTYPE change and `igraph_weighted_sparsemat` removal; residual from later `FLAGS: no_rng` additions
