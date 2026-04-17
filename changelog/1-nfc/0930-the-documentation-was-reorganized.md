# The documentation was reorganized.

**Category**: Documentation, performance, and vendor updates

The documentation was reorganized.

---

**Original changelog wording:**

> The documentation was reorganized.

---

## Proof of work: `git diff --numstat HEAD..next`

Before and after the change, side by side (add-before, del-before, add-after, del-after, file):

```
add-b  del-b  add-a  del-a  file
  11     0     0     0  changelog/1-nfc/0930-the-documentation-was-reorganized.md
   4     2     0     0  doc/CMakeLists.txt
  18     1     0     0  doc/attributes.xxml
  22     0     0     0  doc/basicigraph.xxml
   1     6     0     0  doc/bipartite.xxml
   1     0     0     0  doc/community.xxml
  10     3     0     0  doc/cycles.xxml
   1     1     0     0  doc/doxrox.py
   0     5     0     0  doc/foreign.xxml
  85     0     0     0  doc/games.xxml
  52    54     0     0  doc/generators.xxml
  20    16     0     0  doc/igraph-docs.xml
   9     0     0     0  doc/installation.xml
   2    14     0     0  doc/isomorphism.xxml
   0     7     0     0  doc/iterators.xxml
   0     0     0     0  doc/linalg.xxml
   0     6     0     0  doc/matrix.xxml
   0     4     0     0  doc/motifs.xxml
   3    11     0     0  doc/nongraph.xxml
   0     4     0     0  doc/operators.xxml
   0     0     0     0  doc/processes.xxml
   1     0     0     0  doc/progress.xxml
   0     8     0     0  doc/sparsemat.xxml
  32     0     0     0  doc/spatial.xxml
   3    28     0     0  doc/structural.xxml
   2     7     0     0  doc/strvector.xxml
  12     6     0     0  doc/tutorial.xml
   7    12     0     0  doc/vector.xxml
   1     0     0     0  doc/vectorlist.xxml
   0     5     0     0  doc/visitors.xxml
   0     0     0     0  doc/arpack.xxml
   0     0     0     0  doc/spatialgames.xxml
```

Notes on remaining differences:
- All documentation files fully ported (0/0 after). This includes the reorganization of content across files, file renames (arpack.xxml → linalg.xxml, spatialgames.xxml → processes.xxml), new files (games.xxml, spatial.xxml), and section restructuring.
- New doc files (spatial.xxml, games.xxml) include `doxrox-include` directives for functions that may be added in later entries; these are harmless as docs are not built in tests.
