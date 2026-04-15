# igraph_attribute_table_t

**Category**: Attribute handling

The `gettype` member of `igraph_attribute_table_t` was renamed to `get_type` for consistency with the naming scheme of other struct members.

---

**Original changelog wording:**

> The `gettype` member of `igraph_attribute_table_t` was renamed to `get_type` for consistency with the naming scheme of other struct members.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
11	0	-	-	changelog/1-nfc/0330-attribute-table-t.md
158	145	156	143	include/igraph_attributes.h
2	8	0	6	src/graph/attributes.c
4	17	3	16	src/graph/attributes.h
2	2	-	-	src/graph/cattributes.c
7	7	-	-	src/io/pajek.c
2	2	-	-	src/io/lgl.c
3	4	1	2	src/io/leda.c
2	2	-	-	src/io/ncol.c
```

Notes on remaining differences:
- `changelog/1-nfc/0330-attribute-table-t.md`: Fully resolved (- means no diff). Will show a small diff after adding this proof-of-work section, which is expected as next doesn't have it.
- `include/igraph_attributes.h`: Decreased by 2/2. Remaining 156/143 diff is from other changelog entries (doc reorganization, `__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS`, `IGRAPH_ATTRIBUTE_DEFAULT` removal, other struct member renames, etc.).
- `src/graph/attributes.c`: Decreased by 2/2. Remaining 0/6 is from removal of deprecated `igraph_i_set_attribute_table` wrapper in a later entry.
- `src/graph/attributes.h`: Decreased by 1/1. Remaining 3/16 is from macro changes (`__BEGIN_DECLS`, `IGRAPH_I_ATTRIBUTE_*` macros) in other entries.
- `src/graph/cattributes.c`, `src/io/pajek.c`, `src/io/lgl.c`, `src/io/ncol.c`: Fully resolved (no remaining diff for the `gettype` rename).
- `src/io/leda.c`: Decreased by 2/2. Remaining 1/2 is from other changes (header comment updates in later entries).
