# igraph_attribute_record_t

**Category**: Attribute handling

The `value` member of `igraph_attribute_record_t` is now a union that can be used to formally treat the associated pointer as an `igraph_vector_t *`, `igraph_strvector_t *` or `igraph_vector_bool_t *`.

---

**Original changelog wording:**

> The `value` member of `igraph_attribute_record_t` is now a union that can be used to formally treat the associated pointer as an `igraph_vector_t *`, `igraph_strvector_t *` or `igraph_vector_bool_t *`.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0360-attribute-record-t.md
 123   123    98   123  include/igraph_attributes.h
```

Notes on remaining differences:
- `changelog/1-nfc/0360-attribute-record-t.md`: Fully ported (0/0 remaining). The proof-of-work section we appended does not appear in the diff because `next` doesn't have it — this is expected.
- `include/igraph_attributes.h`: Remaining 98 add / 123 del are unrelated changes: copyright header updates, `__BEGIN_DECLS` → `IGRAPH_BEGIN_C_DECLS`, reformatted `igraph_attribute_type_t` enum, moved `igraph_attribute_elemtype_t` enum, section header comments, documentation rewrites for other types (`igraph_attribute_table_t` members), removal of `igraph_i_set_attribute_table`, and `__END_DECLS` → `IGRAPH_END_C_DECLS`. These belong to other changelog entries.
