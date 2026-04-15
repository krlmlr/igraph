# Attribute table members that retrieve graph, vertex or edge attributes must n...

**Category**: Attribute handling

Attribute table members that retrieve graph, vertex or edge attributes must not clear the incoming result vector any more; results must be appended to the end of the provided result vector instead.

---

**Original changelog wording:**

> Attribute table members that retrieve graph, vertex or edge attributes must not clear the incoming result vector any more; results must be appended to the end of the provided result vector instead.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0340-attribute-table-members-that-retrieve-graph-verte.md
 156   143   123   124  include/igraph_attributes.h
```

Notes on remaining differences:
- `changelog/1-nfc/0340-attribute-table-members-that-retrieve-graph-verte.md`: Fully ported (0/0 remaining). The after `del` count will increase slightly due to the proof-of-work section added here which does not exist on `next`.
- `include/igraph_attributes.h`: Remaining 123 add / 124 del are from other changelog entries (copyright header changes, `__BEGIN_DECLS`/`IGRAPH_BEGIN_C_DECLS`, `igraph_attribute_type_t` enum reformatting, `igraph_attribute_elemtype_t` relocation, `igraph_attribute_record_t` documentation, other struct member documentation updates, removal of `igraph_i_set_attribute_table` declaration, section headers, etc.). The decrease of 33 additions and 19 deletions corresponds to the documentation changes for the 9 `get_*_*_attr` members and removal of the old conversion note paragraph.
