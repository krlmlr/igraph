# Proof of Work: `git diff --numstat main next`

Each line from `git diff --numstat origin/main origin/next` is annotated with
the changelog entry tag it corresponds to.

## Legend

- **CHANGELOG** (2 files): Changelog files
- **VERSIONING-POLICY** (1 files): Explicit versioning policy
- **CONTRIBUTORS** (4 files): Contributor documentation
- **META** (3 files): Repository metadata
- **BUILD-CPP14** (1 files): C++14 requirement; compiler flags
- **BUILD-DEPS** (1 files): Dependency management
- **BUILD-CMAKE** (7 files): Build system changes
- **BUILD-CI** (2 files): CI configuration
- **VENDOR-QHULL** (33 files): Qhull vendored for spatial functions
- **VENDOR-INFOMAP** (54 files): Infomap updated to 2.8.0
- **VENDOR-NANOFLANN** (1 files): nanoflann updated to 1.9.0
- **VENDOR-OTHER** (18 files): Other vendor updates (mini-gmp, plfit, cs, f2c, lapack)
- **TOOL-SAMPLING** (1 files): Sampling uniformity test tool
- **DOC** (30 files): Documentation reorganization and improvements
- **INTERFACES** (2 files): Interface descriptions (functions.yaml, types.yaml)
- **SETUP** (2 files): igraph_setup() infrastructure
- **ERROR-CODES** (2 files): Error code changes
- **INTERRUPT** (3 files): Interruption handler changes
- **STATUS** (2 files): Status handler changes
- **PROGRESS** (2 files): Progress handler changes
- **MEMORY** (2 files): Memory management macros
- **DECLS** (1 files): Declaration macros (igraph_decls.h)
- **VERSION** (2 files): Version handling
- **MAIN-HEADER** (1 files): Main igraph.h reorganization
- **RNG** (9 files): RNG changes (set_default, RNG_BEGIN/END removal)
- **TYPES** (4 files): Core type changes (igraph_int_t, igraph_multiple_t, constants)
- **DS-VECTOR** (9 files): Vector/vector_ptr changes
- **DS-MATRIX** (6 files): Matrix changes
- **DS-STRVECTOR** (2 files): String vector changes
- **DS-PMT** (3 files): Polymorphic type templates
- **DS-SPARSEMAT** (2 files): Sparse matrix changes
- **DS-OTHER** (47 files): Other data structures (bitset, dqueue, heap, stack, etc.)
- **DEP-ARRAY3D** (4 files): Removed igraph_array3_t (3D array)
- **DEP-MICROSCOPIC** (2 files): Removed microscopic update functions
- **DEP-ZEROIN** (1 files): Removed igraph_zeroin()
- **ATTRS** (4 files): Attribute handler/record changes
- **GRAPH** (9 files): Core graph interface changes
- **ITERATORS** (4 files): Iterator/visitor changes
- **ADJLIST** (2 files): Adjacency list changes
- **CONSTRUCTORS** (18 files): Graph constructor changes (adjacency, LCF, lattice, etc.)
- **GAMES-ER** (1 files): Erdős-Rényi game changes
- **GAMES** (31 files): Other random graph generator changes
- **BIPARTITE** (2 files): Bipartite function changes
- **SPATIAL** (8 files): New spatial graph functions
- **SAMPLING** (1 files): New sampling functions
- **PATHS** (18 files): Path/distance function changes
- **CYCLES** (7 files): Cycle function changes
- **COMM-INFOMAP** (7 files): Infomap community detection
- **COMM-LEIDEN** (1 files): Leiden community detection
- **COMM** (26 files): Other community detection changes
- **ISO** (8 files): Isomorphism changes (igraph_topology.h→igraph_isomorphism.h)
- **CENTRALITY** (14 files): Centrality function changes
- **CLIQUES** (7 files): Clique/independent set changes
- **LAYOUT** (28 files): Layout function changes
- **IO** (31 files): I/O format changes (Pajek, GML, GraphML, etc.)
- **PROPS** (22 files): Graph property changes
- **FLOW** (5 files): Flow/cut algorithm changes
- **OPERATORS** (22 files): Graph operator changes
- **CONNECTIVITY** (9 files): Component/separator/connectivity changes
- **LINALG** (11 files): Linear algebra changes (ARPACK, BLAS, LAPACK, eigen)
- **MISC** (29 files): Miscellaneous algorithm changes
- **HRG** (7 files): Hierarchical random graph changes
- **INTERNAL** (12 files): Internal utility changes
- **TEST** (507 files): Test changes
- **EXAMPLE** (157 files): Example code updates
- **FUZZ** (27 files): Fuzzing harness updates
- **OTHER-SRC** (4 files): Other source changes

## Files by Category

### CHANGELOG: Changelog files (2 files)

  +276	-0	CHANGELOG.md
  +213	-0	CHANGELOG_PROOF_OF_WORK.md

### VERSIONING-POLICY: Explicit versioning policy (1 files)

  +58	-0	VERSIONING.md

### CONTRIBUTORS: Contributor documentation (4 files)

  +45	-0	.all-contributorsrc
  +39	-2	ACKNOWLEDGEMENTS.md
  +7	-0	CONTRIBUTORS.md
  +5	-0	CONTRIBUTORS.txt

### META: Repository metadata (3 files)

  +1	-0	.gitignore
  +12	-10	CONTRIBUTING.md
  +3	-3	README.md

### BUILD-CPP14: C++14 requirement; compiler flags (1 files)

  +12	-1	etc/cmake/compilers.cmake

### BUILD-DEPS: Dependency management (1 files)

  +12	-4	etc/cmake/dependencies.cmake

### BUILD-CMAKE: Build system changes (7 files)

  +2	-2	CMakeLists.txt
  +5	-0	etc/cmake/cpack_install_script.cmake
  +1	-0	etc/cmake/features.cmake
  +5	-5	etc/cmake/packaging.cmake
  +8	-5	etc/cmake/summary.cmake
  +24	-14	src/CMakeLists.txt
  +1	-0	src/config.h.in

### BUILD-CI: CI configuration (2 files)

  +11	-10	azure-pipelines.yml
  +1	-0	codecov.yml

### VENDOR-QHULL: Qhull vendored for spatial functions (33 files)

  +12	-0	vendor/qhull/CHANGES.md
  +48	-0	vendor/qhull/CMakeLists.txt
  +39	-0	vendor/qhull/COPYING.txt
  +720	-0	vendor/qhull/README.txt
  +69	-0	vendor/qhull/libqhull_r/accessors_r.c
  +2302	-0	vendor/qhull/libqhull_r/geom2_r.c
  +1284	-0	vendor/qhull/libqhull_r/geom_r.c
  +189	-0	vendor/qhull/libqhull_r/geom_r.h
  +2268	-0	vendor/qhull/libqhull_r/global_r.c
  +4128	-0	vendor/qhull/libqhull_r/io_r.c
  +166	-0	vendor/qhull/libqhull_r/io_r.h
  +1754	-0	vendor/qhull/libqhull_r/libqhull_r.c
  +1281	-0	vendor/qhull/libqhull_r/libqhull_r.h
  +566	-0	vendor/qhull/libqhull_r/mem_r.c
  +235	-0	vendor/qhull/libqhull_r/mem_r.h
  +5589	-0	vendor/qhull/libqhull_r/merge_r.c
  +238	-0	vendor/qhull/libqhull_r/merge_r.h
  +3959	-0	vendor/qhull/libqhull_r/poly2_r.c
  +1448	-0	vendor/qhull/libqhull_r/poly_r.c
  +310	-0	vendor/qhull/libqhull_r/poly_r.h
  +161	-0	vendor/qhull/libqhull_r/qhull_ra.h
  +1383	-0	vendor/qhull/libqhull_r/qset_r.c
  +515	-0	vendor/qhull/libqhull_r/qset_r.h
  +249	-0	vendor/qhull/libqhull_r/random_r.c
  +41	-0	vendor/qhull/libqhull_r/random_r.h
  +854	-0	vendor/qhull/libqhull_r/rboxlib_r.c
  +727	-0	vendor/qhull/libqhull_r/stat_r.c
  +563	-0	vendor/qhull/libqhull_r/stat_r.h
  +617	-0	vendor/qhull/libqhull_r/user_r.c
  +1061	-0	vendor/qhull/libqhull_r/user_r.h
  +102	-0	vendor/qhull/libqhull_r/usermem_r.c
  +68	-0	vendor/qhull/libqhull_r/userprintf_r.c
  +53	-0	vendor/qhull/libqhull_r/userprintf_rbox_r.c

### VENDOR-INFOMAP: Infomap updated to 2.8.0 (54 files)

  +16	-0	vendor/infomap/CITATION.cff
  +48	-0	vendor/infomap/CMakeLists.txt
  +674	-0	vendor/infomap/LICENSE_GPLv3.txt
  +162	-0	vendor/infomap/README.rst
  +103	-0	vendor/infomap/src/Infomap.h
  +240	-0	vendor/infomap/src/core/BiasedMapEquation.cpp
  +180	-0	vendor/infomap/src/core/BiasedMapEquation.h
  +165	-0	vendor/infomap/src/core/FlowData.h
  +26	-0	vendor/infomap/src/core/InfoEdge.cpp
  +47	-0	vendor/infomap/src/core/InfoEdge.h
  +405	-0	vendor/infomap/src/core/InfoNode.cpp
  +374	-0	vendor/infomap/src/core/InfoNode.h
  +2182	-0	vendor/infomap/src/core/InfomapBase.cpp
  +586	-0	vendor/infomap/src/core/InfomapBase.h
  +137	-0	vendor/infomap/src/core/InfomapConfig.h
  +766	-0	vendor/infomap/src/core/InfomapOptimizer.h
  +113	-0	vendor/infomap/src/core/InfomapOptimizerBase.h
  +339	-0	vendor/infomap/src/core/MapEquation.h
  +451	-0	vendor/infomap/src/core/MemMapEquation.cpp
  +174	-0	vendor/infomap/src/core/MemMapEquation.h
  +271	-0	vendor/infomap/src/core/MetaMapEquation.cpp
  +185	-0	vendor/infomap/src/core/MetaMapEquation.h
  +329	-0	vendor/infomap/src/core/StateNetwork.cpp
  +216	-0	vendor/infomap/src/core/StateNetwork.h
  +238	-0	vendor/infomap/src/core/iterators/InfomapIterator.cpp
  +341	-0	vendor/infomap/src/core/iterators/InfomapIterator.h
  +32	-0	vendor/infomap/src/core/iterators/IterWrapper.h
  +369	-0	vendor/infomap/src/core/iterators/infomapIterators.h
  +628	-0	vendor/infomap/src/core/iterators/treeIterators.h
  +189	-0	vendor/infomap/src/io/ClusterMap.cpp
  +52	-0	vendor/infomap/src/io/ClusterMap.h
  +264	-0	vendor/infomap/src/io/Config.cpp
  +268	-0	vendor/infomap/src/io/Config.h
  +990	-0	vendor/infomap/src/io/Network.cpp
  +214	-0	vendor/infomap/src/io/Network.h
  +629	-0	vendor/infomap/src/io/Output.cpp
  +36	-0	vendor/infomap/src/io/Output.h
  +362	-0	vendor/infomap/src/io/ProgramInterface.cpp
  +423	-0	vendor/infomap/src/io/ProgramInterface.h
  +87	-0	vendor/infomap/src/io/SafeFile.h
  +69	-0	vendor/infomap/src/utils/Date.h
  +50	-0	vendor/infomap/src/utils/FileURI.cpp
  +54	-0	vendor/infomap/src/utils/FileURI.h
  +898	-0	vendor/infomap/src/utils/FlowCalculator.cpp
  +75	-0	vendor/infomap/src/utils/FlowCalculator.h
  +17	-0	vendor/infomap/src/utils/Log.cpp
  +110	-0	vendor/infomap/src/utils/Log.h
  +153	-0	vendor/infomap/src/utils/MetaCollection.h
  +45	-0	vendor/infomap/src/utils/Random.h
  +103	-0	vendor/infomap/src/utils/Stopwatch.h
  +82	-0	vendor/infomap/src/utils/VectorMap.h
  +216	-0	vendor/infomap/src/utils/convert.h
  +57	-0	vendor/infomap/src/utils/infomath.h
  +19	-0	vendor/infomap/src/version.h

### VENDOR-NANOFLANN: nanoflann updated to 1.9.0 (1 files)

  +2813	-0	vendor/nanoflann/nanoflann.hpp

### VENDOR-OTHER: Other vendor updates (mini-gmp, plfit, cs, f2c, lapack) (18 files)

  +2	-0	vendor/CMakeLists.txt
  +2	-2	vendor/cs/cs.h
  +0	-2	vendor/cs/cs_randperm.c
  +2	-1	vendor/f2c/s_cat.c
  +4	-2	vendor/f2c/s_copy.c
  +1	-2	vendor/lapack/fortran_intrinsics.c
  +80	-36	vendor/mini-gmp/mini-gmp.c
  +1	-0	vendor/mini-gmp/mini-gmp.h
  +2	-2	vendor/plfit/gss.h
  +2	-2	vendor/plfit/hzeta.h
  +2	-2	vendor/plfit/kolmogorov.h
  +7	-7	vendor/plfit/lbfgs.h
  +0	-1	vendor/plfit/plfit.c
  +2	-3	vendor/plfit/plfit.h
  +6	-6	vendor/plfit/plfit_decls.h
  +2	-2	vendor/plfit/plfit_error.h
  +2	-2	vendor/plfit/plfit_mt.h
  +2	-2	vendor/plfit/plfit_sampling.h

### TOOL-SAMPLING: Sampling uniformity test tool (1 files)

  +111	-0	tools/sampling_uniformity_test/test.cpp

### DOC: Documentation reorganization and improvements (30 files)

  +4	-2	doc/CMakeLists.txt
  +1	-1	doc/arpack.xxml => doc/linalg.xxml
  +18	-1	doc/attributes.xxml
  +32	-10	doc/basicigraph.xxml
  +2	-6	doc/bipartite.xxml
  +1	-0	doc/community.xxml
  +10	-3	doc/cycles.xxml
  +1	-1	doc/doxrox.py
  +0	-5	doc/foreign.xxml
  +85	-0	doc/games.xxml
  +52	-54	doc/generators.xxml
  +20	-16	doc/igraph-docs.xml
  +9	-0	doc/installation.xml
  +6	-16	doc/isomorphism.xxml
  +0	-7	doc/iterators.xxml
  +0	-6	doc/matrix.xxml
  +0	-4	doc/motifs.xxml
  +3	-11	doc/nongraph.xxml
  +0	-4	doc/operators.xxml
  +9	-9	doc/pmt.xml
  +1	-0	doc/progress.xxml
  +0	-8	doc/sparsemat.xxml
  +32	-0	doc/spatial.xxml
  +2	-9	doc/spatialgames.xxml => doc/processes.xxml
  +3	-28	doc/structural.xxml
  +2	-7	doc/strvector.xxml
  +16	-10	doc/tutorial.xml
  +7	-12	doc/vector.xxml
  +1	-0	doc/vectorlist.xxml
  +0	-5	doc/visitors.xxml

### INTERFACES: Interface descriptions (functions.yaml, types.yaml) (2 files)

  +473	-445	interfaces/functions.yaml
  +44	-45	interfaces/types.yaml

### SETUP: igraph_setup() infrastructure (2 files)

  +14	-12	examples/simple/igraph_adjacency.c => include/igraph_setup.h
  +67	-0	src/core/setup.c

### ERROR-CODES: Error code changes (2 files)

  +29	-96	include/igraph_error.h
  +58	-49	src/core/error.c

### INTERRUPT: Interruption handler changes (3 files)

  +12	-17	include/igraph_interrupt.h
  +5	-6	src/core/interruption.c
  +8	-10	src/core/interruption.h

### STATUS: Status handler changes (2 files)

  +14	-24	include/igraph_statusbar.h
  +11	-14	src/core/statusbar.c

### PROGRESS: Progress handler changes (2 files)

  +35	-22	include/igraph_progress.h
  +8	-13	src/core/progress.c

### MEMORY: Memory management macros (2 files)

  +5	-16	include/igraph_memory.h
  +1	-1	src/core/memory.c

### DECLS: Declaration macros (igraph_decls.h) (1 files)

  +18	-11	include/igraph_decls.h

### VERSION: Version handling (2 files)

  +6	-11	include/igraph_version.h.in
  +15	-13	src/version.c

### MAIN-HEADER: Main igraph.h reorganization (1 files)

  +7	-8	include/igraph.h

### RNG: RNG changes (set_default, RNG_BEGIN/END removal) (9 files)

  +14	-40	include/igraph_random.h
  +60	-98	src/random/random.c
  +43	-0	src/random/random_device.cpp
  +17	-20	src/random/random_internal.h
  +1	-1	src/random/rng_glibc2.c
  +1	-1	src/random/rng_mt19937.c
  +3	-5	src/random/rng_pcg32.c
  +1	-1	src/random/rng_pcg64.c
  +192	-0	src/random/sampling.c

### TYPES: Core type changes (igraph_int_t, igraph_multiple_t, constants) (4 files)

  +5	-9	include/igraph_config.h.in
  +96	-50	include/igraph_constants.h
  +7	-12	include/igraph_datatype.h
  +11	-25	include/igraph_types.h

### DS-VECTOR: Vector/vector_ptr changes (9 files)

  +18	-25	include/igraph_vector.h
  +5	-9	include/igraph_vector_list.h
  +41	-57	include/igraph_vector_pmt.h
  +17	-24	include/igraph_vector_ptr.h
  +3	-8	include/igraph_vector_type.h
  +75	-132	src/core/vector.c
  +289	-291	src/core/vector.pmt
  +1	-2	src/core/vector_list.c
  +96	-59	src/core/vector_ptr.c

### DS-MATRIX: Matrix changes (6 files)

  +5	-13	include/igraph_matrix.h
  +5	-9	include/igraph_matrix_list.h
  +40	-52	include/igraph_matrix_pmt.h
  +17	-31	src/core/matrix.c
  +170	-212	src/core/matrix.pmt
  +1	-2	src/core/matrix_list.c

### DS-STRVECTOR: String vector changes (2 files)

  +28	-35	include/igraph_strvector.h
  +126	-105	src/core/strvector.c

### DS-PMT: Polymorphic type templates (3 files)

  +11	-10	include/igraph_pmt.h
  +3	-8	include/igraph_pmt_off.h
  +21	-24	include/igraph_typed_list_pmt.h

### DS-SPARSEMAT: Sparse matrix changes (2 files)

  +33	-58	include/igraph_sparsemat.h
  +109	-422	src/core/sparsemat.c

### DS-OTHER: Other data structures (bitset, dqueue, heap, stack, etc.) (47 files)

  +24	-25	include/igraph_bitset.h
  +5	-8	include/igraph_bitset_list.h
  +7	-16	include/igraph_complex.h
  +5	-10	include/igraph_dqueue.h
  +6	-12	include/igraph_dqueue_pmt.h
  +5	-10	include/igraph_heap.h
  +7	-13	include/igraph_heap_pmt.h
  +12	-17	include/igraph_psumtree.h
  +5	-10	include/igraph_qsort.h
  +5	-10	include/igraph_stack.h
  +7	-12	include/igraph_stack_pmt.h
  +5	-10	include/igraph_threading.h.in
  +57	-105	src/core/bitset.c
  +1	-1	src/core/bitset_list.c
  +23	-24	src/core/buckets.c
  +19	-20	src/core/buckets.h
  +17	-18	src/core/cutheap.c
  +10	-11	src/core/cutheap.h
  +1	-2	src/core/dqueue.c
  +6	-19	src/core/dqueue.pmt
  +8	-9	src/core/estack.c
  +8	-9	src/core/estack.h
  +3	-4	src/core/fixed_vectorlist.c
  +5	-6	src/core/fixed_vectorlist.h
  +22	-22	src/core/genheap.c
  +11	-11	src/core/genheap.h
  +19	-19	src/core/grid.c
  +15	-16	src/core/grid.h
  +1	-2	src/core/heap.c
  +18	-23	src/core/heap.pmt
  +130	-143	src/core/indheap.c
  +31	-34	src/core/indheap.h
  +9	-10	src/core/marked_queue.c
  +9	-10	src/core/marked_queue.h
  +1	-2	src/core/printing.c
  +9	-10	src/core/psumtree.c
  +18	-18	src/core/set.c
  +13	-13	src/core/set.h
  +1	-2	src/core/stack.c
  +10	-11	src/core/stack.pmt
  +13	-14	src/core/trie.c
  +10	-11	src/core/trie.h
  +1	-16	src/math/complex.c
  +4	-8	tests/benchmarks/igraph_qsort.c
  +2	-7	tests/unit/igraph_psumtree.c
  +1	-2	tests/unit/igraph_qsort.c
  +3	-4	tests/unit/igraph_qsort_r.c

### DEP-ARRAY3D: Removed igraph_array3_t (3D array) (4 files)

  +0	-63	include/igraph_array.h
  +0	-54	include/igraph_array_pmt.h
  +29	-30	src/core/array.c => tests/regression/bug_2608.c
  +0	-110	src/core/array.pmt

### DEP-MICROSCOPIC: Removed microscopic update functions (2 files)

  +0	-61	include/igraph_microscopic_update.h
  +0	-1209	src/misc/microscopic_update.c

### DEP-ZEROIN: Removed igraph_zeroin() (1 files)

  +0	-201	src/internal/zeroin.c

### ATTRS: Attribute handler/record changes (4 files)

  +235	-163	include/igraph_attributes.h
  +618	-27	src/graph/attributes.c
  +19	-23	src/graph/attributes.h
  +879	-2494	src/graph/cattributes.c

### GRAPH: Core graph interface changes (9 files)

  +6	-11	include/igraph_graph_list.h
  +57	-41	include/igraph_interface.h
  +4	-34	src/graph/basic_query.c
  +1	-1	src/graph/caching.c
  +3	-3	src/graph/caching.h
  +2	-3	src/graph/graph_list.c
  +3	-13	src/graph/internal.h
  +58	-22	src/graph/type_common.c
  +339	-250	src/graph/type_indexededgelist.c

### ITERATORS: Iterator/visitor changes (4 files)

  +47	-52	include/igraph_iterators.h
  +15	-20	include/igraph_visitor.h
  +124	-170	src/graph/iterators.c
  +38	-37	src/graph/visitors.c

### ADJLIST: Adjacency list changes (2 files)

  +30	-35	include/igraph_adjlist.h
  +123	-186	src/graph/adjlist.c

### CONSTRUCTORS: Graph constructor changes (adjacency, LCF, lattice, etc.) (18 files)

  +33	-42	include/igraph_constructors.h
  +315	-216	src/constructors/adjacency.c
  +5	-6	src/constructors/atlas-edges.h
  +8	-8	src/constructors/atlas.c
  +8	-21	src/constructors/basic_constructors.c
  +7	-7	src/constructors/circulant.c
  +8	-9	src/constructors/de_bruijn.c
  +37	-38	src/constructors/famous.c
  +37	-38	src/constructors/full.c
  +10	-10	src/constructors/generalized_petersen.c
  +15	-16	src/constructors/kautz.c
  +46	-50	src/constructors/lattices.c
  +37	-37	src/constructors/lcf.c
  +19	-20	src/constructors/linegraph.c
  +18	-18	src/constructors/mycielskian.c
  +7	-8	src/constructors/prufer.c
  +52	-91	src/constructors/regular.c
  +6	-8	src/constructors/trees.c

### GAMES-ER: Erdős-Rényi game changes (1 files)

  +644	-244	src/games/erdos_renyi.c

### GAMES: Other random graph generator changes (31 files)

  +84	-90	include/igraph_games.h
  +70	-88	src/games/barabasi.c
  +9	-15	src/games/callaway_traits.c
  +6	-8	src/games/chung_lu.c
  +31	-45	src/games/citations.c
  +65	-50	src/games/correlated.c
  +72	-107	src/games/degree_sequence.c
  +3	-3	src/games/degree_sequence_vl/degree_sequence_vl.h
  +5	-5	src/games/degree_sequence_vl/gengraph_definitions.h
  +17	-17	src/games/degree_sequence_vl/gengraph_degree_sequence.cpp
  +12	-12	src/games/degree_sequence_vl/gengraph_degree_sequence.h
  +101	-101	src/games/degree_sequence_vl/gengraph_graph_molloy_hash.cpp
  +33	-33	src/games/degree_sequence_vl/gengraph_graph_molloy_hash.h
  +137	-137	src/games/degree_sequence_vl/gengraph_graph_molloy_optimized.cpp
  +40	-40	src/games/degree_sequence_vl/gengraph_graph_molloy_optimized.h
  +27	-27	src/games/degree_sequence_vl/gengraph_hash.h
  +1	-7	src/games/degree_sequence_vl/gengraph_mr-connected.cpp
  +49	-49	src/games/degree_sequence_vl/gengraph_qsort.h
  +10	-198	src/games/dotproduct.c
  +7	-13	src/games/establishment.c
  +21	-26	src/games/forestfire.c
  +5	-11	src/games/grg.c
  +12	-18	src/games/growing_random.c
  +10	-16	src/games/islands.c
  +2	-4	src/games/k_regular.c
  +33	-43	src/games/preference.c
  +40	-48	src/games/recent_degree.c
  +128	-123	src/games/sbm.c
  +26	-26	src/games/static_fitness.c
  +9	-17	src/games/tree.c
  +9	-10	src/games/watts_strogatz.c

### BIPARTITE: Bipartite function changes (2 files)

  +52	-52	include/igraph_bipartite.h
  +737	-383	src/misc/bipartite.c

### SPATIAL: New spatial graph functions (8 files)

  +91	-0	include/igraph_spatial.h
  +816	-0	src/spatial/beta_skeleton.cpp
  +188	-0	src/spatial/convex_hull.c
  +280	-0	src/spatial/delaunay.c
  +119	-0	src/spatial/edge_lengths.c
  +121	-0	src/spatial/nanoflann_internal.hpp
  +189	-0	src/spatial/nearest_neighbor.cpp
  +34	-0	src/spatial/spatial_internal.h

### SAMPLING: New sampling functions (1 files)

  +45	-0	include/igraph_sampling.h

### PATHS: Path/distance function changes (18 files)

  +113	-176	include/igraph_paths.h
  +46	-28	src/paths/all_shortest_paths.c
  +14	-16	src/paths/astar.c
  +86	-95	src/paths/bellman_ford.c
  +152	-136	src/paths/dijkstra.c
  +176	-363	src/paths/distances.c
  +31	-33	src/paths/eulerian.c
  +40	-38	src/paths/floyd_warshall.c
  +11	-11	src/paths/histogram.c
  +94	-82	src/paths/johnson.c
  +119	-0	src/paths/paths_internal.h
  +15	-71	src/paths/random_walk.c
  +239	-264	src/paths/shortest_paths.c
  +79	-57	src/paths/simple_paths.c
  +67	-74	src/paths/sparsifier.c
  +154	-70	src/paths/unweighted.c
  +22	-28	src/paths/voronoi.c
  +34	-36	src/paths/widest_paths.c

### CYCLES: Cycle function changes (7 files)

  +40	-26	include/igraph_cycles.h
  +51	-34	src/cycles/simple_cycles.c
  +53	-55	src/misc/cycle_bases.c => src/cycles/cycle_bases.c
  +83	-86	src/misc/feedback_arc_set.c => src/cycles/feedback_sets.c
  +6	-6	src/misc/feedback_arc_set.h => src/cycles/feedback_sets.h
  +16	-16	src/misc/order_cycle.cpp => src/cycles/order_cycle.cpp
  +3	-3	src/misc/order_cycle.h => src/cycles/order_cycle.h

### COMM-INFOMAP: Infomap community detection (7 files)

  +275	-0	src/community/infomap.cpp
  +0	-323	src/community/infomap/infomap.cc
  +0	-382	src/community/infomap/infomap_FlowGraph.cc
  +0	-81	src/community/infomap/infomap_FlowGraph.h
  +0	-522	src/community/infomap/infomap_Greedy.cc
  +0	-74	src/community/infomap/infomap_Greedy.h
  +0	-52	src/community/infomap/infomap_Node.h

### COMM-LEIDEN: Leiden community detection (1 files)

  +815	-368	src/community/leiden.c

### COMM: Other community detection changes (26 files)

  +72	-51	include/igraph_community.h
  +4	-4	src/community/community_internal.h
  +50	-53	src/community/community_misc.c
  +149	-113	src/community/edge_betweenness.c
  +41	-55	src/community/fast_modularity.c
  +26	-38	src/community/fluid.c
  +512	-206	src/community/label_propagation.c
  +79	-76	src/community/leading_eigenvector.c
  +49	-53	src/community/louvain.c
  +18	-20	src/community/modularity.c
  +23	-14	src/community/optimal_modularity.c
  +4	-5	src/community/spinglass/NetDataTypes.cpp
  +44	-45	src/community/spinglass/NetDataTypes.h
  +7	-8	src/community/spinglass/NetRoutines.cpp
  +1	-2	src/community/spinglass/NetRoutines.h
  +25	-40	src/community/spinglass/clustertool.cpp
  +88	-89	src/community/spinglass/pottsmodel_2.cpp
  +20	-21	src/community/spinglass/pottsmodel_2.h
  +26	-37	src/community/voronoi.c
  +6	-7	src/community/walktrap/walktrap.cpp
  +1	-2	src/community/walktrap/walktrap_communities.cpp
  +2	-3	src/community/walktrap/walktrap_communities.h
  +4	-5	src/community/walktrap/walktrap_graph.cpp
  +1	-2	src/community/walktrap/walktrap_graph.h
  +1	-2	src/community/walktrap/walktrap_heap.cpp
  +1	-2	src/community/walktrap/walktrap_heap.h

### ISO: Isomorphism changes (igraph_topology.h→igraph_isomorphism.h) (8 files)

  +34	-69	include/igraph_topology.h => include/igraph_isomorphism.h
  +166	-31	src/isomorphism/bliss.cc
  +36	-33	src/isomorphism/isoclasses.c
  +3	-4	src/isomorphism/isoclasses.h
  +9	-10	src/isomorphism/isomorphism_misc.c
  +119	-129	src/isomorphism/lad.c
  +5	-33	src/isomorphism/queries.c
  +67	-108	src/isomorphism/vf2.c

### CENTRALITY: Centrality function changes (14 files)

  +99	-96	include/igraph_centrality.h
  +289	-186	src/centrality/betweenness.c
  +4	-4	src/centrality/centrality_internal.h
  +26	-6	src/centrality/centrality_other.c
  +56	-94	src/centrality/centralization.c
  +42	-44	src/centrality/closeness.c
  +25	-24	src/centrality/coreness.c
  +169	-103	src/centrality/eigenvector.c
  +149	-167	src/centrality/hub_authority.c
  +81	-79	src/centrality/pagerank.c
  +3	-4	src/centrality/prpack.cpp
  +4	-4	src/centrality/prpack/prpack_igraph_graph.cpp
  +3	-4	src/centrality/prpack_internal.h
  +17	-17	src/centrality/truss.cpp

### CLIQUES: Clique/independent set changes (7 files)

  +85	-60	include/igraph_cliques.h
  +9	-7	src/cliques/cliquer_internal.h
  +36	-23	src/cliques/cliquer_wrapper.c
  +150	-87	src/cliques/cliques.c
  +74	-93	src/cliques/glet.c
  +175	-104	src/cliques/maximal_cliques.c
  +51	-40	src/cliques/maximal_cliques_template.h

### LAYOUT: Layout function changes (28 files)

  +36	-42	include/igraph_layout.h
  +21	-23	src/layout/align.c
  +11	-13	src/layout/circular.c
  +42	-44	src/layout/davidson_harel.c
  +2	-2	src/layout/drl/drl_Node.h
  +2	-2	src/layout/drl/drl_Node_3d.h
  +23	-23	src/layout/drl/drl_graph.cpp
  +13	-13	src/layout/drl/drl_graph.h
  +19	-19	src/layout/drl/drl_graph_3d.cpp
  +13	-13	src/layout/drl/drl_graph_3d.h
  +1	-5	src/layout/drl/drl_layout.cpp
  +1	-5	src/layout/drl/drl_layout_3d.cpp
  +37	-43	src/layout/fruchterman_reingold.c
  +11	-16	src/layout/gem.c
  +24	-26	src/layout/graphopt.c
  +31	-31	src/layout/kamada_kawai.c
  +24	-30	src/layout/large_graph.c
  +5	-8	src/layout/layout_bipartite.c
  +5	-7	src/layout/layout_grid.c
  +4	-5	src/layout/layout_internal.h
  +11	-25	src/layout/layout_random.c
  +13	-20	src/layout/mds.c
  +34	-25	src/layout/merge_dla.c
  +15	-15	src/layout/merge_grid.c
  +10	-10	src/layout/merge_grid.h
  +64	-66	src/layout/reingold_tilford.c
  +164	-180	src/layout/sugiyama.c
  +73	-77	src/layout/umap.c

### IO: I/O format changes (Pajek, GML, GraphML, etc.) (31 files)

  +10	-25	include/igraph_foreign.h
  +14	-45	src/io/dimacs.c
  +3	-3	src/io/dl-header.h
  +2	-2	src/io/dl-lexer.l
  +17	-17	src/io/dl-parser.y
  +24	-20	src/io/dl.c
  +15	-16	src/io/dot.c
  +4	-5	src/io/edgelist.c
  +1	-1	src/io/gml-header.h
  +2	-2	src/io/gml-lexer.l
  +3	-3	src/io/gml-parser.y
  +26	-26	src/io/gml-tree.c
  +22	-22	src/io/gml-tree.h
  +120	-150	src/io/gml.c
  +6	-7	src/io/graphdb.c
  +160	-299	src/io/graphml.c
  +10	-11	src/io/leda.c
  +2	-2	src/io/lgl-header.h
  +2	-2	src/io/lgl-lexer.l
  +5	-5	src/io/lgl-parser.y
  +42	-37	src/io/lgl.c
  +1	-1	src/io/ncol-header.h
  +2	-2	src/io/ncol-lexer.l
  +5	-5	src/io/ncol-parser.y
  +39	-35	src/io/ncol.c
  +10	-10	src/io/pajek-header.h
  +2	-2	src/io/pajek-lexer.l
  +187	-107	src/io/pajek-parser.y
  +49	-100	src/io/pajek.c
  +5	-9	src/io/parse_utils.c
  +2	-2	src/io/parse_utils.h

### PROPS: Graph property changes (22 files)

  +11	-16	include/igraph_neighborhood.h
  +30	-52	include/igraph_structural.h
  +9	-14	include/igraph_transitivity.h
  +58	-36	src/properties/basic_properties.c
  +17	-22	src/properties/complete.c
  +12	-20	src/properties/constraint.c
  +9	-11	src/properties/convergence_degree.c
  +26	-127	src/properties/dag.c
  +77	-88	src/properties/degrees.c
  +28	-30	src/properties/ecc.c
  +37	-38	src/properties/girth.c
  +8	-12	src/properties/loops.c
  +68	-46	src/properties/multiplicity.c
  +47	-49	src/properties/neighborhood.c
  +12	-13	src/properties/perfect.c
  +3	-4	src/properties/properties_internal.h
  +13	-13	src/properties/rich_club.c
  +13	-71	src/properties/spectral.c
  +49	-44	src/properties/trees.c
  +71	-95	src/properties/triangles.c
  +11	-13	src/properties/triangles_template.h
  +10	-12	src/properties/triangles_template1.h

### FLOW: Flow/cut algorithm changes (5 files)

  +31	-36	include/igraph_flow.h
  +197	-202	src/flow/flow.c
  +5	-6	src/flow/flow_conversion.c
  +5	-6	src/flow/flow_internal.h
  +154	-154	src/flow/st-cuts.c

### OPERATORS: Graph operator changes (22 files)

  +37	-29	include/igraph_operators.h
  +2	-4	src/operators/add_edge.c
  +6	-8	src/operators/complementer.c
  +12	-13	src/operators/compose.c
  +36	-40	src/operators/connect_neighborhood.c
  +15	-17	src/operators/contract.c
  +10	-12	src/operators/difference.c
  +18	-19	src/operators/disjoint_union.c
  +16	-17	src/operators/intersection.c
  +6	-9	src/operators/join.c
  +16	-17	src/operators/misc_internal.c
  +3	-4	src/operators/misc_internal.h
  +18	-22	src/operators/permute.c
  +86	-86	src/operators/products.c
  +6	-7	src/operators/reverse.c
  +113	-110	src/operators/rewire.c
  +46	-56	src/operators/rewire_edges.c
  +7	-5	src/operators/rewire_internal.h
  +7	-9	src/operators/simplify.c
  +47	-63	src/operators/subgraph.c
  +3	-5	src/operators/subgraph.h
  +14	-15	src/operators/union.c

### CONNECTIVITY: Component/separator/connectivity changes (9 files)

  +5	-10	include/igraph_cohesive_blocks.h
  +11	-25	include/igraph_components.h
  +5	-5	include/igraph_reachability.h
  +7	-13	include/igraph_separators.h
  +38	-37	src/connectivity/cohesive_blocks.c
  +111	-148	src/connectivity/components.c
  +32	-32	src/connectivity/percolation.c
  +21	-27	src/connectivity/reachability.c
  +77	-75	src/connectivity/separators.c

### LINALG: Linear algebra changes (ARPACK, BLAS, LAPACK, eigen) (11 files)

  +72	-13	include/igraph_arpack.h
  +5	-10	include/igraph_blas.h
  +28	-31	include/igraph_eigen.h
  +5	-10	include/igraph_lapack.h
  +185	-107	src/linalg/arpack.c
  +3	-4	src/linalg/arpack_internal.h
  +5	-7	src/linalg/blas.c
  +3	-5	src/linalg/blas_internal.h
  +25	-27	src/linalg/eigen.c
  +41	-42	src/linalg/lapack.c
  +3	-5	src/linalg/lapack_internal.h

### MISC: Miscellaneous algorithm changes (29 files)

  +14	-19	include/igraph_cocitation.h
  +17	-19	include/igraph_coloring.h
  +8	-13	include/igraph_embedding.h
  +6	-11	include/igraph_epidemics.h
  +24	-8	include/igraph_graphicality.h
  +7	-12	include/igraph_graphlets.h
  +13	-19	include/igraph_hrg.h
  +20	-3	include/igraph_lsap.h
  +6	-10	include/igraph_matching.h
  +17	-23	include/igraph_mixing.h
  +16	-25	include/igraph_motifs.h
  +8	-32	include/igraph_nongraph.h
  +7	-12	include/igraph_scan.h
  +17	-18	src/misc/chordality.c
  +66	-62	src/misc/cocitation.c
  +44	-51	src/misc/coloring.c
  +87	-171	src/misc/conversion.c
  +89	-92	src/misc/degree_sequence.cpp
  +56	-62	src/misc/embedding.c
  +81	-63	src/misc/graphicality.c
  +36	-0	src/misc/graphicality.h
  +36	-47	src/misc/matching.c
  +151	-101	src/misc/mixing.c
  +142	-129	src/misc/motifs.c
  +16	-223	src/misc/other.c
  +2	-11	src/misc/power_law_fit.c
  +64	-105	src/misc/scan.c
  +16	-27	src/misc/sir.c
  +331	-203	src/misc/spanning_trees.c

### HRG: Hierarchical random graph changes (7 files)

  +1	-1	src/hrg/dendro.h
  +2	-2	src/hrg/graph.h
  +1	-1	src/hrg/graph_simp.h
  +69	-88	src/hrg/hrg.cc
  +2	-2	src/hrg/hrg_types.cc
  +1	-1	src/hrg/rbtree.h
  +1	-1	src/hrg/splittree_eq.h

### INTERNAL: Internal utility changes (12 files)

  +1	-1	src/f2c.h
  +12	-15	src/internal/glpk_support.c
  +7	-9	src/internal/glpk_support.h
  +1	-3	src/internal/gmp_internal.h
  +1	-2	src/internal/hacks.c
  +3	-4	src/internal/hacks.h
  +56	-56	src/internal/lsap.c
  +136	-7	src/internal/utils.c
  +8	-1	src/internal/utils.h
  +26	-26	src/math/safe_intop.c
  +22	-22	src/math/safe_intop.h
  +1	-22	src/math/utils.c

### TEST: Test changes (507 files)

  +30	-8	tests/CMakeLists.txt
  +2	-2	tests/benchmarks/bench.h
  +150	-0	tests/benchmarks/beta_skeletons.c ← also: SPATIAL
  +2	-2	tests/benchmarks/coloring.c
  +12	-12	tests/benchmarks/community.c
  +3	-3	tests/benchmarks/connectivity.c
  +24	-24	tests/benchmarks/erdos_renyi.c ← also: GAMES-ER
  +3	-3	tests/benchmarks/graphicality.c
  +100	-0	tests/benchmarks/igraph_adjacency.c ← also: CONSTRUCTORS
  +13	-13	tests/benchmarks/igraph_average_path_length_unweighted.c
  +11	-11	tests/benchmarks/igraph_betweenness.c ← also: CENTRALITY
  +21	-21	tests/benchmarks/igraph_betweenness_weighted.c ← also: CENTRALITY
  +6	-6	tests/benchmarks/igraph_cliques.c ← also: CLIQUES
  +5	-5	tests/benchmarks/igraph_closeness_weighted.c
  +1	-1	tests/benchmarks/igraph_decompose.c
  +31	-12	tests/benchmarks/igraph_degree.c ← also: PROPS
  +10	-10	tests/benchmarks/igraph_degree_sequence_game.c ← also: GAMES
  +64	-0	tests/benchmarks/igraph_delaunay_graph.c ← also: SPATIAL
  +101	-161	tests/benchmarks/igraph_distances.c
  +5	-5	tests/benchmarks/igraph_ecc.c
  +8	-8	tests/benchmarks/igraph_induced_subgraph.c
  +2	-2	tests/benchmarks/igraph_induced_subgraph_edges.c
  +3	-5	tests/benchmarks/igraph_layout_umap.c
  +3	-5	tests/benchmarks/igraph_matrix_transpose.c ← also: DS-MATRIX
  +7	-6	tests/benchmarks/igraph_maximal_cliques.c ← also: CLIQUES
  +77	-0	tests/benchmarks/igraph_nearest_neighbor_graph.c ← also: SPATIAL
  +52	-55	tests/benchmarks/igraph_neighborhood.c
  +42	-24	tests/benchmarks/igraph_pagerank.c ← also: CENTRALITY
  +43	-25	tests/benchmarks/igraph_pagerank_weighted.c ← also: CENTRALITY
  +5	-9	tests/benchmarks/igraph_power_law_fit.c
  +2	-2	tests/benchmarks/igraph_random_walk.c
  +6	-6	tests/benchmarks/igraph_realize_degree_sequence.c ← also: PROPS
  +77	-0	tests/benchmarks/igraph_rewire.c ← also: OPERATORS
  +2	-2	tests/benchmarks/igraph_strength.c
  +5	-5	tests/benchmarks/igraph_transitivity.c
  +2	-2	tests/benchmarks/igraph_tree_game.c
  +2	-2	tests/benchmarks/igraph_vertex_connectivity.c
  +9	-17	tests/benchmarks/igraph_voronoi.c
  +75	-75	tests/benchmarks/inc_vs_adj.c
  +5	-5	tests/benchmarks/intersection.c
  +6	-6	tests/benchmarks/lad.c
  +3	-3	tests/benchmarks/modularity.c
  +164	-0	tests/benchmarks/spanning_tree.c ← also: MISC
  +1	-2	tests/regression/bug-1033045.c
  +1	-2	tests/regression/bug-1149658.c
  +6	-6	tests/regression/bug_1760.c
  +1	-1	tests/regression/bug_1814.c
  +1	-1	tests/regression/bug_1970.c
  +2	-3	tests/regression/bug_2150.c
  +1	-1	tests/regression/bug_2497.c
  +1	-1	tests/regression/bug_2506.c
  +1	-1	tests/regression/bug_2517.c
  +0	-0	tests/regression/bug_2608.out
  +1	-1	tests/regression/cattr_bool_bug.c
  +1	-1	tests/regression/cattr_bool_bug2.c
  +2	-2	tests/regression/igraph_layout_kamada_kawai_3d_bug_1462.c
  +2	-3	tests/regression/igraph_layout_reingold_tilford_bug_879.c
  +1	-1	tests/regression/igraph_read_graph_gml_invalid_inputs.c
  +1	-1	tests/regression/igraph_read_graph_graphml_invalid_inputs.c
  +1	-1	tests/regression/igraph_read_graph_pajek_invalid_inputs.c ← also: IO
  +4	-9	tests/unit/2wheap.c
  +7	-8	tests/unit/VF2-compat.c
  +42	-46	tests/unit/adj.c
  +6	-6	tests/unit/adj.out
  +6	-6	tests/unit/adjlist.c
  +10	-10	tests/unit/all_almost_e.c
  +10	-10	tests/unit/all_shortest_paths.c ← also: PATHS
  +26	-31	tests/unit/assortativity.c
  +182	-0	tests/unit/beta_skeletons.c ← also: SPATIAL
  +338	-0	tests/unit/beta_skeletons.out ← also: SPATIAL
  +7	-8	tests/unit/bfs.c
  +1	-2	tests/unit/bfs_simple.c
  +3	-5	tests/unit/bitset.c
  +2	-2	tests/unit/bliss_automorphisms.c ← also: ISO
  +1	-2	tests/unit/cattributes5.c ← also: ATTRS
  +22	-23	tests/unit/cattributes6.c ← also: ATTRS
  +99	-99	tests/unit/cattributes6.out ← also: ATTRS
  +2	-3	tests/unit/centralization.c
  +1	-1	tests/unit/cmp_epsilon.c
  +12	-11	tests/unit/coloring.c
  +14	-6	tests/unit/community_indexing.c
  +66	-25	tests/unit/community_label_propagation.c ← also: COMM
  +5	-5	tests/unit/community_label_propagation2.c ← also: COMM
  +1	-1	tests/unit/community_label_propagation2.out ← also: COMM
  +3	-5	tests/unit/community_label_propagation3.c ← also: COMM
  +129	-16	tests/unit/community_leiden.c ← also: COMM-LEIDEN
  +31	-16	tests/unit/community_leiden.out ← also: COMM-LEIDEN
  +1	-1	tests/unit/community_walktrap.c
  +2	-2	tests/unit/components.c
  +37	-45	tests/unit/constructor-failure.c
  +5	-13	tests/unit/coreness.c
  +3	-4	tests/unit/cutheap.c
  +20	-20	tests/unit/cycle_bases.c
  +4	-5	tests/unit/d_indheap.c
  +4	-4	tests/unit/dgemv.c
  +11	-11	tests/unit/edge_selectors.c
  +22	-23	tests/unit/efficiency.c
  +106	-0	tests/unit/eigen_stress.c ← also: LINALG
  +233	-21	tests/unit/erdos_renyi_game_gnm.c ← also: GAMES-ER
  +173	-86	tests/unit/erdos_renyi_game_gnp.c ← also: GAMES-ER
  +1	-1	tests/unit/error_macros.c
  +1	-1	tests/unit/expand_path_to_pairs.c
  +1	-1	tests/unit/fatal_handler.c
  +1	-1	tests/unit/foreign_empty.c
  +2	-3	tests/unit/full.c
  +4	-4	tests/unit/gen2wheap.c
  +1	-1	tests/unit/global_transitivity.c
  +5	-6	tests/unit/glpk_error.c
  +1	-1	tests/unit/gml.c
  +5	-6	tests/unit/graphlets.c
  +1	-1	tests/unit/harmonic_centrality.c
  +3	-3	tests/unit/heap.c
  +13	-13	tests/unit/hub_and_authority.c ← also: CENTRALITY
  +5	-5	tests/unit/hub_and_authority.out ← also: CENTRALITY
  +2	-3	tests/unit/igraph_add_edges.c
  +1	-2	tests/unit/igraph_add_vertices.c
  +2	-2	tests/unit/igraph_adhesion.c
  +8	-8	tests/unit/igraph_adjacency.c ← also: CONSTRUCTORS
  +19	-4	tests/unit/igraph_adjacency.out ← also: CONSTRUCTORS
  +1	-2	tests/unit/igraph_adjacency_spectral_embedding.c ← also: CONSTRUCTORS
  +37	-7	tests/unit/igraph_adjlist_init_complementer.c
  +45	-3	tests/unit/igraph_adjlist_init_complementer.out
  +1	-1	tests/unit/igraph_adjlist_simplify.c
  +6	-7	tests/unit/igraph_all_st_cuts.c
  +3	-3	tests/unit/igraph_all_st_mincuts.c
  +10	-10	tests/unit/igraph_almost_equals.c
  +1	-2	tests/unit/igraph_are_connected.c => tests/unit/igraph_are_adjacent.c
  +1	-2	tests/unit/igraph_arpack_rnsolve.c
  +2	-2	tests/unit/igraph_arpack_unpack_complex.c
  +1	-1	tests/unit/igraph_atlas.c
  +1	-1	tests/unit/igraph_attribute_combination_remove.c
  +2	-2	tests/unit/igraph_average_path_length.c
  +4	-4	tests/unit/igraph_average_path_length_dijkstra.c
  +1	-1	tests/unit/igraph_barabasi_aging_game.c
  +3	-3	tests/unit/igraph_barabasi_game.c
  +37	-38	tests/unit/igraph_betweenness.c ← also: CENTRALITY
  +67	-68	tests/unit/igraph_betweenness_subset.c ← also: CENTRALITY
  +56	-26	tests/unit/igraph_biadjacency.c ← also: CONSTRUCTORS
  +59	-4	tests/unit/igraph_biadjacency.out ← also: CONSTRUCTORS
  +2	-2	tests/unit/igraph_biconnected_components.c
  +5	-5	tests/unit/igraph_bipartite_create.c
  +266	-87	tests/unit/igraph_bipartite_game.c ← also: BIPARTITE
  +3	-4	tests/unit/igraph_bipartite_projection.c
  +1	-1	tests/unit/igraph_blas_dgemm.c
  +1	-1	tests/unit/igraph_callaway_traits_game.c
  +7	-7	tests/unit/igraph_chung_lu_game.c
  +2	-2	tests/unit/igraph_circulant.c
  +1	-1	tests/unit/igraph_cited_type_game.c
  +1	-1	tests/unit/igraph_citing_cited_type_game.c
  +1	-1	tests/unit/igraph_clique_size_hist.c
  +6	-6	tests/unit/igraph_closeness.c
  +2	-2	tests/unit/igraph_cohesion.c
  +2	-2	tests/unit/igraph_cohesive_blocks.c
  +16	-16	tests/unit/igraph_community_eb_get_merges.c
  +45	-33	tests/unit/igraph_community_edge_betweenness.c ← also: COMM
  +2	-3	tests/unit/igraph_community_fastgreedy.c
  +2	-4	tests/unit/igraph_community_fluid_communities.c
  +105	-61	tests/unit/igraph_community_infomap.c ← also: COMM-INFOMAP
  +45	-8	tests/unit/igraph_community_infomap.out ← also: COMM-INFOMAP
  +1	-2	tests/unit/igraph_community_leading_eigenvector2.c ← also: DS-VECTOR
  +169	-0	tests/unit/igraph_community_optimal_modularity.c ← also: COMM
  +5	-5	tests/unit/igraph_community_voronoi.c
  +1	-1	tests/unit/igraph_compare_communities.c
  +2	-3	tests/unit/igraph_complex.c
  +2	-2	tests/unit/igraph_connect_neighborhood.c
  +1	-1	tests/unit/igraph_constraint.c
  +17	-17	tests/unit/igraph_contract_vertices.c
  +2	-3	tests/unit/igraph_convergence_degree.c ← also: PROPS
  +5	-6	tests/unit/igraph_convex_hull_2d.c
  +11	-3	tests/unit/igraph_correlated_game.c ← also: GAMES
  +1	-1	tests/unit/igraph_correlated_pair_game.c
  +1	-1	tests/unit/igraph_count_adjacent_triangles.c
  +3	-3	tests/unit/igraph_create.c
  +2	-3	tests/unit/igraph_decompose_strong.c
  +40	-16	tests/unit/igraph_degree.c ← also: PROPS
  +9	-6	tests/unit/igraph_degree.out ← also: PROPS
  +21	-20	tests/unit/igraph_degree_sequence_game.c ← also: GAMES
  +217	-0	tests/unit/igraph_delaunay_graph.c ← also: SPATIAL
  +713	-0	tests/unit/igraph_delaunay_graph.out ← also: SPATIAL
  +1	-1	tests/unit/igraph_delete_edges.c
  +1	-1	tests/unit/igraph_delete_vertices.c
  +84	-25	tests/unit/igraph_density.c ← also: PROPS
  +11	-15	tests/unit/igraph_diameter.c ← also: PROPS
  +5	-6	tests/unit/igraph_diameter_dijkstra.c ← also: PROPS
  +2	-3	tests/unit/igraph_disjoint_union.c
  +4	-4	tests/unit/igraph_distances_floyd_warshall.c ← also: PATHS
  +5	-5	tests/unit/igraph_distances_floyd_warshall_speedup.c ← also: PATHS
  +45	-17	tests/unit/igraph_distances_johnson.c ← also: PATHS
  +19	-2	tests/unit/igraph_distances_johnson.out ← also: PATHS
  +0	-1	tests/unit/igraph_diversity.c
  +1	-1	tests/unit/igraph_dominator_tree.c
  +1	-1	tests/unit/igraph_dot_product_game.c
  +1	-1	tests/unit/igraph_dyad_census.c
  +15	-15	tests/unit/igraph_ecc.c
  +9	-9	tests/unit/igraph_eccentricity.c ← also: PROPS
  +5	-5	tests/unit/igraph_eccentricity_dijkstra.c ← also: PROPS
  +101	-19	tests/unit/igraph_edge_betweenness.c ← also: CENTRALITY
  +8	-0	tests/unit/igraph_edge_betweenness.out ← also: CENTRALITY
  +62	-64	tests/unit/igraph_edge_betweenness_subset.c ← also: CENTRALITY
  +2	-2	tests/unit/igraph_edge_disjoint_paths.c
  +10	-3	tests/unit/igraph_edges.c
  +6	-3	tests/unit/igraph_edges.out
  +3	-4	tests/unit/igraph_eigen_matrix.c ← also: DS-MATRIX
  +1	-2	tests/unit/igraph_eigen_matrix2.c ← also: DS-MATRIX
  +1	-2	tests/unit/igraph_eigen_matrix3.c ← also: DS-MATRIX
  +1	-2	tests/unit/igraph_eigen_matrix4.c ← also: DS-MATRIX
  +3	-4	tests/unit/igraph_eigen_matrix_symmetric.c ← also: DS-MATRIX
  +3	-4	tests/unit/igraph_eigen_matrix_symmetric_arpack.c ← also: DS-MATRIX
  +63	-24	tests/unit/igraph_eigenvector_centrality.c ← also: CENTRALITY
  +30	-0	tests/unit/igraph_eigenvector_centrality.out ← also: CENTRALITY
  +1	-2	tests/unit/igraph_empty.c
  +15	-16	tests/unit/igraph_es_all_between.c
  +6	-7	tests/unit/igraph_es_path.c
  +1	-1	tests/unit/igraph_establishment_game.c
  +1	-1	tests/unit/igraph_extended_chordal_ring.c
  +11	-11	tests/unit/igraph_feedback_arc_set.c
  +7	-7	tests/unit/igraph_feedback_vertex_set.c
  +1	-1	tests/unit/igraph_forest_fire_game.c
  +4	-4	tests/unit/igraph_from_prufer.c
  +11	-11	tests/unit/igraph_full_bipartite.c
  +2	-2	tests/unit/igraph_full_citation.c
  +1	-1	tests/unit/igraph_full_multipartite.c
  +1	-1	tests/unit/igraph_generalized_petersen.c
  +5	-5	tests/unit/igraph_get_adjacency.c ← also: CONSTRUCTORS
  +6	-5	tests/unit/igraph_get_adjacency_sparse.c ← also: CONSTRUCTORS
  +8	-8	tests/unit/igraph_get_all_shortest_paths_dijkstra.c ← also: PATHS
  +30	-21	tests/unit/igraph_get_all_simple_paths.c ← also: PATHS
  +81	-10	tests/unit/igraph_get_all_simple_paths.out ← also: PATHS
  +3	-3	tests/unit/igraph_get_biadjacency.c ← also: CONSTRUCTORS
  +2	-2	tests/unit/igraph_get_eid.c
  +5	-5	tests/unit/igraph_get_isomorphisms_vf2.c
  +4	-4	tests/unit/igraph_get_k_shortest_paths.c ← also: PATHS
  +1	-2	tests/unit/igraph_get_laplacian.c
  +16	-16	tests/unit/igraph_get_shortest_path_astar.c ← also: PATHS
  +1	-1	tests/unit/igraph_get_shortest_path_bellman_ford.c ← also: PATHS
  +7	-8	tests/unit/igraph_get_shortest_paths2.c ← also: PATHS
  +20	-21	tests/unit/igraph_get_shortest_paths_bellman_ford.c ← also: PATHS
  +18	-19	tests/unit/igraph_get_shortest_paths_dijkstra.c ← also: PATHS
  +3	-3	tests/unit/igraph_get_stochastic.c
  +1	-1	tests/unit/igraph_get_stochastic_sparse.c
  +5	-5	tests/unit/igraph_get_subisomorphisms_vf2.c
  +5	-6	tests/unit/igraph_gomory_hu_tree.c
  +50	-50	tests/unit/igraph_graph_center.c
  +1	-1	tests/unit/igraph_graph_center.out
  +2	-2	tests/unit/igraph_graph_power.c
  +1	-1	tests/unit/igraph_grg_game.c
  +2	-2	tests/unit/igraph_growing_random_game.c
  +1	-1	tests/unit/igraph_has_mutual.c
  +1	-1	tests/unit/igraph_hexagonal_lattice.c
  +9	-6	tests/unit/igraph_hrg.c
  +2	-2	tests/unit/igraph_hrg2.c
  +2	-2	tests/unit/igraph_hrg3.c
  +1	-1	tests/unit/igraph_hrg_create.c
  +2	-2	tests/unit/igraph_hsbm_game.c ← also: GAMES
  +2	-2	tests/unit/igraph_hsbm_list_game.c
  +8	-9	tests/unit/igraph_i_incident.c => tests/unit/igraph_incident.c ← also: ITERATORS
  +2	-1	tests/unit/igraph_i_incident.out => tests/unit/igraph_incident.out ← also: ITERATORS
  +2	-7	tests/unit/igraph_i_layout_sphere.c
  +0	-122	tests/unit/igraph_i_neighbors.c ← also: ITERATORS
  +26	-1	tests/unit/igraph_i_neighbors.out => tests/unit/igraph_neighbors.out ← also: ITERATORS
  +1	-6	tests/unit/igraph_i_umap_fit_ab.c
  +0	-8	tests/unit/igraph_i_umap_fit_ab.o
  +8	-0	tests/unit/igraph_i_umap_fit_ab.out
  +1	-2	tests/unit/igraph_induced_subgraph.c
  +1	-1	tests/unit/igraph_induced_subgraph_edges.c
  +2	-3	tests/unit/igraph_induced_subgraph_map.c
  +1	-1	tests/unit/igraph_induced_subgraph_map.out
  +1	-2	tests/unit/igraph_intersection.c
  +1	-1	tests/unit/igraph_is_acyclic.c
  +1	-1	tests/unit/igraph_is_biconnected.c
  +1	-1	tests/unit/igraph_is_chordal.c
  +1	-1	tests/unit/igraph_is_clique.c
  +5	-5	tests/unit/igraph_is_complete.c
  +1	-1	tests/unit/igraph_is_connected.c
  +3	-3	tests/unit/igraph_is_dag.c
  +1	-1	tests/unit/igraph_is_forest.c
  +9	-13	tests/unit/igraph_is_forest2.c
  +2	-2	tests/unit/igraph_is_mutual.c
  +1	-1	tests/unit/igraph_is_same_graph.c
  +3	-3	tests/unit/igraph_is_separator.c
  +1	-1	tests/unit/igraph_is_tree.c
  +1	-1	tests/unit/igraph_isomorphic.c ← also: ISO
  +1	-2	tests/unit/igraph_isomorphic_bliss.c ← also: ISO
  +7	-4	tests/unit/igraph_isomorphic_vf2.c ← also: ISO
  +1	-2	tests/unit/igraph_join.c
  +37	-34	tests/unit/igraph_joint_degree_distribution.c ← also: PROPS
  +4	-4	tests/unit/igraph_joint_type_distribution.c
  +22	-23	tests/unit/igraph_k_regular_game.c ← also: GAMES
  +1	-1	tests/unit/igraph_kautz.c
  +11	-11	tests/unit/igraph_lapack_dgeev.c
  +14	-14	tests/unit/igraph_lapack_dgeevx.c
  +1	-2	tests/unit/igraph_lapack_dgehrd.c
  +1	-1	tests/unit/igraph_lapack_dgetrf.c
  +2	-2	tests/unit/igraph_lapack_dgetrs.c
  +7	-8	tests/unit/igraph_lapack_dsyevr.c
  +1	-1	tests/unit/igraph_lastcit_game.c
  +2	-2	tests/unit/igraph_layout_align.c
  +1	-1	tests/unit/igraph_layout_bipartite.c
  +2	-2	tests/unit/igraph_layout_davidson_harel.c
  +1	-1	tests/unit/igraph_layout_drl.c
  +1	-1	tests/unit/igraph_layout_drl_3d.c
  +1	-1	tests/unit/igraph_layout_fruchterman_reingold.c
  +1	-1	tests/unit/igraph_layout_fruchterman_reingold_3d.c
  +2	-2	tests/unit/igraph_layout_gem.c
  +1	-1	tests/unit/igraph_layout_graphopt.c
  +1	-2	tests/unit/igraph_layout_grid.c
  +1	-1	tests/unit/igraph_layout_kamada_kawai.c
  +2	-3	tests/unit/igraph_layout_lgl.c
  +2	-7	tests/unit/igraph_layout_mds.c
  +3	-4	tests/unit/igraph_layout_merge.c
  +2	-3	tests/unit/igraph_layout_merge2.c
  +2	-3	tests/unit/igraph_layout_merge3.c
  +1	-1	tests/unit/igraph_layout_random_3d.c
  +1	-1	tests/unit/igraph_layout_reingold_tilford_circular.c
  +2	-3	tests/unit/igraph_layout_reingold_tilford_extended.c
  +1	-1	tests/unit/igraph_layout_sphere.c
  +2	-2	tests/unit/igraph_layout_star.c
  +81	-29	tests/unit/igraph_layout_sugiyama.c ← also: LAYOUT
  +169	-87	tests/unit/igraph_layout_sugiyama.out ← also: LAYOUT
  +11	-11	tests/unit/igraph_layout_umap.c
  +69	-0	tests/unit/igraph_lcf.c ← also: CONSTRUCTORS
  +1	-1	tests/unit/igraph_le_community_to_membership.c
  +1	-1	tests/unit/igraph_linegraph.c
  +1	-1	tests/unit/igraph_list_triangles.c
  +1	-1	tests/unit/igraph_local_scan_k_ecount.c
  +1	-1	tests/unit/igraph_local_scan_k_ecount_them.c
  +1	-1	tests/unit/igraph_local_scan_subset_ecount.c
  +7	-8	tests/unit/igraph_local_transitivity.c
  +18	-18	tests/unit/igraph_maxflow.c
  +24	-16	tests/unit/igraph_maximal_cliques.c ← also: CLIQUES
  +9	-8	tests/unit/igraph_maximal_cliques2.c ← also: CLIQUES
  +5	-5	tests/unit/igraph_maximal_cliques3.c ← also: CLIQUES
  +10	-8	tests/unit/igraph_maximal_cliques4.c ← also: CLIQUES
  +5	-5	tests/unit/igraph_maximal_cliques_file.c ← also: CLIQUES
  +7	-7	tests/unit/igraph_maximum_bipartite_matching.c
  +1	-1	tests/unit/igraph_mean_degree.c ← also: PROPS
  +24	-20	tests/unit/igraph_minimum_size_separators.c ← also: CONNECTIVITY
  +49	-24	tests/unit/igraph_minimum_size_separators.out ← also: CONNECTIVITY
  +1	-2	tests/unit/igraph_modularity.c
  +2	-2	tests/unit/igraph_modularity_matrix.c ← also: DS-MATRIX
  +4	-5	tests/unit/igraph_motifs_randesu.c ← also: MISC
  +5	-5	tests/unit/igraph_motifs_randesu_estimate.c ← also: MISC
  +4	-4	tests/unit/igraph_motifs_randesu_no.c ← also: MISC
  +278	-0	tests/unit/igraph_nearest_neighbor_graph.c ← also: SPATIAL
  +809	-0	tests/unit/igraph_nearest_neighbor_graph.out ← also: SPATIAL
  +1	-1	tests/unit/igraph_neighborhood.c
  +2	-2	tests/unit/igraph_neighborhood_graphs.c
  +1	-1	tests/unit/igraph_neighborhood_size.c
  +155	-12	tests/unit/igraph_neighbors.c ← also: ITERATORS
  +74	-75	tests/unit/igraph_pagerank.c ← also: CENTRALITY
  +1	-1	tests/unit/igraph_path_length_hist.c
  +3	-4	tests/unit/igraph_perfect.c
  +1	-1	tests/unit/igraph_permute_vertices.c
  +3	-4	tests/unit/igraph_power_law_fit.c
  +2	-3	tests/unit/igraph_preference_game.c
  +10	-10	tests/unit/igraph_product.c
  +1	-1	tests/unit/igraph_progress_handler_stderr.c
  +6	-6	tests/unit/igraph_pseudo_diameter.c ← also: PROPS
  +8	-8	tests/unit/igraph_pseudo_diameter_dijkstra.c ← also: PROPS
  +3	-3	tests/unit/igraph_random_sample.c
  +6	-6	tests/unit/igraph_random_walk.c
  +1	-2	tests/unit/igraph_read_graph_graphdb.c
  +4	-5	tests/unit/igraph_read_graph_graphml.c
  +19	-19	tests/unit/igraph_realize_bipartite_degree_sequence.c ← also: PROPS
  +1	-1	tests/unit/igraph_recent_degree_aging_game.c ← also: PROPS
  +1	-1	tests/unit/igraph_recent_degree_game.c ← also: PROPS
  +7	-7	tests/unit/igraph_reindex_membership.c
  +1	-1	tests/unit/igraph_residual_graph.c
  +1	-1	tests/unit/igraph_reverse_edges.c
  +8	-9	tests/unit/igraph_rewire.c ← also: OPERATORS
  +2	-2	tests/unit/igraph_rewire_directed_edges.c ← also: OPERATORS
  +9	-10	tests/unit/igraph_rng_get_integer.c
  +1	-1	tests/unit/igraph_rooted_product.c
  +1	-1	tests/unit/igraph_running_mean.c
  +9	-9	tests/unit/igraph_sample_dirichlet.c => tests/unit/igraph_rng_sample_dirichlet.c ← also: SAMPLING
  +0	-0	tests/unit/igraph_sample_dirichlet.out => tests/unit/igraph_rng_sample_dirichlet.out ← also: SAMPLING
  +6	-6	tests/unit/igraph_sample_sphere.c => tests/unit/igraph_rng_sample_sphere.c ← also: SAMPLING
  +69	-19	tests/unit/igraph_sbm_game.c ← also: GAMES
  +0	-1	tests/unit/igraph_sbm_game.out ← also: GAMES
  +1	-1	tests/unit/igraph_set_progress_handler.c
  +11	-8	tests/unit/igraph_similarity.c ← also: MISC
  +2	-0	tests/unit/igraph_similarity.out ← also: MISC
  +10	-10	tests/unit/igraph_simple_cycles.c
  +1	-1	tests/unit/igraph_simple_interconnected_islands_game.c
  +4	-4	tests/unit/igraph_sir.c
  +1	-1	tests/unit/igraph_solve_lsap.c
  +12	-12	tests/unit/igraph_spanner.c
  +8	-13	tests/unit/igraph_sparsemat2.c ← also: DS-SPARSEMAT
  +2	-3	tests/unit/igraph_sparsemat5.c ← also: DS-SPARSEMAT
  +1	-2	tests/unit/igraph_sparsemat9.c ← also: DS-SPARSEMAT
  +1	-1	tests/unit/igraph_sparsemat_droptol.c ← also: DS-SPARSEMAT
  +3	-3	tests/unit/igraph_sparsemat_fkeep.c ← also: DS-SPARSEMAT
  +1	-1	tests/unit/igraph_sparsemat_getelements_sorted.c ← also: DS-SPARSEMAT
  +1	-2	tests/unit/igraph_sparsemat_is_symmetric.c ← also: DS-SPARSEMAT
  +1	-1	tests/unit/igraph_sparsemat_iterator_idx.c ← also: DS-SPARSEMAT
  +2	-3	tests/unit/igraph_sparsemat_minmax.c ← also: DS-SPARSEMAT
  +1	-1	tests/unit/igraph_sparsemat_nonzero_storage.c ← also: DS-SPARSEMAT
  +1	-1	tests/unit/igraph_sparsemat_normalize.c ← also: DS-SPARSEMAT
  +0	-47	tests/unit/igraph_sparsemat_view.c ← also: DS-SPARSEMAT
  +3	-4	tests/unit/igraph_sparsemat_which_minmax.c ← also: DS-SPARSEMAT
  +64	-0	tests/unit/igraph_spatial_edge_lengths.c ← also: SPATIAL
  +7	-0	tests/unit/igraph_spatial_edge_lengths.out ← also: SPATIAL
  +2	-2	tests/unit/igraph_split_join_distance.c
  +6	-7	tests/unit/igraph_square_lattice.c
  +2	-2	tests/unit/igraph_st_edge_connectivity.c
  +1	-1	tests/unit/igraph_st_mincut.c
  +1	-1	tests/unit/igraph_st_mincut_value.c
  +4	-4	tests/unit/igraph_st_vertex_connectivity.c
  +13	-13	tests/unit/igraph_static_power_law_game.c
  +10	-4	tests/unit/igraph_strvector.c ← also: DS-STRVECTOR
  +14	-0	tests/unit/igraph_strvector.out ← also: DS-STRVECTOR
  +3	-3	tests/unit/igraph_subcomponent.c
  +1	-1	tests/unit/igraph_subisomorphic.c ← also: ISO
  +16	-14	tests/unit/igraph_subisomorphic_lad.c ← also: ISO
  +11	-17	tests/unit/igraph_to_prufer.c
  +2	-2	tests/unit/igraph_transitive_closure.c
  +1	-1	tests/unit/igraph_transitivity_avglocal_undirected.c
  +1	-1	tests/unit/igraph_transitivity_barrat.c
  +1	-1	tests/unit/igraph_triangular_lattice.c
  +4	-6	tests/unit/igraph_trussness.c
  +1	-2	tests/unit/igraph_turan.c
  +1	-1	tests/unit/igraph_unfold_tree.c
  +7	-8	tests/unit/igraph_union.c
  +1	-1	tests/unit/igraph_vector_floor.c ← also: DS-VECTOR
  +1	-1	tests/unit/igraph_vector_lex_cmp.c ← also: DS-VECTOR
  +2	-2	tests/unit/igraph_vertex_disjoint_paths.c
  +2	-2	tests/unit/igraph_voronoi.c
  +24	-33	tests/unit/igraph_weighted_adjacency.c ← also: CONSTRUCTORS
  +85	-92	tests/unit/igraph_weighted_adjacency.out ← also: CONSTRUCTORS
  +108	-0	tests/unit/igraph_weighted_biadjacency.c ← also: CONSTRUCTORS
  +75	-0	tests/unit/igraph_weighted_biadjacency.out ← also: CONSTRUCTORS
  +18	-18	tests/unit/igraph_weighted_cliques.c ← also: CLIQUES
  +3	-3	tests/unit/igraph_wheel.c
  +3	-3	tests/unit/igraph_write_graph_dimacs_flow.c
  +1	-1	tests/unit/igraph_write_graph_dot.c
  +1	-2	tests/unit/igraph_write_graph_leda.c
  +1	-1	tests/unit/inclist.c
  +1	-1	tests/unit/is_coloring.c
  +22	-23	tests/unit/isoclasses.c
  +19	-19	tests/unit/isoclasses2.c
  +16	-22	tests/unit/isomorphism_test.c
  +1	-1	tests/unit/jdm.c
  +1	-1	tests/unit/kary_tree.c
  +4	-5	tests/unit/knn.c
  +4	-5	tests/unit/levc-stress.c
  +2	-3	tests/unit/lineendings.c
  +2	-3	tests/unit/marked_queue.c
  +2	-3	tests/unit/matrix.c ← also: DS-MATRIX
  +4	-5	tests/unit/matrix2.c ← also: DS-MATRIX
  +1	-2	tests/unit/matrix3.c ← also: DS-MATRIX
  +8	-9	tests/unit/matrix_complex.c ← also: DS-MATRIX
  +240	-0	tests/unit/max_results.c ← also: CLIQUES
  +5	-5	tests/unit/maximal_cliques_callback.c ← also: CLIQUES
  +1	-1	tests/unit/maximal_cliques_hist.c ← also: CLIQUES
  +88	-0	tests/unit/minimum_spanning_tree.c ← also: MISC
  +14	-0	tests/unit/minimum_spanning_tree.out ← also: MISC
  +1	-1	tests/unit/mycielskian.c
  +1	-1	tests/unit/ncol.c
  +23	-10	tests/unit/null_communities.c ← also: COMM
  +2	-2	tests/unit/overflow.c
  +3	-4	tests/unit/pajek.c ← also: IO
  +1	-2	tests/unit/pajek2.c ← also: IO
  +2	-3	tests/unit/pajek_bipartite.c ← also: IO
  +1	-2	tests/unit/pajek_bipartite2.c ← also: IO
  +30	-30	tests/unit/pajek_bipartite2.out ← also: IO
  +1	-2	tests/unit/pajek_signed.c ← also: IO
  +10	-10	tests/unit/pajek_signed.out ← also: IO
  +1	-1	tests/unit/paths.c
  +17	-17	tests/unit/percolation.c
  +11	-2	tests/unit/prop_caching.c ← also: GRAPH
  +5	-5	tests/unit/random_sampling.c
  +1	-1	tests/unit/random_spanning_tree.c ← also: MISC
  +2	-2	tests/unit/reachability.c
  +13	-13	tests/unit/rich_club.c
  +1	-2	tests/unit/ring.c
  +3	-4	tests/unit/rng_init_destroy_max_bits_name_set_default.c
  +1	-1	tests/unit/rng_reproducibility.c
  +4	-5	tests/unit/set.c
  +1	-1	tests/unit/simplify_and_colorize.c
  +5	-6	tests/unit/single_target_shortest_path.c ← also: PATHS
  +3	-6	tests/unit/spinglass.c
  +1	-2	tests/unit/stack.c
  +5	-5	tests/unit/strvector_set_len_remove_print.c ← also: DS-STRVECTOR
  +1	-1	tests/unit/symmetric_tree.c
  +110	-74	tests/unit/test_utilities.c
  +16	-6	tests/unit/test_utilities.h
  +1	-2	tests/unit/tls1.c
  +1	-2	tests/unit/tls2.c
  +1	-2	tests/unit/topological_sorting.c
  +6	-6	tests/unit/tree_game.c
  +5	-12	tests/unit/triad_census.c
  +3	-4	tests/unit/trie.c
  +25	-39	tests/unit/vector.c ← also: DS-VECTOR
  +4	-7	tests/unit/vector.out ← also: DS-VECTOR
  +12	-4	tests/unit/vector2.c ← also: DS-VECTOR
  +5	-2	tests/unit/vector2.out ← also: DS-VECTOR
  +1	-2	tests/unit/vector3.c ← also: DS-VECTOR
  +22	-22	tests/unit/vector4.c ← also: DS-VECTOR
  +2	-3	tests/unit/vector_list.c ← also: DS-VECTOR
  +2	-3	tests/unit/vector_ptr.c ← also: DS-VECTOR
  +1	-2	tests/unit/vector_ptr_sort_ind.c ← also: DS-VECTOR
  +3	-4	tests/unit/vector_sort_ind.c ← also: DS-VECTOR
  +1	-1	tests/unit/vertex_selectors.c
  +7	-7	tests/unit/watts_strogatz_game.c
  +7	-7	tests/unit/widest_paths.c
  +1	-1	tests/unit/zapsmall.c
  +1	-1	tests/unit/zero_allocs.c

### EXAMPLE: Example code updates (157 files)

  +4	-3	examples/simple/adjlist.c
  +7	-5	examples/simple/bellman_ford.c
  +3	-0	examples/simple/blas.c
  +3	-0	examples/simple/blas_dgemm.c
  +5	-3	examples/simple/cattributes.c ← also: ATTRS
  +4	-2	examples/simple/cattributes2.c ← also: ATTRS
  +4	-2	examples/simple/cattributes3.c ← also: ATTRS
  +4	-2	examples/simple/cattributes4.c ← also: ATTRS
  +6	-5	examples/simple/centralization.c
  +5	-3	examples/simple/cohesive_blocks.c
  +5	-2	examples/simple/coloring.c
  +3	-0	examples/simple/creation.c
  +10	-11	examples/simple/distances.c
  +4	-2	examples/simple/dominator_tree.c
  +4	-3	examples/simple/dot.c
  +4	-2	examples/simple/dqueue.c
  +6	-4	examples/simple/eigenvector_centrality.c ← also: CENTRALITY
  +5	-5	examples/simple/even_tarjan.c
  +5	-3	examples/simple/flow.c
  +10	-7	examples/simple/flow2.c
  +4	-2	examples/simple/foreign.c
  +4	-2	examples/simple/gml.c
  +4	-1	examples/simple/graphml.c
  +6	-4	examples/simple/igraph_all_st_mincuts.c
  +5	-2	examples/simple/igraph_assortativity_degree.c ← also: PROPS
  +10	-7	examples/simple/igraph_assortativity_nominal.c
  +4	-3	examples/simple/igraph_atlas.c
  +3	-1	examples/simple/igraph_attribute_combination.c
  +7	-3	examples/simple/igraph_average_path_length.c
  +4	-2	examples/simple/igraph_avg_nearest_neighbor_degree.c ← also: SPATIAL
  +8	-6	examples/simple/igraph_barabasi_game.c
  +7	-6	examples/simple/igraph_barabasi_game2.c
  +4	-2	examples/simple/igraph_bfs.c
  +9	-7	examples/simple/igraph_bfs_callback.c
  +4	-3	examples/simple/igraph_bfs_simple.c
  +9	-6	examples/simple/igraph_biconnected_components.c
  +9	-10	examples/simple/igraph_bipartite_create.c
  +4	-1	examples/simple/igraph_bipartite_projection.c
  +13	-11	examples/simple/igraph_cliques.c ← also: CLIQUES
  +4	-2	examples/simple/igraph_cocitation.c
  +10	-5	examples/simple/igraph_community_edge_betweenness.c ← also: COMM
  +7	-4	examples/simple/igraph_community_edge_betweenness.out ← also: COMM
  +9	-5	examples/simple/igraph_community_fastgreedy.c
  +8	-7	examples/simple/igraph_community_label_propagation.c ← also: COMM
  +29	-27	examples/simple/igraph_community_leading_eigenvector.c ← also: DS-VECTOR
  +68	-24	examples/simple/igraph_community_leiden.c ← also: COMM-LEIDEN
  +3	-0	examples/simple/igraph_community_leiden.out ← also: COMM-LEIDEN
  +7	-4	examples/simple/igraph_community_multilevel.c
  +22	-75	examples/simple/igraph_community_optimal_modularity.c ← also: COMM
  +2	-0	examples/simple/igraph_community_optimal_modularity.out ← also: COMM
  +4	-2	examples/simple/igraph_complementer.c
  +4	-2	examples/simple/igraph_compose.c
  +5	-2	examples/simple/igraph_contract_vertices.c
  +4	-2	examples/simple/igraph_copy.c
  +4	-2	examples/simple/igraph_create.c
  +10	-10	examples/simple/igraph_decompose.c
  +5	-4	examples/simple/igraph_degree.c ← also: PROPS
  +30	-10	examples/simple/igraph_degree_sequence_game.c ← also: GAMES
  +4	-2	examples/simple/igraph_delete_edges.c
  +1	-2	examples/simple/igraph_delete_vertices.c
  +0	-172	examples/simple/igraph_deterministic_optimal_imitation.c
  +34	-23	examples/simple/igraph_diameter.c ← also: PROPS
  +2	-2	examples/simple/igraph_diameter.out ← also: PROPS
  +4	-3	examples/simple/igraph_difference.c
  +5	-3	examples/simple/igraph_disjoint_union.c
  +23	-3	examples/simple/igraph_eccentricity.c ← also: PROPS
  +22	-3	examples/simple/igraph_erdos_renyi_game_gnm.c ← also: GAMES-ER
  +22	-3	examples/simple/igraph_erdos_renyi_game_gnp.c ← also: GAMES-ER
  +6	-5	examples/simple/igraph_es_pairs.c
  +4	-3	examples/simple/igraph_feedback_arc_set.c
  +5	-3	examples/simple/igraph_feedback_arc_set_ip.c
  +10	-9	examples/simple/igraph_fisher_yates_shuffle.c
  +6	-4	examples/simple/igraph_full.c
  +6	-7	examples/simple/igraph_get_all_shortest_paths_dijkstra.c ← also: PATHS
  +20	-23	examples/simple/igraph_get_eid.c
  +34	-44	examples/simple/igraph_get_eids.c
  +15	-11	examples/simple/igraph_get_laplacian.c
  +4	-2	examples/simple/igraph_get_laplacian_sparse.c
  +17	-15	examples/simple/igraph_get_shortest_paths.c ← also: PATHS
  +6	-5	examples/simple/igraph_get_shortest_paths_dijkstra.c ← also: PATHS
  +7	-5	examples/simple/igraph_girth.c
  +8	-5	examples/simple/igraph_grg_game.c
  +4	-2	examples/simple/igraph_has_multiple.c
  +18	-10	examples/simple/igraph_independent_sets.c ← also: CLIQUES
  +5	-0	examples/simple/igraph_independent_sets.out ← also: CLIQUES
  +6	-4	examples/simple/igraph_intersection.c
  +4	-1	examples/simple/igraph_is_biconnected.c
  +4	-2	examples/simple/igraph_is_directed.c
  +5	-3	examples/simple/igraph_is_loop.c
  +4	-2	examples/simple/igraph_is_minimal_separator.c
  +5	-3	examples/simple/igraph_is_multiple.c
  +4	-2	examples/simple/igraph_is_separator.c
  +9	-6	examples/simple/igraph_isomorphic_vf2.c ← also: ISO
  +4	-2	examples/simple/igraph_join.c
  +4	-2	examples/simple/igraph_kary_tree.c
  +4	-3	examples/simple/igraph_lapack_dgeev.c
  +4	-3	examples/simple/igraph_lapack_dgeevx.c
  +4	-2	examples/simple/igraph_lapack_dgesv.c
  +4	-3	examples/simple/igraph_lapack_dsyevr.c
  +8	-10	examples/simple/igraph_layout_reingold_tilford.c
  +28	-61	examples/simple/igraph_lcf.c ← also: CONSTRUCTORS
  +3	-0	examples/simple/igraph_lcf.out ← also: CONSTRUCTORS
  +7	-3	examples/simple/igraph_list_triangles.c
  +11	-9	examples/simple/igraph_maximal_cliques.c ← also: CLIQUES
  +3	-5	examples/simple/igraph_maximum_bipartite_matching.c
  +9	-7	examples/simple/igraph_mincut.c
  +5	-3	examples/simple/igraph_minimal_separators.c
  +3	-3	examples/simple/igraph_minimum_size_separators.c ← also: CONNECTIVITY
  +9	-6	examples/simple/igraph_minimum_spanning_tree.c ← also: MISC
  +1	-1	examples/simple/igraph_minimum_spanning_tree.out ← also: MISC
  +8	-5	examples/simple/igraph_motifs_randesu.c ← also: MISC
  +7	-6	examples/simple/igraph_neighbors.c ← also: ITERATORS
  +6	-3	examples/simple/igraph_pagerank.c ← also: CENTRALITY
  +4	-2	examples/simple/igraph_power_law_fit.c
  +7	-5	examples/simple/igraph_radius.c
  +4	-4	examples/simple/igraph_random_sample.c
  +4	-2	examples/simple/igraph_read_graph_dl.c
  +4	-3	examples/simple/igraph_read_graph_graphdb.c
  +4	-2	examples/simple/igraph_read_graph_lgl.c
  +4	-1	examples/simple/igraph_realize_degree_sequence.c ← also: PROPS
  +4	-2	examples/simple/igraph_reciprocity.c
  +4	-1	examples/simple/igraph_regular_tree.c
  +4	-1	examples/simple/igraph_ring.c
  +0	-213	examples/simple/igraph_roulette_wheel_imitation.c
  +7	-6	examples/simple/igraph_similarity.c ← also: MISC
  +4	-2	examples/simple/igraph_simplify.c
  +4	-2	examples/simple/igraph_small.c
  +5	-3	examples/simple/igraph_sparsemat.c ← also: DS-SPARSEMAT
  +27	-29	examples/simple/igraph_sparsemat3.c ← also: DS-SPARSEMAT
  +23	-21	examples/simple/igraph_sparsemat4.c ← also: DS-SPARSEMAT
  +7	-5	examples/simple/igraph_sparsemat6.c ← also: DS-SPARSEMAT
  +4	-2	examples/simple/igraph_sparsemat7.c ← also: DS-SPARSEMAT
  +4	-3	examples/simple/igraph_sparsemat8.c ← also: DS-SPARSEMAT
  +4	-1	examples/simple/igraph_star.c
  +0	-182	examples/simple/igraph_stochastic_imitation.c
  +5	-3	examples/simple/igraph_strvector.c ← also: DS-STRVECTOR
  +9	-7	examples/simple/igraph_subisomorphic_lad.c ← also: ISO
  +3	-0	examples/simple/igraph_symmetric_tree.c
  +4	-2	examples/simple/igraph_to_undirected.c
  +4	-2	examples/simple/igraph_topological_sorting.c
  +4	-2	examples/simple/igraph_transitivity.c
  +4	-2	examples/simple/igraph_union.c
  +7	-4	examples/simple/igraph_vector_int_list_sort.c ← also: DS-VECTOR
  +4	-3	examples/simple/igraph_version.c
  +5	-3	examples/simple/igraph_vs_nonadj.c
  +5	-3	examples/simple/igraph_vs_range.c
  +11	-8	examples/simple/igraph_vs_vector.c ← also: DS-VECTOR
  +37	-22	examples/simple/igraph_weighted_adjacency.c ← also: CONSTRUCTORS
  +5	-5	examples/simple/igraph_weighted_adjacency.out ← also: CONSTRUCTORS
  +5	-2	examples/simple/igraph_write_graph_lgl.c
  +5	-4	examples/simple/igraph_write_graph_pajek.c ← also: IO
  +5	-4	examples/simple/random_seed.c
  +3	-0	examples/simple/safelocale.c
  +6	-4	examples/simple/walktrap.c
  +29	-25	examples/tutorial/tutorial1.c
  +41	-33	examples/tutorial/tutorial2.c
  +49	-44	examples/tutorial/tutorial3.c

### FUZZ: Fuzzing harness updates (27 files)

  +5	-2	fuzzing/basic_properties_directed.cpp
  +5	-2	fuzzing/basic_properties_undirected.cpp
  +4	-4	fuzzing/bliss.cpp ← also: ISO
  +4	-4	fuzzing/build.sh
  +17	-10	fuzzing/centrality.cpp
  +14	-7	fuzzing/community.cpp
  +2	-2	fuzzing/edge_connectivity.cpp
  +13	-13	fuzzing/linear_algos_directed.cpp
  +53	-14	fuzzing/linear_algos_undirected.cpp
  +7	-3	fuzzing/misc_algos.cpp
  +12	-11	fuzzing/misc_algos_weighted.cpp
  +2	-2	fuzzing/read_dimacs_flow.cpp
  +1	-1	fuzzing/read_dl.cpp
  +1	-1	fuzzing/read_edgelist.cpp
  +1	-1	fuzzing/read_gml.cpp
  +1	-1	fuzzing/read_graphdb.cpp
  +1	-1	fuzzing/read_graphml.cpp
  +1	-1	fuzzing/read_lgl.cpp
  +1	-1	fuzzing/read_ncol.cpp
  +1	-1	fuzzing/read_pajek.cpp ← also: IO
  +35	-5	fuzzing/spatial.cpp
  +2	-2	fuzzing/vertex_connectivity.cpp
  +5	-5	fuzzing/vertex_separators.cpp
  +20	-11	fuzzing/weighted_centrality.cpp
  +9	-6	fuzzing/weighted_community.cpp
  +1	-1	fuzzing/write_all_gml.cpp
  +1	-1	fuzzing/write_all_graphml.cpp

### OTHER-SRC: Other source changes (4 files)

  +5	-18	include/igraph_conversion.h
  +5	-10	include/igraph_eulerian.h
  +1	-1	src/core/math.h
  +69	-39	src/core/typed_list.pmt

## Flat Annotated `git diff --numstat`

```
+45	-0	.all-contributorsrc	[CONTRIBUTORS]
+1	-0	.gitignore	[META]
+39	-2	ACKNOWLEDGEMENTS.md	[CONTRIBUTORS]
+276	-0	CHANGELOG.md	[CHANGELOG]
+213	-0	CHANGELOG_PROOF_OF_WORK.md	[CHANGELOG]
+2	-2	CMakeLists.txt	[BUILD-CMAKE]
+12	-10	CONTRIBUTING.md	[META]
+7	-0	CONTRIBUTORS.md	[CONTRIBUTORS]
+5	-0	CONTRIBUTORS.txt	[CONTRIBUTORS]
+3	-3	README.md	[META]
+58	-0	VERSIONING.md	[VERSIONING-POLICY]
+11	-10	azure-pipelines.yml	[BUILD-CI]
+1	-0	codecov.yml	[BUILD-CI]
+4	-2	doc/CMakeLists.txt	[DOC]
+18	-1	doc/attributes.xxml	[DOC]
+32	-10	doc/basicigraph.xxml	[DOC]
+2	-6	doc/bipartite.xxml	[DOC]
+1	-0	doc/community.xxml	[DOC]
+10	-3	doc/cycles.xxml	[DOC]
+1	-1	doc/doxrox.py	[DOC]
+0	-5	doc/foreign.xxml	[DOC]
+85	-0	doc/games.xxml	[DOC]
+52	-54	doc/generators.xxml	[DOC]
+20	-16	doc/igraph-docs.xml	[DOC]
+9	-0	doc/installation.xml	[DOC]
+6	-16	doc/isomorphism.xxml	[DOC]
+0	-7	doc/iterators.xxml	[DOC]
+1	-1	doc/arpack.xxml => doc/linalg.xxml	[DOC]
+0	-6	doc/matrix.xxml	[DOC]
+0	-4	doc/motifs.xxml	[DOC]
+3	-11	doc/nongraph.xxml	[DOC]
+0	-4	doc/operators.xxml	[DOC]
+9	-9	doc/pmt.xml	[DOC]
+2	-9	doc/spatialgames.xxml => doc/processes.xxml	[DOC]
+1	-0	doc/progress.xxml	[DOC]
+0	-8	doc/sparsemat.xxml	[DOC]
+32	-0	doc/spatial.xxml	[DOC]
+3	-28	doc/structural.xxml	[DOC]
+2	-7	doc/strvector.xxml	[DOC]
+16	-10	doc/tutorial.xml	[DOC]
+7	-12	doc/vector.xxml	[DOC]
+1	-0	doc/vectorlist.xxml	[DOC]
+0	-5	doc/visitors.xxml	[DOC]
+12	-1	etc/cmake/compilers.cmake	[BUILD-CPP14]
+5	-0	etc/cmake/cpack_install_script.cmake	[BUILD-CMAKE]
+12	-4	etc/cmake/dependencies.cmake	[BUILD-DEPS]
+1	-0	etc/cmake/features.cmake	[BUILD-CMAKE]
+5	-5	etc/cmake/packaging.cmake	[BUILD-CMAKE]
+8	-5	etc/cmake/summary.cmake	[BUILD-CMAKE]
+4	-3	examples/simple/adjlist.c	[EXAMPLE]
+7	-5	examples/simple/bellman_ford.c	[EXAMPLE]
+3	-0	examples/simple/blas.c	[EXAMPLE]
+3	-0	examples/simple/blas_dgemm.c	[EXAMPLE]
+5	-3	examples/simple/cattributes.c	[EXAMPLE] ← ATTRS
+4	-2	examples/simple/cattributes2.c	[EXAMPLE] ← ATTRS
+4	-2	examples/simple/cattributes3.c	[EXAMPLE] ← ATTRS
+4	-2	examples/simple/cattributes4.c	[EXAMPLE] ← ATTRS
+6	-5	examples/simple/centralization.c	[EXAMPLE]
+5	-3	examples/simple/cohesive_blocks.c	[EXAMPLE]
+5	-2	examples/simple/coloring.c	[EXAMPLE]
+3	-0	examples/simple/creation.c	[EXAMPLE]
+10	-11	examples/simple/distances.c	[EXAMPLE]
+4	-2	examples/simple/dominator_tree.c	[EXAMPLE]
+4	-3	examples/simple/dot.c	[EXAMPLE]
+4	-2	examples/simple/dqueue.c	[EXAMPLE]
+6	-4	examples/simple/eigenvector_centrality.c	[EXAMPLE] ← CENTRALITY
+5	-5	examples/simple/even_tarjan.c	[EXAMPLE]
+5	-3	examples/simple/flow.c	[EXAMPLE]
+10	-7	examples/simple/flow2.c	[EXAMPLE]
+4	-2	examples/simple/foreign.c	[EXAMPLE]
+4	-2	examples/simple/gml.c	[EXAMPLE]
+4	-1	examples/simple/graphml.c	[EXAMPLE]
+6	-4	examples/simple/igraph_all_st_mincuts.c	[EXAMPLE]
+5	-2	examples/simple/igraph_assortativity_degree.c	[EXAMPLE] ← PROPS
+10	-7	examples/simple/igraph_assortativity_nominal.c	[EXAMPLE]
+4	-3	examples/simple/igraph_atlas.c	[EXAMPLE]
+3	-1	examples/simple/igraph_attribute_combination.c	[EXAMPLE]
+7	-3	examples/simple/igraph_average_path_length.c	[EXAMPLE]
+4	-2	examples/simple/igraph_avg_nearest_neighbor_degree.c	[EXAMPLE] ← SPATIAL
+8	-6	examples/simple/igraph_barabasi_game.c	[EXAMPLE]
+7	-6	examples/simple/igraph_barabasi_game2.c	[EXAMPLE]
+4	-2	examples/simple/igraph_bfs.c	[EXAMPLE]
+9	-7	examples/simple/igraph_bfs_callback.c	[EXAMPLE]
+4	-3	examples/simple/igraph_bfs_simple.c	[EXAMPLE]
+9	-6	examples/simple/igraph_biconnected_components.c	[EXAMPLE]
+9	-10	examples/simple/igraph_bipartite_create.c	[EXAMPLE]
+4	-1	examples/simple/igraph_bipartite_projection.c	[EXAMPLE]
+13	-11	examples/simple/igraph_cliques.c	[EXAMPLE] ← CLIQUES
+4	-2	examples/simple/igraph_cocitation.c	[EXAMPLE]
+10	-5	examples/simple/igraph_community_edge_betweenness.c	[EXAMPLE] ← COMM
+7	-4	examples/simple/igraph_community_edge_betweenness.out	[EXAMPLE] ← COMM
+9	-5	examples/simple/igraph_community_fastgreedy.c	[EXAMPLE]
+8	-7	examples/simple/igraph_community_label_propagation.c	[EXAMPLE] ← COMM
+29	-27	examples/simple/igraph_community_leading_eigenvector.c	[EXAMPLE] ← DS-VECTOR
+68	-24	examples/simple/igraph_community_leiden.c	[EXAMPLE] ← COMM-LEIDEN
+3	-0	examples/simple/igraph_community_leiden.out	[EXAMPLE] ← COMM-LEIDEN
+7	-4	examples/simple/igraph_community_multilevel.c	[EXAMPLE]
+22	-75	examples/simple/igraph_community_optimal_modularity.c	[EXAMPLE] ← COMM
+2	-0	examples/simple/igraph_community_optimal_modularity.out	[EXAMPLE] ← COMM
+4	-2	examples/simple/igraph_complementer.c	[EXAMPLE]
+4	-2	examples/simple/igraph_compose.c	[EXAMPLE]
+5	-2	examples/simple/igraph_contract_vertices.c	[EXAMPLE]
+4	-2	examples/simple/igraph_copy.c	[EXAMPLE]
+4	-2	examples/simple/igraph_create.c	[EXAMPLE]
+10	-10	examples/simple/igraph_decompose.c	[EXAMPLE]
+5	-4	examples/simple/igraph_degree.c	[EXAMPLE] ← PROPS
+30	-10	examples/simple/igraph_degree_sequence_game.c	[EXAMPLE] ← GAMES
+4	-2	examples/simple/igraph_delete_edges.c	[EXAMPLE]
+1	-2	examples/simple/igraph_delete_vertices.c	[EXAMPLE]
+0	-172	examples/simple/igraph_deterministic_optimal_imitation.c	[EXAMPLE]
+34	-23	examples/simple/igraph_diameter.c	[EXAMPLE] ← PROPS
+2	-2	examples/simple/igraph_diameter.out	[EXAMPLE] ← PROPS
+4	-3	examples/simple/igraph_difference.c	[EXAMPLE]
+5	-3	examples/simple/igraph_disjoint_union.c	[EXAMPLE]
+23	-3	examples/simple/igraph_eccentricity.c	[EXAMPLE] ← PROPS
+22	-3	examples/simple/igraph_erdos_renyi_game_gnm.c	[EXAMPLE] ← GAMES-ER
+22	-3	examples/simple/igraph_erdos_renyi_game_gnp.c	[EXAMPLE] ← GAMES-ER
+6	-5	examples/simple/igraph_es_pairs.c	[EXAMPLE]
+4	-3	examples/simple/igraph_feedback_arc_set.c	[EXAMPLE]
+5	-3	examples/simple/igraph_feedback_arc_set_ip.c	[EXAMPLE]
+10	-9	examples/simple/igraph_fisher_yates_shuffle.c	[EXAMPLE]
+6	-4	examples/simple/igraph_full.c	[EXAMPLE]
+6	-7	examples/simple/igraph_get_all_shortest_paths_dijkstra.c	[EXAMPLE] ← PATHS
+20	-23	examples/simple/igraph_get_eid.c	[EXAMPLE]
+34	-44	examples/simple/igraph_get_eids.c	[EXAMPLE]
+15	-11	examples/simple/igraph_get_laplacian.c	[EXAMPLE]
+4	-2	examples/simple/igraph_get_laplacian_sparse.c	[EXAMPLE]
+17	-15	examples/simple/igraph_get_shortest_paths.c	[EXAMPLE] ← PATHS
+6	-5	examples/simple/igraph_get_shortest_paths_dijkstra.c	[EXAMPLE] ← PATHS
+7	-5	examples/simple/igraph_girth.c	[EXAMPLE]
+8	-5	examples/simple/igraph_grg_game.c	[EXAMPLE]
+4	-2	examples/simple/igraph_has_multiple.c	[EXAMPLE]
+18	-10	examples/simple/igraph_independent_sets.c	[EXAMPLE] ← CLIQUES
+5	-0	examples/simple/igraph_independent_sets.out	[EXAMPLE] ← CLIQUES
+6	-4	examples/simple/igraph_intersection.c	[EXAMPLE]
+4	-1	examples/simple/igraph_is_biconnected.c	[EXAMPLE]
+4	-2	examples/simple/igraph_is_directed.c	[EXAMPLE]
+5	-3	examples/simple/igraph_is_loop.c	[EXAMPLE]
+4	-2	examples/simple/igraph_is_minimal_separator.c	[EXAMPLE]
+5	-3	examples/simple/igraph_is_multiple.c	[EXAMPLE]
+4	-2	examples/simple/igraph_is_separator.c	[EXAMPLE]
+9	-6	examples/simple/igraph_isomorphic_vf2.c	[EXAMPLE] ← ISO
+4	-2	examples/simple/igraph_join.c	[EXAMPLE]
+4	-2	examples/simple/igraph_kary_tree.c	[EXAMPLE]
+4	-3	examples/simple/igraph_lapack_dgeev.c	[EXAMPLE]
+4	-3	examples/simple/igraph_lapack_dgeevx.c	[EXAMPLE]
+4	-2	examples/simple/igraph_lapack_dgesv.c	[EXAMPLE]
+4	-3	examples/simple/igraph_lapack_dsyevr.c	[EXAMPLE]
+8	-10	examples/simple/igraph_layout_reingold_tilford.c	[EXAMPLE]
+28	-61	examples/simple/igraph_lcf.c	[EXAMPLE] ← CONSTRUCTORS
+3	-0	examples/simple/igraph_lcf.out	[EXAMPLE] ← CONSTRUCTORS
+7	-3	examples/simple/igraph_list_triangles.c	[EXAMPLE]
+11	-9	examples/simple/igraph_maximal_cliques.c	[EXAMPLE] ← CLIQUES
+3	-5	examples/simple/igraph_maximum_bipartite_matching.c	[EXAMPLE]
+9	-7	examples/simple/igraph_mincut.c	[EXAMPLE]
+5	-3	examples/simple/igraph_minimal_separators.c	[EXAMPLE]
+3	-3	examples/simple/igraph_minimum_size_separators.c	[EXAMPLE] ← CONNECTIVITY
+9	-6	examples/simple/igraph_minimum_spanning_tree.c	[EXAMPLE] ← MISC
+1	-1	examples/simple/igraph_minimum_spanning_tree.out	[EXAMPLE] ← MISC
+8	-5	examples/simple/igraph_motifs_randesu.c	[EXAMPLE] ← MISC
+7	-6	examples/simple/igraph_neighbors.c	[EXAMPLE] ← ITERATORS
+6	-3	examples/simple/igraph_pagerank.c	[EXAMPLE] ← CENTRALITY
+4	-2	examples/simple/igraph_power_law_fit.c	[EXAMPLE]
+7	-5	examples/simple/igraph_radius.c	[EXAMPLE]
+4	-4	examples/simple/igraph_random_sample.c	[EXAMPLE]
+4	-2	examples/simple/igraph_read_graph_dl.c	[EXAMPLE]
+4	-3	examples/simple/igraph_read_graph_graphdb.c	[EXAMPLE]
+4	-2	examples/simple/igraph_read_graph_lgl.c	[EXAMPLE]
+4	-1	examples/simple/igraph_realize_degree_sequence.c	[EXAMPLE] ← PROPS
+4	-2	examples/simple/igraph_reciprocity.c	[EXAMPLE]
+4	-1	examples/simple/igraph_regular_tree.c	[EXAMPLE]
+4	-1	examples/simple/igraph_ring.c	[EXAMPLE]
+0	-213	examples/simple/igraph_roulette_wheel_imitation.c	[EXAMPLE]
+7	-6	examples/simple/igraph_similarity.c	[EXAMPLE] ← MISC
+4	-2	examples/simple/igraph_simplify.c	[EXAMPLE]
+4	-2	examples/simple/igraph_small.c	[EXAMPLE]
+5	-3	examples/simple/igraph_sparsemat.c	[EXAMPLE] ← DS-SPARSEMAT
+27	-29	examples/simple/igraph_sparsemat3.c	[EXAMPLE] ← DS-SPARSEMAT
+23	-21	examples/simple/igraph_sparsemat4.c	[EXAMPLE] ← DS-SPARSEMAT
+7	-5	examples/simple/igraph_sparsemat6.c	[EXAMPLE] ← DS-SPARSEMAT
+4	-2	examples/simple/igraph_sparsemat7.c	[EXAMPLE] ← DS-SPARSEMAT
+4	-3	examples/simple/igraph_sparsemat8.c	[EXAMPLE] ← DS-SPARSEMAT
+4	-1	examples/simple/igraph_star.c	[EXAMPLE]
+0	-182	examples/simple/igraph_stochastic_imitation.c	[EXAMPLE]
+5	-3	examples/simple/igraph_strvector.c	[EXAMPLE] ← DS-STRVECTOR
+9	-7	examples/simple/igraph_subisomorphic_lad.c	[EXAMPLE] ← ISO
+3	-0	examples/simple/igraph_symmetric_tree.c	[EXAMPLE]
+4	-2	examples/simple/igraph_to_undirected.c	[EXAMPLE]
+4	-2	examples/simple/igraph_topological_sorting.c	[EXAMPLE]
+4	-2	examples/simple/igraph_transitivity.c	[EXAMPLE]
+4	-2	examples/simple/igraph_union.c	[EXAMPLE]
+7	-4	examples/simple/igraph_vector_int_list_sort.c	[EXAMPLE] ← DS-VECTOR
+4	-3	examples/simple/igraph_version.c	[EXAMPLE]
+5	-3	examples/simple/igraph_vs_nonadj.c	[EXAMPLE]
+5	-3	examples/simple/igraph_vs_range.c	[EXAMPLE]
+11	-8	examples/simple/igraph_vs_vector.c	[EXAMPLE] ← DS-VECTOR
+37	-22	examples/simple/igraph_weighted_adjacency.c	[EXAMPLE] ← CONSTRUCTORS
+5	-5	examples/simple/igraph_weighted_adjacency.out	[EXAMPLE] ← CONSTRUCTORS
+5	-2	examples/simple/igraph_write_graph_lgl.c	[EXAMPLE]
+5	-4	examples/simple/igraph_write_graph_pajek.c	[EXAMPLE] ← IO
+5	-4	examples/simple/random_seed.c	[EXAMPLE]
+3	-0	examples/simple/safelocale.c	[EXAMPLE]
+6	-4	examples/simple/walktrap.c	[EXAMPLE]
+29	-25	examples/tutorial/tutorial1.c	[EXAMPLE]
+41	-33	examples/tutorial/tutorial2.c	[EXAMPLE]
+49	-44	examples/tutorial/tutorial3.c	[EXAMPLE]
+5	-2	fuzzing/basic_properties_directed.cpp	[FUZZ]
+5	-2	fuzzing/basic_properties_undirected.cpp	[FUZZ]
+4	-4	fuzzing/bliss.cpp	[FUZZ] ← ISO
+4	-4	fuzzing/build.sh	[FUZZ]
+17	-10	fuzzing/centrality.cpp	[FUZZ]
+14	-7	fuzzing/community.cpp	[FUZZ]
+2	-2	fuzzing/edge_connectivity.cpp	[FUZZ]
+13	-13	fuzzing/linear_algos_directed.cpp	[FUZZ]
+53	-14	fuzzing/linear_algos_undirected.cpp	[FUZZ]
+7	-3	fuzzing/misc_algos.cpp	[FUZZ]
+12	-11	fuzzing/misc_algos_weighted.cpp	[FUZZ]
+2	-2	fuzzing/read_dimacs_flow.cpp	[FUZZ]
+1	-1	fuzzing/read_dl.cpp	[FUZZ]
+1	-1	fuzzing/read_edgelist.cpp	[FUZZ]
+1	-1	fuzzing/read_gml.cpp	[FUZZ]
+1	-1	fuzzing/read_graphdb.cpp	[FUZZ]
+1	-1	fuzzing/read_graphml.cpp	[FUZZ]
+1	-1	fuzzing/read_lgl.cpp	[FUZZ]
+1	-1	fuzzing/read_ncol.cpp	[FUZZ]
+1	-1	fuzzing/read_pajek.cpp	[FUZZ] ← IO
+35	-5	fuzzing/spatial.cpp	[FUZZ]
+2	-2	fuzzing/vertex_connectivity.cpp	[FUZZ]
+5	-5	fuzzing/vertex_separators.cpp	[FUZZ]
+20	-11	fuzzing/weighted_centrality.cpp	[FUZZ]
+9	-6	fuzzing/weighted_community.cpp	[FUZZ]
+1	-1	fuzzing/write_all_gml.cpp	[FUZZ]
+1	-1	fuzzing/write_all_graphml.cpp	[FUZZ]
+7	-8	include/igraph.h	[MAIN-HEADER]
+30	-35	include/igraph_adjlist.h	[ADJLIST]
+72	-13	include/igraph_arpack.h	[LINALG]
+0	-63	include/igraph_array.h	[DEP-ARRAY3D]
+0	-54	include/igraph_array_pmt.h	[DEP-ARRAY3D]
+235	-163	include/igraph_attributes.h	[ATTRS]
+52	-52	include/igraph_bipartite.h	[BIPARTITE]
+24	-25	include/igraph_bitset.h	[DS-OTHER]
+5	-8	include/igraph_bitset_list.h	[DS-OTHER]
+5	-10	include/igraph_blas.h	[LINALG]
+99	-96	include/igraph_centrality.h	[CENTRALITY]
+85	-60	include/igraph_cliques.h	[CLIQUES]
+14	-19	include/igraph_cocitation.h	[MISC]
+5	-10	include/igraph_cohesive_blocks.h	[CONNECTIVITY]
+17	-19	include/igraph_coloring.h	[MISC]
+72	-51	include/igraph_community.h	[COMM]
+7	-16	include/igraph_complex.h	[DS-OTHER]
+11	-25	include/igraph_components.h	[CONNECTIVITY]
+5	-9	include/igraph_config.h.in	[TYPES]
+96	-50	include/igraph_constants.h	[TYPES]
+33	-42	include/igraph_constructors.h	[CONSTRUCTORS]
+5	-18	include/igraph_conversion.h	[OTHER-SRC]
+40	-26	include/igraph_cycles.h	[CYCLES]
+7	-12	include/igraph_datatype.h	[TYPES]
+18	-11	include/igraph_decls.h	[DECLS]
+5	-10	include/igraph_dqueue.h	[DS-OTHER]
+6	-12	include/igraph_dqueue_pmt.h	[DS-OTHER]
+28	-31	include/igraph_eigen.h	[LINALG]
+8	-13	include/igraph_embedding.h	[MISC]
+6	-11	include/igraph_epidemics.h	[MISC]
+29	-96	include/igraph_error.h	[ERROR-CODES]
+5	-10	include/igraph_eulerian.h	[OTHER-SRC]
+31	-36	include/igraph_flow.h	[FLOW]
+10	-25	include/igraph_foreign.h	[IO]
+84	-90	include/igraph_games.h	[GAMES]
+6	-11	include/igraph_graph_list.h	[GRAPH]
+24	-8	include/igraph_graphicality.h	[MISC]
+7	-12	include/igraph_graphlets.h	[MISC]
+5	-10	include/igraph_heap.h	[DS-OTHER]
+7	-13	include/igraph_heap_pmt.h	[DS-OTHER]
+13	-19	include/igraph_hrg.h	[MISC]
+57	-41	include/igraph_interface.h	[GRAPH]
+12	-17	include/igraph_interrupt.h	[INTERRUPT]
+34	-69	include/igraph_topology.h => include/igraph_isomorphism.h	[ISO]
+47	-52	include/igraph_iterators.h	[ITERATORS]
+5	-10	include/igraph_lapack.h	[LINALG]
+36	-42	include/igraph_layout.h	[LAYOUT]
+20	-3	include/igraph_lsap.h	[MISC]
+6	-10	include/igraph_matching.h	[MISC]
+5	-13	include/igraph_matrix.h	[DS-MATRIX]
+5	-9	include/igraph_matrix_list.h	[DS-MATRIX]
+40	-52	include/igraph_matrix_pmt.h	[DS-MATRIX]
+5	-16	include/igraph_memory.h	[MEMORY]
+0	-61	include/igraph_microscopic_update.h	[DEP-MICROSCOPIC]
+17	-23	include/igraph_mixing.h	[MISC]
+16	-25	include/igraph_motifs.h	[MISC]
+11	-16	include/igraph_neighborhood.h	[PROPS]
+8	-32	include/igraph_nongraph.h	[MISC]
+37	-29	include/igraph_operators.h	[OPERATORS]
+113	-176	include/igraph_paths.h	[PATHS]
+11	-10	include/igraph_pmt.h	[DS-PMT]
+3	-8	include/igraph_pmt_off.h	[DS-PMT]
+35	-22	include/igraph_progress.h	[PROGRESS]
+12	-17	include/igraph_psumtree.h	[DS-OTHER]
+5	-10	include/igraph_qsort.h	[DS-OTHER]
+14	-40	include/igraph_random.h	[RNG]
+5	-5	include/igraph_reachability.h	[CONNECTIVITY]
+45	-0	include/igraph_sampling.h	[SAMPLING]
+7	-12	include/igraph_scan.h	[MISC]
+7	-13	include/igraph_separators.h	[CONNECTIVITY]
+14	-12	examples/simple/igraph_adjacency.c => include/igraph_setup.h	[SETUP]
+33	-58	include/igraph_sparsemat.h	[DS-SPARSEMAT]
+91	-0	include/igraph_spatial.h	[SPATIAL]
+5	-10	include/igraph_stack.h	[DS-OTHER]
+7	-12	include/igraph_stack_pmt.h	[DS-OTHER]
+14	-24	include/igraph_statusbar.h	[STATUS]
+30	-52	include/igraph_structural.h	[PROPS]
+28	-35	include/igraph_strvector.h	[DS-STRVECTOR]
+5	-10	include/igraph_threading.h.in	[DS-OTHER]
+9	-14	include/igraph_transitivity.h	[PROPS]
+21	-24	include/igraph_typed_list_pmt.h	[DS-PMT]
+11	-25	include/igraph_types.h	[TYPES]
+18	-25	include/igraph_vector.h	[DS-VECTOR]
+5	-9	include/igraph_vector_list.h	[DS-VECTOR]
+41	-57	include/igraph_vector_pmt.h	[DS-VECTOR]
+17	-24	include/igraph_vector_ptr.h	[DS-VECTOR]
+3	-8	include/igraph_vector_type.h	[DS-VECTOR]
+6	-11	include/igraph_version.h.in	[VERSION]
+15	-20	include/igraph_visitor.h	[ITERATORS]
+473	-445	interfaces/functions.yaml	[INTERFACES]
+44	-45	interfaces/types.yaml	[INTERFACES]
+24	-14	src/CMakeLists.txt	[BUILD-CMAKE]
+289	-186	src/centrality/betweenness.c	[CENTRALITY]
+4	-4	src/centrality/centrality_internal.h	[CENTRALITY]
+26	-6	src/centrality/centrality_other.c	[CENTRALITY]
+56	-94	src/centrality/centralization.c	[CENTRALITY]
+42	-44	src/centrality/closeness.c	[CENTRALITY]
+25	-24	src/centrality/coreness.c	[CENTRALITY]
+169	-103	src/centrality/eigenvector.c	[CENTRALITY]
+149	-167	src/centrality/hub_authority.c	[CENTRALITY]
+81	-79	src/centrality/pagerank.c	[CENTRALITY]
+3	-4	src/centrality/prpack.cpp	[CENTRALITY]
+4	-4	src/centrality/prpack/prpack_igraph_graph.cpp	[CENTRALITY]
+3	-4	src/centrality/prpack_internal.h	[CENTRALITY]
+17	-17	src/centrality/truss.cpp	[CENTRALITY]
+9	-7	src/cliques/cliquer_internal.h	[CLIQUES]
+36	-23	src/cliques/cliquer_wrapper.c	[CLIQUES]
+150	-87	src/cliques/cliques.c	[CLIQUES]
+74	-93	src/cliques/glet.c	[CLIQUES]
+175	-104	src/cliques/maximal_cliques.c	[CLIQUES]
+51	-40	src/cliques/maximal_cliques_template.h	[CLIQUES]
+4	-4	src/community/community_internal.h	[COMM]
+50	-53	src/community/community_misc.c	[COMM]
+149	-113	src/community/edge_betweenness.c	[COMM]
+41	-55	src/community/fast_modularity.c	[COMM]
+26	-38	src/community/fluid.c	[COMM]
+275	-0	src/community/infomap.cpp	[COMM-INFOMAP]
+0	-323	src/community/infomap/infomap.cc	[COMM-INFOMAP]
+0	-382	src/community/infomap/infomap_FlowGraph.cc	[COMM-INFOMAP]
+0	-81	src/community/infomap/infomap_FlowGraph.h	[COMM-INFOMAP]
+0	-522	src/community/infomap/infomap_Greedy.cc	[COMM-INFOMAP]
+0	-74	src/community/infomap/infomap_Greedy.h	[COMM-INFOMAP]
+0	-52	src/community/infomap/infomap_Node.h	[COMM-INFOMAP]
+512	-206	src/community/label_propagation.c	[COMM]
+79	-76	src/community/leading_eigenvector.c	[COMM]
+815	-368	src/community/leiden.c	[COMM-LEIDEN]
+49	-53	src/community/louvain.c	[COMM]
+18	-20	src/community/modularity.c	[COMM]
+23	-14	src/community/optimal_modularity.c	[COMM]
+4	-5	src/community/spinglass/NetDataTypes.cpp	[COMM]
+44	-45	src/community/spinglass/NetDataTypes.h	[COMM]
+7	-8	src/community/spinglass/NetRoutines.cpp	[COMM]
+1	-2	src/community/spinglass/NetRoutines.h	[COMM]
+25	-40	src/community/spinglass/clustertool.cpp	[COMM]
+88	-89	src/community/spinglass/pottsmodel_2.cpp	[COMM]
+20	-21	src/community/spinglass/pottsmodel_2.h	[COMM]
+26	-37	src/community/voronoi.c	[COMM]
+6	-7	src/community/walktrap/walktrap.cpp	[COMM]
+1	-2	src/community/walktrap/walktrap_communities.cpp	[COMM]
+2	-3	src/community/walktrap/walktrap_communities.h	[COMM]
+4	-5	src/community/walktrap/walktrap_graph.cpp	[COMM]
+1	-2	src/community/walktrap/walktrap_graph.h	[COMM]
+1	-2	src/community/walktrap/walktrap_heap.cpp	[COMM]
+1	-2	src/community/walktrap/walktrap_heap.h	[COMM]
+1	-0	src/config.h.in	[BUILD-CMAKE]
+38	-37	src/connectivity/cohesive_blocks.c	[CONNECTIVITY]
+111	-148	src/connectivity/components.c	[CONNECTIVITY]
+32	-32	src/connectivity/percolation.c	[CONNECTIVITY]
+21	-27	src/connectivity/reachability.c	[CONNECTIVITY]
+77	-75	src/connectivity/separators.c	[CONNECTIVITY]
+315	-216	src/constructors/adjacency.c	[CONSTRUCTORS]
+5	-6	src/constructors/atlas-edges.h	[CONSTRUCTORS]
+8	-8	src/constructors/atlas.c	[CONSTRUCTORS]
+8	-21	src/constructors/basic_constructors.c	[CONSTRUCTORS]
+7	-7	src/constructors/circulant.c	[CONSTRUCTORS]
+8	-9	src/constructors/de_bruijn.c	[CONSTRUCTORS]
+37	-38	src/constructors/famous.c	[CONSTRUCTORS]
+37	-38	src/constructors/full.c	[CONSTRUCTORS]
+10	-10	src/constructors/generalized_petersen.c	[CONSTRUCTORS]
+15	-16	src/constructors/kautz.c	[CONSTRUCTORS]
+46	-50	src/constructors/lattices.c	[CONSTRUCTORS]
+37	-37	src/constructors/lcf.c	[CONSTRUCTORS]
+19	-20	src/constructors/linegraph.c	[CONSTRUCTORS]
+18	-18	src/constructors/mycielskian.c	[CONSTRUCTORS]
+7	-8	src/constructors/prufer.c	[CONSTRUCTORS]
+52	-91	src/constructors/regular.c	[CONSTRUCTORS]
+6	-8	src/constructors/trees.c	[CONSTRUCTORS]
+0	-110	src/core/array.pmt	[DEP-ARRAY3D]
+57	-105	src/core/bitset.c	[DS-OTHER]
+1	-1	src/core/bitset_list.c	[DS-OTHER]
+23	-24	src/core/buckets.c	[DS-OTHER]
+19	-20	src/core/buckets.h	[DS-OTHER]
+17	-18	src/core/cutheap.c	[DS-OTHER]
+10	-11	src/core/cutheap.h	[DS-OTHER]
+1	-2	src/core/dqueue.c	[DS-OTHER]
+6	-19	src/core/dqueue.pmt	[DS-OTHER]
+58	-49	src/core/error.c	[ERROR-CODES]
+8	-9	src/core/estack.c	[DS-OTHER]
+8	-9	src/core/estack.h	[DS-OTHER]
+3	-4	src/core/fixed_vectorlist.c	[DS-OTHER]
+5	-6	src/core/fixed_vectorlist.h	[DS-OTHER]
+22	-22	src/core/genheap.c	[DS-OTHER]
+11	-11	src/core/genheap.h	[DS-OTHER]
+19	-19	src/core/grid.c	[DS-OTHER]
+15	-16	src/core/grid.h	[DS-OTHER]
+1	-2	src/core/heap.c	[DS-OTHER]
+18	-23	src/core/heap.pmt	[DS-OTHER]
+130	-143	src/core/indheap.c	[DS-OTHER]
+31	-34	src/core/indheap.h	[DS-OTHER]
+5	-6	src/core/interruption.c	[INTERRUPT]
+8	-10	src/core/interruption.h	[INTERRUPT]
+9	-10	src/core/marked_queue.c	[DS-OTHER]
+9	-10	src/core/marked_queue.h	[DS-OTHER]
+1	-1	src/core/math.h	[OTHER-SRC]
+17	-31	src/core/matrix.c	[DS-MATRIX]
+170	-212	src/core/matrix.pmt	[DS-MATRIX]
+1	-2	src/core/matrix_list.c	[DS-MATRIX]
+1	-1	src/core/memory.c	[MEMORY]
+1	-2	src/core/printing.c	[DS-OTHER]
+8	-13	src/core/progress.c	[PROGRESS]
+9	-10	src/core/psumtree.c	[DS-OTHER]
+18	-18	src/core/set.c	[DS-OTHER]
+13	-13	src/core/set.h	[DS-OTHER]
+67	-0	src/core/setup.c	[SETUP]
+109	-422	src/core/sparsemat.c	[DS-SPARSEMAT]
+1	-2	src/core/stack.c	[DS-OTHER]
+10	-11	src/core/stack.pmt	[DS-OTHER]
+11	-14	src/core/statusbar.c	[STATUS]
+126	-105	src/core/strvector.c	[DS-STRVECTOR]
+13	-14	src/core/trie.c	[DS-OTHER]
+10	-11	src/core/trie.h	[DS-OTHER]
+69	-39	src/core/typed_list.pmt	[OTHER-SRC]
+75	-132	src/core/vector.c	[DS-VECTOR]
+289	-291	src/core/vector.pmt	[DS-VECTOR]
+1	-2	src/core/vector_list.c	[DS-VECTOR]
+96	-59	src/core/vector_ptr.c	[DS-VECTOR]
+53	-55	src/misc/cycle_bases.c => src/cycles/cycle_bases.c	[CYCLES]
+83	-86	src/misc/feedback_arc_set.c => src/cycles/feedback_sets.c	[CYCLES]
+6	-6	src/misc/feedback_arc_set.h => src/cycles/feedback_sets.h	[CYCLES]
+16	-16	src/misc/order_cycle.cpp => src/cycles/order_cycle.cpp	[CYCLES]
+3	-3	src/misc/order_cycle.h => src/cycles/order_cycle.h	[CYCLES]
+51	-34	src/cycles/simple_cycles.c	[CYCLES]
+1	-1	src/f2c.h	[INTERNAL]
+197	-202	src/flow/flow.c	[FLOW]
+5	-6	src/flow/flow_conversion.c	[FLOW]
+5	-6	src/flow/flow_internal.h	[FLOW]
+154	-154	src/flow/st-cuts.c	[FLOW]
+70	-88	src/games/barabasi.c	[GAMES]
+9	-15	src/games/callaway_traits.c	[GAMES]
+6	-8	src/games/chung_lu.c	[GAMES]
+31	-45	src/games/citations.c	[GAMES]
+65	-50	src/games/correlated.c	[GAMES]
+72	-107	src/games/degree_sequence.c	[GAMES]
+3	-3	src/games/degree_sequence_vl/degree_sequence_vl.h	[GAMES]
+5	-5	src/games/degree_sequence_vl/gengraph_definitions.h	[GAMES]
+17	-17	src/games/degree_sequence_vl/gengraph_degree_sequence.cpp	[GAMES]
+12	-12	src/games/degree_sequence_vl/gengraph_degree_sequence.h	[GAMES]
+101	-101	src/games/degree_sequence_vl/gengraph_graph_molloy_hash.cpp	[GAMES]
+33	-33	src/games/degree_sequence_vl/gengraph_graph_molloy_hash.h	[GAMES]
+137	-137	src/games/degree_sequence_vl/gengraph_graph_molloy_optimized.cpp	[GAMES]
+40	-40	src/games/degree_sequence_vl/gengraph_graph_molloy_optimized.h	[GAMES]
+27	-27	src/games/degree_sequence_vl/gengraph_hash.h	[GAMES]
+1	-7	src/games/degree_sequence_vl/gengraph_mr-connected.cpp	[GAMES]
+49	-49	src/games/degree_sequence_vl/gengraph_qsort.h	[GAMES]
+10	-198	src/games/dotproduct.c	[GAMES]
+644	-244	src/games/erdos_renyi.c	[GAMES-ER]
+7	-13	src/games/establishment.c	[GAMES]
+21	-26	src/games/forestfire.c	[GAMES]
+5	-11	src/games/grg.c	[GAMES]
+12	-18	src/games/growing_random.c	[GAMES]
+10	-16	src/games/islands.c	[GAMES]
+2	-4	src/games/k_regular.c	[GAMES]
+33	-43	src/games/preference.c	[GAMES]
+40	-48	src/games/recent_degree.c	[GAMES]
+128	-123	src/games/sbm.c	[GAMES]
+26	-26	src/games/static_fitness.c	[GAMES]
+9	-17	src/games/tree.c	[GAMES]
+9	-10	src/games/watts_strogatz.c	[GAMES]
+123	-186	src/graph/adjlist.c	[ADJLIST]
+618	-27	src/graph/attributes.c	[ATTRS]
+19	-23	src/graph/attributes.h	[ATTRS]
+4	-34	src/graph/basic_query.c	[GRAPH]
+1	-1	src/graph/caching.c	[GRAPH]
+3	-3	src/graph/caching.h	[GRAPH]
+879	-2494	src/graph/cattributes.c	[ATTRS]
+2	-3	src/graph/graph_list.c	[GRAPH]
+3	-13	src/graph/internal.h	[GRAPH]
+124	-170	src/graph/iterators.c	[ITERATORS]
+58	-22	src/graph/type_common.c	[GRAPH]
+339	-250	src/graph/type_indexededgelist.c	[GRAPH]
+38	-37	src/graph/visitors.c	[ITERATORS]
+1	-1	src/hrg/dendro.h	[HRG]
+2	-2	src/hrg/graph.h	[HRG]
+1	-1	src/hrg/graph_simp.h	[HRG]
+69	-88	src/hrg/hrg.cc	[HRG]
+2	-2	src/hrg/hrg_types.cc	[HRG]
+1	-1	src/hrg/rbtree.h	[HRG]
+1	-1	src/hrg/splittree_eq.h	[HRG]
+12	-15	src/internal/glpk_support.c	[INTERNAL]
+7	-9	src/internal/glpk_support.h	[INTERNAL]
+1	-3	src/internal/gmp_internal.h	[INTERNAL]
+1	-2	src/internal/hacks.c	[INTERNAL]
+3	-4	src/internal/hacks.h	[INTERNAL]
+56	-56	src/internal/lsap.c	[INTERNAL]
+136	-7	src/internal/utils.c	[INTERNAL]
+8	-1	src/internal/utils.h	[INTERNAL]
+0	-201	src/internal/zeroin.c	[DEP-ZEROIN]
+14	-45	src/io/dimacs.c	[IO]
+3	-3	src/io/dl-header.h	[IO]
+2	-2	src/io/dl-lexer.l	[IO]
+17	-17	src/io/dl-parser.y	[IO]
+24	-20	src/io/dl.c	[IO]
+15	-16	src/io/dot.c	[IO]
+4	-5	src/io/edgelist.c	[IO]
+1	-1	src/io/gml-header.h	[IO]
+2	-2	src/io/gml-lexer.l	[IO]
+3	-3	src/io/gml-parser.y	[IO]
+26	-26	src/io/gml-tree.c	[IO]
+22	-22	src/io/gml-tree.h	[IO]
+120	-150	src/io/gml.c	[IO]
+6	-7	src/io/graphdb.c	[IO]
+160	-299	src/io/graphml.c	[IO]
+10	-11	src/io/leda.c	[IO]
+2	-2	src/io/lgl-header.h	[IO]
+2	-2	src/io/lgl-lexer.l	[IO]
+5	-5	src/io/lgl-parser.y	[IO]
+42	-37	src/io/lgl.c	[IO]
+1	-1	src/io/ncol-header.h	[IO]
+2	-2	src/io/ncol-lexer.l	[IO]
+5	-5	src/io/ncol-parser.y	[IO]
+39	-35	src/io/ncol.c	[IO]
+10	-10	src/io/pajek-header.h	[IO]
+2	-2	src/io/pajek-lexer.l	[IO]
+187	-107	src/io/pajek-parser.y	[IO]
+49	-100	src/io/pajek.c	[IO]
+5	-9	src/io/parse_utils.c	[IO]
+2	-2	src/io/parse_utils.h	[IO]
+166	-31	src/isomorphism/bliss.cc	[ISO]
+36	-33	src/isomorphism/isoclasses.c	[ISO]
+3	-4	src/isomorphism/isoclasses.h	[ISO]
+9	-10	src/isomorphism/isomorphism_misc.c	[ISO]
+119	-129	src/isomorphism/lad.c	[ISO]
+5	-33	src/isomorphism/queries.c	[ISO]
+67	-108	src/isomorphism/vf2.c	[ISO]
+21	-23	src/layout/align.c	[LAYOUT]
+11	-13	src/layout/circular.c	[LAYOUT]
+42	-44	src/layout/davidson_harel.c	[LAYOUT]
+2	-2	src/layout/drl/drl_Node.h	[LAYOUT]
+2	-2	src/layout/drl/drl_Node_3d.h	[LAYOUT]
+23	-23	src/layout/drl/drl_graph.cpp	[LAYOUT]
+13	-13	src/layout/drl/drl_graph.h	[LAYOUT]
+19	-19	src/layout/drl/drl_graph_3d.cpp	[LAYOUT]
+13	-13	src/layout/drl/drl_graph_3d.h	[LAYOUT]
+1	-5	src/layout/drl/drl_layout.cpp	[LAYOUT]
+1	-5	src/layout/drl/drl_layout_3d.cpp	[LAYOUT]
+37	-43	src/layout/fruchterman_reingold.c	[LAYOUT]
+11	-16	src/layout/gem.c	[LAYOUT]
+24	-26	src/layout/graphopt.c	[LAYOUT]
+31	-31	src/layout/kamada_kawai.c	[LAYOUT]
+24	-30	src/layout/large_graph.c	[LAYOUT]
+5	-8	src/layout/layout_bipartite.c	[LAYOUT]
+5	-7	src/layout/layout_grid.c	[LAYOUT]
+4	-5	src/layout/layout_internal.h	[LAYOUT]
+11	-25	src/layout/layout_random.c	[LAYOUT]
+13	-20	src/layout/mds.c	[LAYOUT]
+34	-25	src/layout/merge_dla.c	[LAYOUT]
+15	-15	src/layout/merge_grid.c	[LAYOUT]
+10	-10	src/layout/merge_grid.h	[LAYOUT]
+64	-66	src/layout/reingold_tilford.c	[LAYOUT]
+164	-180	src/layout/sugiyama.c	[LAYOUT]
+73	-77	src/layout/umap.c	[LAYOUT]
+185	-107	src/linalg/arpack.c	[LINALG]
+3	-4	src/linalg/arpack_internal.h	[LINALG]
+5	-7	src/linalg/blas.c	[LINALG]
+3	-5	src/linalg/blas_internal.h	[LINALG]
+25	-27	src/linalg/eigen.c	[LINALG]
+41	-42	src/linalg/lapack.c	[LINALG]
+3	-5	src/linalg/lapack_internal.h	[LINALG]
+1	-16	src/math/complex.c	[DS-OTHER]
+26	-26	src/math/safe_intop.c	[INTERNAL]
+22	-22	src/math/safe_intop.h	[INTERNAL]
+1	-22	src/math/utils.c	[INTERNAL]
+737	-383	src/misc/bipartite.c	[BIPARTITE]
+17	-18	src/misc/chordality.c	[MISC]
+66	-62	src/misc/cocitation.c	[MISC]
+44	-51	src/misc/coloring.c	[MISC]
+87	-171	src/misc/conversion.c	[MISC]
+89	-92	src/misc/degree_sequence.cpp	[MISC]
+56	-62	src/misc/embedding.c	[MISC]
+81	-63	src/misc/graphicality.c	[MISC]
+36	-0	src/misc/graphicality.h	[MISC]
+36	-47	src/misc/matching.c	[MISC]
+0	-1209	src/misc/microscopic_update.c	[DEP-MICROSCOPIC]
+151	-101	src/misc/mixing.c	[MISC]
+142	-129	src/misc/motifs.c	[MISC]
+16	-223	src/misc/other.c	[MISC]
+2	-11	src/misc/power_law_fit.c	[MISC]
+64	-105	src/misc/scan.c	[MISC]
+16	-27	src/misc/sir.c	[MISC]
+331	-203	src/misc/spanning_trees.c	[MISC]
+2	-4	src/operators/add_edge.c	[OPERATORS]
+6	-8	src/operators/complementer.c	[OPERATORS]
+12	-13	src/operators/compose.c	[OPERATORS]
+36	-40	src/operators/connect_neighborhood.c	[OPERATORS]
+15	-17	src/operators/contract.c	[OPERATORS]
+10	-12	src/operators/difference.c	[OPERATORS]
+18	-19	src/operators/disjoint_union.c	[OPERATORS]
+16	-17	src/operators/intersection.c	[OPERATORS]
+6	-9	src/operators/join.c	[OPERATORS]
+16	-17	src/operators/misc_internal.c	[OPERATORS]
+3	-4	src/operators/misc_internal.h	[OPERATORS]
+18	-22	src/operators/permute.c	[OPERATORS]
+86	-86	src/operators/products.c	[OPERATORS]
+6	-7	src/operators/reverse.c	[OPERATORS]
+113	-110	src/operators/rewire.c	[OPERATORS]
+46	-56	src/operators/rewire_edges.c	[OPERATORS]
+7	-5	src/operators/rewire_internal.h	[OPERATORS]
+7	-9	src/operators/simplify.c	[OPERATORS]
+47	-63	src/operators/subgraph.c	[OPERATORS]
+3	-5	src/operators/subgraph.h	[OPERATORS]
+14	-15	src/operators/union.c	[OPERATORS]
+46	-28	src/paths/all_shortest_paths.c	[PATHS]
+14	-16	src/paths/astar.c	[PATHS]
+86	-95	src/paths/bellman_ford.c	[PATHS]
+152	-136	src/paths/dijkstra.c	[PATHS]
+176	-363	src/paths/distances.c	[PATHS]
+31	-33	src/paths/eulerian.c	[PATHS]
+40	-38	src/paths/floyd_warshall.c	[PATHS]
+11	-11	src/paths/histogram.c	[PATHS]
+94	-82	src/paths/johnson.c	[PATHS]
+119	-0	src/paths/paths_internal.h	[PATHS]
+15	-71	src/paths/random_walk.c	[PATHS]
+239	-264	src/paths/shortest_paths.c	[PATHS]
+79	-57	src/paths/simple_paths.c	[PATHS]
+67	-74	src/paths/sparsifier.c	[PATHS]
+154	-70	src/paths/unweighted.c	[PATHS]
+22	-28	src/paths/voronoi.c	[PATHS]
+34	-36	src/paths/widest_paths.c	[PATHS]
+58	-36	src/properties/basic_properties.c	[PROPS]
+17	-22	src/properties/complete.c	[PROPS]
+12	-20	src/properties/constraint.c	[PROPS]
+9	-11	src/properties/convergence_degree.c	[PROPS]
+26	-127	src/properties/dag.c	[PROPS]
+77	-88	src/properties/degrees.c	[PROPS]
+28	-30	src/properties/ecc.c	[PROPS]
+37	-38	src/properties/girth.c	[PROPS]
+8	-12	src/properties/loops.c	[PROPS]
+68	-46	src/properties/multiplicity.c	[PROPS]
+47	-49	src/properties/neighborhood.c	[PROPS]
+12	-13	src/properties/perfect.c	[PROPS]
+3	-4	src/properties/properties_internal.h	[PROPS]
+13	-13	src/properties/rich_club.c	[PROPS]
+13	-71	src/properties/spectral.c	[PROPS]
+49	-44	src/properties/trees.c	[PROPS]
+71	-95	src/properties/triangles.c	[PROPS]
+11	-13	src/properties/triangles_template.h	[PROPS]
+10	-12	src/properties/triangles_template1.h	[PROPS]
+60	-98	src/random/random.c	[RNG]
+43	-0	src/random/random_device.cpp	[RNG]
+17	-20	src/random/random_internal.h	[RNG]
+1	-1	src/random/rng_glibc2.c	[RNG]
+1	-1	src/random/rng_mt19937.c	[RNG]
+3	-5	src/random/rng_pcg32.c	[RNG]
+1	-1	src/random/rng_pcg64.c	[RNG]
+192	-0	src/random/sampling.c	[RNG]
+816	-0	src/spatial/beta_skeleton.cpp	[SPATIAL]
+188	-0	src/spatial/convex_hull.c	[SPATIAL]
+280	-0	src/spatial/delaunay.c	[SPATIAL]
+119	-0	src/spatial/edge_lengths.c	[SPATIAL]
+121	-0	src/spatial/nanoflann_internal.hpp	[SPATIAL]
+189	-0	src/spatial/nearest_neighbor.cpp	[SPATIAL]
+34	-0	src/spatial/spatial_internal.h	[SPATIAL]
+15	-13	src/version.c	[VERSION]
+30	-8	tests/CMakeLists.txt	[TEST]
+2	-2	tests/benchmarks/bench.h	[TEST]
+150	-0	tests/benchmarks/beta_skeletons.c	[TEST] ← SPATIAL
+2	-2	tests/benchmarks/coloring.c	[TEST]
+12	-12	tests/benchmarks/community.c	[TEST]
+3	-3	tests/benchmarks/connectivity.c	[TEST]
+24	-24	tests/benchmarks/erdos_renyi.c	[TEST] ← GAMES-ER
+3	-3	tests/benchmarks/graphicality.c	[TEST]
+100	-0	tests/benchmarks/igraph_adjacency.c	[TEST] ← CONSTRUCTORS
+13	-13	tests/benchmarks/igraph_average_path_length_unweighted.c	[TEST]
+11	-11	tests/benchmarks/igraph_betweenness.c	[TEST] ← CENTRALITY
+21	-21	tests/benchmarks/igraph_betweenness_weighted.c	[TEST] ← CENTRALITY
+6	-6	tests/benchmarks/igraph_cliques.c	[TEST] ← CLIQUES
+5	-5	tests/benchmarks/igraph_closeness_weighted.c	[TEST]
+1	-1	tests/benchmarks/igraph_decompose.c	[TEST]
+31	-12	tests/benchmarks/igraph_degree.c	[TEST] ← PROPS
+10	-10	tests/benchmarks/igraph_degree_sequence_game.c	[TEST] ← GAMES
+64	-0	tests/benchmarks/igraph_delaunay_graph.c	[TEST] ← SPATIAL
+101	-161	tests/benchmarks/igraph_distances.c	[TEST]
+5	-5	tests/benchmarks/igraph_ecc.c	[TEST]
+8	-8	tests/benchmarks/igraph_induced_subgraph.c	[TEST]
+2	-2	tests/benchmarks/igraph_induced_subgraph_edges.c	[TEST]
+3	-5	tests/benchmarks/igraph_layout_umap.c	[TEST]
+3	-5	tests/benchmarks/igraph_matrix_transpose.c	[TEST] ← DS-MATRIX
+7	-6	tests/benchmarks/igraph_maximal_cliques.c	[TEST] ← CLIQUES
+77	-0	tests/benchmarks/igraph_nearest_neighbor_graph.c	[TEST] ← SPATIAL
+52	-55	tests/benchmarks/igraph_neighborhood.c	[TEST]
+42	-24	tests/benchmarks/igraph_pagerank.c	[TEST] ← CENTRALITY
+43	-25	tests/benchmarks/igraph_pagerank_weighted.c	[TEST] ← CENTRALITY
+5	-9	tests/benchmarks/igraph_power_law_fit.c	[TEST]
+4	-8	tests/benchmarks/igraph_qsort.c	[DS-OTHER]
+2	-2	tests/benchmarks/igraph_random_walk.c	[TEST]
+6	-6	tests/benchmarks/igraph_realize_degree_sequence.c	[TEST] ← PROPS
+77	-0	tests/benchmarks/igraph_rewire.c	[TEST] ← OPERATORS
+2	-2	tests/benchmarks/igraph_strength.c	[TEST]
+5	-5	tests/benchmarks/igraph_transitivity.c	[TEST]
+2	-2	tests/benchmarks/igraph_tree_game.c	[TEST]
+2	-2	tests/benchmarks/igraph_vertex_connectivity.c	[TEST]
+9	-17	tests/benchmarks/igraph_voronoi.c	[TEST]
+75	-75	tests/benchmarks/inc_vs_adj.c	[TEST]
+5	-5	tests/benchmarks/intersection.c	[TEST]
+6	-6	tests/benchmarks/lad.c	[TEST]
+3	-3	tests/benchmarks/modularity.c	[TEST]
+164	-0	tests/benchmarks/spanning_tree.c	[TEST] ← MISC
+1	-2	tests/regression/bug-1033045.c	[TEST]
+1	-2	tests/regression/bug-1149658.c	[TEST]
+6	-6	tests/regression/bug_1760.c	[TEST]
+1	-1	tests/regression/bug_1814.c	[TEST]
+1	-1	tests/regression/bug_1970.c	[TEST]
+2	-3	tests/regression/bug_2150.c	[TEST]
+1	-1	tests/regression/bug_2497.c	[TEST]
+1	-1	tests/regression/bug_2506.c	[TEST]
+1	-1	tests/regression/bug_2517.c	[TEST]
+29	-30	src/core/array.c => tests/regression/bug_2608.c	[DEP-ARRAY3D]
+0	-0	tests/regression/bug_2608.out	[TEST]
+1	-1	tests/regression/cattr_bool_bug.c	[TEST]
+1	-1	tests/regression/cattr_bool_bug2.c	[TEST]
+2	-2	tests/regression/igraph_layout_kamada_kawai_3d_bug_1462.c	[TEST]
+2	-3	tests/regression/igraph_layout_reingold_tilford_bug_879.c	[TEST]
+1	-1	tests/regression/igraph_read_graph_gml_invalid_inputs.c	[TEST]
+1	-1	tests/regression/igraph_read_graph_graphml_invalid_inputs.c	[TEST]
+1	-1	tests/regression/igraph_read_graph_pajek_invalid_inputs.c	[TEST] ← IO
+4	-9	tests/unit/2wheap.c	[TEST]
+7	-8	tests/unit/VF2-compat.c	[TEST]
+42	-46	tests/unit/adj.c	[TEST]
+6	-6	tests/unit/adj.out	[TEST]
+6	-6	tests/unit/adjlist.c	[TEST]
+10	-10	tests/unit/all_almost_e.c	[TEST]
+10	-10	tests/unit/all_shortest_paths.c	[TEST] ← PATHS
+26	-31	tests/unit/assortativity.c	[TEST]
+182	-0	tests/unit/beta_skeletons.c	[TEST] ← SPATIAL
+338	-0	tests/unit/beta_skeletons.out	[TEST] ← SPATIAL
+7	-8	tests/unit/bfs.c	[TEST]
+1	-2	tests/unit/bfs_simple.c	[TEST]
+3	-5	tests/unit/bitset.c	[TEST]
+2	-2	tests/unit/bliss_automorphisms.c	[TEST] ← ISO
+1	-2	tests/unit/cattributes5.c	[TEST] ← ATTRS
+22	-23	tests/unit/cattributes6.c	[TEST] ← ATTRS
+99	-99	tests/unit/cattributes6.out	[TEST] ← ATTRS
+2	-3	tests/unit/centralization.c	[TEST]
+1	-1	tests/unit/cmp_epsilon.c	[TEST]
+12	-11	tests/unit/coloring.c	[TEST]
+14	-6	tests/unit/community_indexing.c	[TEST]
+66	-25	tests/unit/community_label_propagation.c	[TEST] ← COMM
+5	-5	tests/unit/community_label_propagation2.c	[TEST] ← COMM
+1	-1	tests/unit/community_label_propagation2.out	[TEST] ← COMM
+3	-5	tests/unit/community_label_propagation3.c	[TEST] ← COMM
+129	-16	tests/unit/community_leiden.c	[TEST] ← COMM-LEIDEN
+31	-16	tests/unit/community_leiden.out	[TEST] ← COMM-LEIDEN
+1	-1	tests/unit/community_walktrap.c	[TEST]
+2	-2	tests/unit/components.c	[TEST]
+37	-45	tests/unit/constructor-failure.c	[TEST]
+5	-13	tests/unit/coreness.c	[TEST]
+3	-4	tests/unit/cutheap.c	[TEST]
+20	-20	tests/unit/cycle_bases.c	[TEST]
+4	-5	tests/unit/d_indheap.c	[TEST]
+4	-4	tests/unit/dgemv.c	[TEST]
+11	-11	tests/unit/edge_selectors.c	[TEST]
+22	-23	tests/unit/efficiency.c	[TEST]
+106	-0	tests/unit/eigen_stress.c	[TEST] ← LINALG
+233	-21	tests/unit/erdos_renyi_game_gnm.c	[TEST] ← GAMES-ER
+173	-86	tests/unit/erdos_renyi_game_gnp.c	[TEST] ← GAMES-ER
+1	-1	tests/unit/error_macros.c	[TEST]
+1	-1	tests/unit/expand_path_to_pairs.c	[TEST]
+1	-1	tests/unit/fatal_handler.c	[TEST]
+1	-1	tests/unit/foreign_empty.c	[TEST]
+2	-3	tests/unit/full.c	[TEST]
+4	-4	tests/unit/gen2wheap.c	[TEST]
+1	-1	tests/unit/global_transitivity.c	[TEST]
+5	-6	tests/unit/glpk_error.c	[TEST]
+1	-1	tests/unit/gml.c	[TEST]
+5	-6	tests/unit/graphlets.c	[TEST]
+1	-1	tests/unit/harmonic_centrality.c	[TEST]
+3	-3	tests/unit/heap.c	[TEST]
+13	-13	tests/unit/hub_and_authority.c	[TEST] ← CENTRALITY
+5	-5	tests/unit/hub_and_authority.out	[TEST] ← CENTRALITY
+2	-3	tests/unit/igraph_add_edges.c	[TEST]
+1	-2	tests/unit/igraph_add_vertices.c	[TEST]
+2	-2	tests/unit/igraph_adhesion.c	[TEST]
+8	-8	tests/unit/igraph_adjacency.c	[TEST] ← CONSTRUCTORS
+19	-4	tests/unit/igraph_adjacency.out	[TEST] ← CONSTRUCTORS
+1	-2	tests/unit/igraph_adjacency_spectral_embedding.c	[TEST] ← CONSTRUCTORS
+37	-7	tests/unit/igraph_adjlist_init_complementer.c	[TEST]
+45	-3	tests/unit/igraph_adjlist_init_complementer.out	[TEST]
+1	-1	tests/unit/igraph_adjlist_simplify.c	[TEST]
+6	-7	tests/unit/igraph_all_st_cuts.c	[TEST]
+3	-3	tests/unit/igraph_all_st_mincuts.c	[TEST]
+10	-10	tests/unit/igraph_almost_equals.c	[TEST]
+1	-2	tests/unit/igraph_are_connected.c => tests/unit/igraph_are_adjacent.c	[TEST]
+1	-2	tests/unit/igraph_arpack_rnsolve.c	[TEST]
+2	-2	tests/unit/igraph_arpack_unpack_complex.c	[TEST]
+1	-1	tests/unit/igraph_atlas.c	[TEST]
+1	-1	tests/unit/igraph_attribute_combination_remove.c	[TEST]
+2	-2	tests/unit/igraph_average_path_length.c	[TEST]
+4	-4	tests/unit/igraph_average_path_length_dijkstra.c	[TEST]
+1	-1	tests/unit/igraph_barabasi_aging_game.c	[TEST]
+3	-3	tests/unit/igraph_barabasi_game.c	[TEST]
+37	-38	tests/unit/igraph_betweenness.c	[TEST] ← CENTRALITY
+67	-68	tests/unit/igraph_betweenness_subset.c	[TEST] ← CENTRALITY
+56	-26	tests/unit/igraph_biadjacency.c	[TEST] ← CONSTRUCTORS
+59	-4	tests/unit/igraph_biadjacency.out	[TEST] ← CONSTRUCTORS
+2	-2	tests/unit/igraph_biconnected_components.c	[TEST]
+5	-5	tests/unit/igraph_bipartite_create.c	[TEST]
+266	-87	tests/unit/igraph_bipartite_game.c	[TEST] ← BIPARTITE
+3	-4	tests/unit/igraph_bipartite_projection.c	[TEST]
+1	-1	tests/unit/igraph_blas_dgemm.c	[TEST]
+1	-1	tests/unit/igraph_callaway_traits_game.c	[TEST]
+7	-7	tests/unit/igraph_chung_lu_game.c	[TEST]
+2	-2	tests/unit/igraph_circulant.c	[TEST]
+1	-1	tests/unit/igraph_cited_type_game.c	[TEST]
+1	-1	tests/unit/igraph_citing_cited_type_game.c	[TEST]
+1	-1	tests/unit/igraph_clique_size_hist.c	[TEST]
+6	-6	tests/unit/igraph_closeness.c	[TEST]
+2	-2	tests/unit/igraph_cohesion.c	[TEST]
+2	-2	tests/unit/igraph_cohesive_blocks.c	[TEST]
+16	-16	tests/unit/igraph_community_eb_get_merges.c	[TEST]
+45	-33	tests/unit/igraph_community_edge_betweenness.c	[TEST] ← COMM
+2	-3	tests/unit/igraph_community_fastgreedy.c	[TEST]
+2	-4	tests/unit/igraph_community_fluid_communities.c	[TEST]
+105	-61	tests/unit/igraph_community_infomap.c	[TEST] ← COMM-INFOMAP
+45	-8	tests/unit/igraph_community_infomap.out	[TEST] ← COMM-INFOMAP
+1	-2	tests/unit/igraph_community_leading_eigenvector2.c	[TEST] ← DS-VECTOR
+169	-0	tests/unit/igraph_community_optimal_modularity.c	[TEST] ← COMM
+5	-5	tests/unit/igraph_community_voronoi.c	[TEST]
+1	-1	tests/unit/igraph_compare_communities.c	[TEST]
+2	-3	tests/unit/igraph_complex.c	[TEST]
+2	-2	tests/unit/igraph_connect_neighborhood.c	[TEST]
+1	-1	tests/unit/igraph_constraint.c	[TEST]
+17	-17	tests/unit/igraph_contract_vertices.c	[TEST]
+2	-3	tests/unit/igraph_convergence_degree.c	[TEST] ← PROPS
+5	-6	tests/unit/igraph_convex_hull_2d.c	[TEST]
+11	-3	tests/unit/igraph_correlated_game.c	[TEST] ← GAMES
+1	-1	tests/unit/igraph_correlated_pair_game.c	[TEST]
+1	-1	tests/unit/igraph_count_adjacent_triangles.c	[TEST]
+3	-3	tests/unit/igraph_create.c	[TEST]
+2	-3	tests/unit/igraph_decompose_strong.c	[TEST]
+40	-16	tests/unit/igraph_degree.c	[TEST] ← PROPS
+9	-6	tests/unit/igraph_degree.out	[TEST] ← PROPS
+21	-20	tests/unit/igraph_degree_sequence_game.c	[TEST] ← GAMES
+217	-0	tests/unit/igraph_delaunay_graph.c	[TEST] ← SPATIAL
+713	-0	tests/unit/igraph_delaunay_graph.out	[TEST] ← SPATIAL
+1	-1	tests/unit/igraph_delete_edges.c	[TEST]
+1	-1	tests/unit/igraph_delete_vertices.c	[TEST]
+84	-25	tests/unit/igraph_density.c	[TEST] ← PROPS
+11	-15	tests/unit/igraph_diameter.c	[TEST] ← PROPS
+5	-6	tests/unit/igraph_diameter_dijkstra.c	[TEST] ← PROPS
+2	-3	tests/unit/igraph_disjoint_union.c	[TEST]
+4	-4	tests/unit/igraph_distances_floyd_warshall.c	[TEST] ← PATHS
+5	-5	tests/unit/igraph_distances_floyd_warshall_speedup.c	[TEST] ← PATHS
+45	-17	tests/unit/igraph_distances_johnson.c	[TEST] ← PATHS
+19	-2	tests/unit/igraph_distances_johnson.out	[TEST] ← PATHS
+0	-1	tests/unit/igraph_diversity.c	[TEST]
+1	-1	tests/unit/igraph_dominator_tree.c	[TEST]
+1	-1	tests/unit/igraph_dot_product_game.c	[TEST]
+1	-1	tests/unit/igraph_dyad_census.c	[TEST]
+15	-15	tests/unit/igraph_ecc.c	[TEST]
+9	-9	tests/unit/igraph_eccentricity.c	[TEST] ← PROPS
+5	-5	tests/unit/igraph_eccentricity_dijkstra.c	[TEST] ← PROPS
+101	-19	tests/unit/igraph_edge_betweenness.c	[TEST] ← CENTRALITY
+8	-0	tests/unit/igraph_edge_betweenness.out	[TEST] ← CENTRALITY
+62	-64	tests/unit/igraph_edge_betweenness_subset.c	[TEST] ← CENTRALITY
+2	-2	tests/unit/igraph_edge_disjoint_paths.c	[TEST]
+10	-3	tests/unit/igraph_edges.c	[TEST]
+6	-3	tests/unit/igraph_edges.out	[TEST]
+3	-4	tests/unit/igraph_eigen_matrix.c	[TEST] ← DS-MATRIX
+1	-2	tests/unit/igraph_eigen_matrix2.c	[TEST] ← DS-MATRIX
+1	-2	tests/unit/igraph_eigen_matrix3.c	[TEST] ← DS-MATRIX
+1	-2	tests/unit/igraph_eigen_matrix4.c	[TEST] ← DS-MATRIX
+3	-4	tests/unit/igraph_eigen_matrix_symmetric.c	[TEST] ← DS-MATRIX
+3	-4	tests/unit/igraph_eigen_matrix_symmetric_arpack.c	[TEST] ← DS-MATRIX
+63	-24	tests/unit/igraph_eigenvector_centrality.c	[TEST] ← CENTRALITY
+30	-0	tests/unit/igraph_eigenvector_centrality.out	[TEST] ← CENTRALITY
+1	-2	tests/unit/igraph_empty.c	[TEST]
+15	-16	tests/unit/igraph_es_all_between.c	[TEST]
+6	-7	tests/unit/igraph_es_path.c	[TEST]
+1	-1	tests/unit/igraph_establishment_game.c	[TEST]
+1	-1	tests/unit/igraph_extended_chordal_ring.c	[TEST]
+11	-11	tests/unit/igraph_feedback_arc_set.c	[TEST]
+7	-7	tests/unit/igraph_feedback_vertex_set.c	[TEST]
+1	-1	tests/unit/igraph_forest_fire_game.c	[TEST]
+4	-4	tests/unit/igraph_from_prufer.c	[TEST]
+11	-11	tests/unit/igraph_full_bipartite.c	[TEST]
+2	-2	tests/unit/igraph_full_citation.c	[TEST]
+1	-1	tests/unit/igraph_full_multipartite.c	[TEST]
+1	-1	tests/unit/igraph_generalized_petersen.c	[TEST]
+5	-5	tests/unit/igraph_get_adjacency.c	[TEST] ← CONSTRUCTORS
+6	-5	tests/unit/igraph_get_adjacency_sparse.c	[TEST] ← CONSTRUCTORS
+8	-8	tests/unit/igraph_get_all_shortest_paths_dijkstra.c	[TEST] ← PATHS
+30	-21	tests/unit/igraph_get_all_simple_paths.c	[TEST] ← PATHS
+81	-10	tests/unit/igraph_get_all_simple_paths.out	[TEST] ← PATHS
+3	-3	tests/unit/igraph_get_biadjacency.c	[TEST] ← CONSTRUCTORS
+2	-2	tests/unit/igraph_get_eid.c	[TEST]
+5	-5	tests/unit/igraph_get_isomorphisms_vf2.c	[TEST]
+4	-4	tests/unit/igraph_get_k_shortest_paths.c	[TEST] ← PATHS
+1	-2	tests/unit/igraph_get_laplacian.c	[TEST]
+16	-16	tests/unit/igraph_get_shortest_path_astar.c	[TEST] ← PATHS
+1	-1	tests/unit/igraph_get_shortest_path_bellman_ford.c	[TEST] ← PATHS
+7	-8	tests/unit/igraph_get_shortest_paths2.c	[TEST] ← PATHS
+20	-21	tests/unit/igraph_get_shortest_paths_bellman_ford.c	[TEST] ← PATHS
+18	-19	tests/unit/igraph_get_shortest_paths_dijkstra.c	[TEST] ← PATHS
+3	-3	tests/unit/igraph_get_stochastic.c	[TEST]
+1	-1	tests/unit/igraph_get_stochastic_sparse.c	[TEST]
+5	-5	tests/unit/igraph_get_subisomorphisms_vf2.c	[TEST]
+5	-6	tests/unit/igraph_gomory_hu_tree.c	[TEST]
+50	-50	tests/unit/igraph_graph_center.c	[TEST]
+1	-1	tests/unit/igraph_graph_center.out	[TEST]
+2	-2	tests/unit/igraph_graph_power.c	[TEST]
+1	-1	tests/unit/igraph_grg_game.c	[TEST]
+2	-2	tests/unit/igraph_growing_random_game.c	[TEST]
+1	-1	tests/unit/igraph_has_mutual.c	[TEST]
+1	-1	tests/unit/igraph_hexagonal_lattice.c	[TEST]
+9	-6	tests/unit/igraph_hrg.c	[TEST]
+2	-2	tests/unit/igraph_hrg2.c	[TEST]
+2	-2	tests/unit/igraph_hrg3.c	[TEST]
+1	-1	tests/unit/igraph_hrg_create.c	[TEST]
+2	-2	tests/unit/igraph_hsbm_game.c	[TEST] ← GAMES
+2	-2	tests/unit/igraph_hsbm_list_game.c	[TEST]
+2	-7	tests/unit/igraph_i_layout_sphere.c	[TEST]
+0	-122	tests/unit/igraph_i_neighbors.c	[TEST] ← ITERATORS
+1	-6	tests/unit/igraph_i_umap_fit_ab.c	[TEST]
+0	-8	tests/unit/igraph_i_umap_fit_ab.o	[TEST]
+8	-0	tests/unit/igraph_i_umap_fit_ab.out	[TEST]
+8	-9	tests/unit/igraph_i_incident.c => tests/unit/igraph_incident.c	[TEST] ← ITERATORS
+2	-1	tests/unit/igraph_i_incident.out => tests/unit/igraph_incident.out	[TEST] ← ITERATORS
+1	-2	tests/unit/igraph_induced_subgraph.c	[TEST]
+1	-1	tests/unit/igraph_induced_subgraph_edges.c	[TEST]
+2	-3	tests/unit/igraph_induced_subgraph_map.c	[TEST]
+1	-1	tests/unit/igraph_induced_subgraph_map.out	[TEST]
+1	-2	tests/unit/igraph_intersection.c	[TEST]
+1	-1	tests/unit/igraph_is_acyclic.c	[TEST]
+1	-1	tests/unit/igraph_is_biconnected.c	[TEST]
+1	-1	tests/unit/igraph_is_chordal.c	[TEST]
+1	-1	tests/unit/igraph_is_clique.c	[TEST]
+5	-5	tests/unit/igraph_is_complete.c	[TEST]
+1	-1	tests/unit/igraph_is_connected.c	[TEST]
+3	-3	tests/unit/igraph_is_dag.c	[TEST]
+1	-1	tests/unit/igraph_is_forest.c	[TEST]
+9	-13	tests/unit/igraph_is_forest2.c	[TEST]
+2	-2	tests/unit/igraph_is_mutual.c	[TEST]
+1	-1	tests/unit/igraph_is_same_graph.c	[TEST]
+3	-3	tests/unit/igraph_is_separator.c	[TEST]
+1	-1	tests/unit/igraph_is_tree.c	[TEST]
+1	-1	tests/unit/igraph_isomorphic.c	[TEST] ← ISO
+1	-2	tests/unit/igraph_isomorphic_bliss.c	[TEST] ← ISO
+7	-4	tests/unit/igraph_isomorphic_vf2.c	[TEST] ← ISO
+1	-2	tests/unit/igraph_join.c	[TEST]
+37	-34	tests/unit/igraph_joint_degree_distribution.c	[TEST] ← PROPS
+4	-4	tests/unit/igraph_joint_type_distribution.c	[TEST]
+22	-23	tests/unit/igraph_k_regular_game.c	[TEST] ← GAMES
+1	-1	tests/unit/igraph_kautz.c	[TEST]
+11	-11	tests/unit/igraph_lapack_dgeev.c	[TEST]
+14	-14	tests/unit/igraph_lapack_dgeevx.c	[TEST]
+1	-2	tests/unit/igraph_lapack_dgehrd.c	[TEST]
+1	-1	tests/unit/igraph_lapack_dgetrf.c	[TEST]
+2	-2	tests/unit/igraph_lapack_dgetrs.c	[TEST]
+7	-8	tests/unit/igraph_lapack_dsyevr.c	[TEST]
+1	-1	tests/unit/igraph_lastcit_game.c	[TEST]
+2	-2	tests/unit/igraph_layout_align.c	[TEST]
+1	-1	tests/unit/igraph_layout_bipartite.c	[TEST]
+2	-2	tests/unit/igraph_layout_davidson_harel.c	[TEST]
+1	-1	tests/unit/igraph_layout_drl.c	[TEST]
+1	-1	tests/unit/igraph_layout_drl_3d.c	[TEST]
+1	-1	tests/unit/igraph_layout_fruchterman_reingold.c	[TEST]
+1	-1	tests/unit/igraph_layout_fruchterman_reingold_3d.c	[TEST]
+2	-2	tests/unit/igraph_layout_gem.c	[TEST]
+1	-1	tests/unit/igraph_layout_graphopt.c	[TEST]
+1	-2	tests/unit/igraph_layout_grid.c	[TEST]
+1	-1	tests/unit/igraph_layout_kamada_kawai.c	[TEST]
+2	-3	tests/unit/igraph_layout_lgl.c	[TEST]
+2	-7	tests/unit/igraph_layout_mds.c	[TEST]
+3	-4	tests/unit/igraph_layout_merge.c	[TEST]
+2	-3	tests/unit/igraph_layout_merge2.c	[TEST]
+2	-3	tests/unit/igraph_layout_merge3.c	[TEST]
+1	-1	tests/unit/igraph_layout_random_3d.c	[TEST]
+1	-1	tests/unit/igraph_layout_reingold_tilford_circular.c	[TEST]
+2	-3	tests/unit/igraph_layout_reingold_tilford_extended.c	[TEST]
+1	-1	tests/unit/igraph_layout_sphere.c	[TEST]
+2	-2	tests/unit/igraph_layout_star.c	[TEST]
+81	-29	tests/unit/igraph_layout_sugiyama.c	[TEST] ← LAYOUT
+169	-87	tests/unit/igraph_layout_sugiyama.out	[TEST] ← LAYOUT
+11	-11	tests/unit/igraph_layout_umap.c	[TEST]
+69	-0	tests/unit/igraph_lcf.c	[TEST] ← CONSTRUCTORS
+1	-1	tests/unit/igraph_le_community_to_membership.c	[TEST]
+1	-1	tests/unit/igraph_linegraph.c	[TEST]
+1	-1	tests/unit/igraph_list_triangles.c	[TEST]
+1	-1	tests/unit/igraph_local_scan_k_ecount.c	[TEST]
+1	-1	tests/unit/igraph_local_scan_k_ecount_them.c	[TEST]
+1	-1	tests/unit/igraph_local_scan_subset_ecount.c	[TEST]
+7	-8	tests/unit/igraph_local_transitivity.c	[TEST]
+18	-18	tests/unit/igraph_maxflow.c	[TEST]
+24	-16	tests/unit/igraph_maximal_cliques.c	[TEST] ← CLIQUES
+9	-8	tests/unit/igraph_maximal_cliques2.c	[TEST] ← CLIQUES
+5	-5	tests/unit/igraph_maximal_cliques3.c	[TEST] ← CLIQUES
+10	-8	tests/unit/igraph_maximal_cliques4.c	[TEST] ← CLIQUES
+5	-5	tests/unit/igraph_maximal_cliques_file.c	[TEST] ← CLIQUES
+7	-7	tests/unit/igraph_maximum_bipartite_matching.c	[TEST]
+1	-1	tests/unit/igraph_mean_degree.c	[TEST] ← PROPS
+24	-20	tests/unit/igraph_minimum_size_separators.c	[TEST] ← CONNECTIVITY
+49	-24	tests/unit/igraph_minimum_size_separators.out	[TEST] ← CONNECTIVITY
+1	-2	tests/unit/igraph_modularity.c	[TEST]
+2	-2	tests/unit/igraph_modularity_matrix.c	[TEST] ← DS-MATRIX
+4	-5	tests/unit/igraph_motifs_randesu.c	[TEST] ← MISC
+5	-5	tests/unit/igraph_motifs_randesu_estimate.c	[TEST] ← MISC
+4	-4	tests/unit/igraph_motifs_randesu_no.c	[TEST] ← MISC
+278	-0	tests/unit/igraph_nearest_neighbor_graph.c	[TEST] ← SPATIAL
+809	-0	tests/unit/igraph_nearest_neighbor_graph.out	[TEST] ← SPATIAL
+1	-1	tests/unit/igraph_neighborhood.c	[TEST]
+2	-2	tests/unit/igraph_neighborhood_graphs.c	[TEST]
+1	-1	tests/unit/igraph_neighborhood_size.c	[TEST]
+155	-12	tests/unit/igraph_neighbors.c	[TEST] ← ITERATORS
+26	-1	tests/unit/igraph_i_neighbors.out => tests/unit/igraph_neighbors.out	[TEST] ← ITERATORS
+74	-75	tests/unit/igraph_pagerank.c	[TEST] ← CENTRALITY
+1	-1	tests/unit/igraph_path_length_hist.c	[TEST]
+3	-4	tests/unit/igraph_perfect.c	[TEST]
+1	-1	tests/unit/igraph_permute_vertices.c	[TEST]
+3	-4	tests/unit/igraph_power_law_fit.c	[TEST]
+2	-3	tests/unit/igraph_preference_game.c	[TEST]
+10	-10	tests/unit/igraph_product.c	[TEST]
+1	-1	tests/unit/igraph_progress_handler_stderr.c	[TEST]
+6	-6	tests/unit/igraph_pseudo_diameter.c	[TEST] ← PROPS
+8	-8	tests/unit/igraph_pseudo_diameter_dijkstra.c	[TEST] ← PROPS
+2	-7	tests/unit/igraph_psumtree.c	[DS-OTHER]
+1	-2	tests/unit/igraph_qsort.c	[DS-OTHER]
+3	-4	tests/unit/igraph_qsort_r.c	[DS-OTHER]
+3	-3	tests/unit/igraph_random_sample.c	[TEST]
+6	-6	tests/unit/igraph_random_walk.c	[TEST]
+1	-2	tests/unit/igraph_read_graph_graphdb.c	[TEST]
+4	-5	tests/unit/igraph_read_graph_graphml.c	[TEST]
+19	-19	tests/unit/igraph_realize_bipartite_degree_sequence.c	[TEST] ← PROPS
+1	-1	tests/unit/igraph_recent_degree_aging_game.c	[TEST] ← PROPS
+1	-1	tests/unit/igraph_recent_degree_game.c	[TEST] ← PROPS
+7	-7	tests/unit/igraph_reindex_membership.c	[TEST]
+1	-1	tests/unit/igraph_residual_graph.c	[TEST]
+1	-1	tests/unit/igraph_reverse_edges.c	[TEST]
+8	-9	tests/unit/igraph_rewire.c	[TEST] ← OPERATORS
+2	-2	tests/unit/igraph_rewire_directed_edges.c	[TEST] ← OPERATORS
+9	-10	tests/unit/igraph_rng_get_integer.c	[TEST]
+9	-9	tests/unit/igraph_sample_dirichlet.c => tests/unit/igraph_rng_sample_dirichlet.c	[TEST] ← SAMPLING
+0	-0	tests/unit/igraph_sample_dirichlet.out => tests/unit/igraph_rng_sample_dirichlet.out	[TEST] ← SAMPLING
+6	-6	tests/unit/igraph_sample_sphere.c => tests/unit/igraph_rng_sample_sphere.c	[TEST] ← SAMPLING
+1	-1	tests/unit/igraph_rooted_product.c	[TEST]
+1	-1	tests/unit/igraph_running_mean.c	[TEST]
+69	-19	tests/unit/igraph_sbm_game.c	[TEST] ← GAMES
+0	-1	tests/unit/igraph_sbm_game.out	[TEST] ← GAMES
+1	-1	tests/unit/igraph_set_progress_handler.c	[TEST]
+11	-8	tests/unit/igraph_similarity.c	[TEST] ← MISC
+2	-0	tests/unit/igraph_similarity.out	[TEST] ← MISC
+10	-10	tests/unit/igraph_simple_cycles.c	[TEST]
+1	-1	tests/unit/igraph_simple_interconnected_islands_game.c	[TEST]
+4	-4	tests/unit/igraph_sir.c	[TEST]
+1	-1	tests/unit/igraph_solve_lsap.c	[TEST]
+12	-12	tests/unit/igraph_spanner.c	[TEST]
+8	-13	tests/unit/igraph_sparsemat2.c	[TEST] ← DS-SPARSEMAT
+2	-3	tests/unit/igraph_sparsemat5.c	[TEST] ← DS-SPARSEMAT
+1	-2	tests/unit/igraph_sparsemat9.c	[TEST] ← DS-SPARSEMAT
+1	-1	tests/unit/igraph_sparsemat_droptol.c	[TEST] ← DS-SPARSEMAT
+3	-3	tests/unit/igraph_sparsemat_fkeep.c	[TEST] ← DS-SPARSEMAT
+1	-1	tests/unit/igraph_sparsemat_getelements_sorted.c	[TEST] ← DS-SPARSEMAT
+1	-2	tests/unit/igraph_sparsemat_is_symmetric.c	[TEST] ← DS-SPARSEMAT
+1	-1	tests/unit/igraph_sparsemat_iterator_idx.c	[TEST] ← DS-SPARSEMAT
+2	-3	tests/unit/igraph_sparsemat_minmax.c	[TEST] ← DS-SPARSEMAT
+1	-1	tests/unit/igraph_sparsemat_nonzero_storage.c	[TEST] ← DS-SPARSEMAT
+1	-1	tests/unit/igraph_sparsemat_normalize.c	[TEST] ← DS-SPARSEMAT
+0	-47	tests/unit/igraph_sparsemat_view.c	[TEST] ← DS-SPARSEMAT
+3	-4	tests/unit/igraph_sparsemat_which_minmax.c	[TEST] ← DS-SPARSEMAT
+64	-0	tests/unit/igraph_spatial_edge_lengths.c	[TEST] ← SPATIAL
+7	-0	tests/unit/igraph_spatial_edge_lengths.out	[TEST] ← SPATIAL
+2	-2	tests/unit/igraph_split_join_distance.c	[TEST]
+6	-7	tests/unit/igraph_square_lattice.c	[TEST]
+2	-2	tests/unit/igraph_st_edge_connectivity.c	[TEST]
+1	-1	tests/unit/igraph_st_mincut.c	[TEST]
+1	-1	tests/unit/igraph_st_mincut_value.c	[TEST]
+4	-4	tests/unit/igraph_st_vertex_connectivity.c	[TEST]
+13	-13	tests/unit/igraph_static_power_law_game.c	[TEST]
+10	-4	tests/unit/igraph_strvector.c	[TEST] ← DS-STRVECTOR
+14	-0	tests/unit/igraph_strvector.out	[TEST] ← DS-STRVECTOR
+3	-3	tests/unit/igraph_subcomponent.c	[TEST]
+1	-1	tests/unit/igraph_subisomorphic.c	[TEST] ← ISO
+16	-14	tests/unit/igraph_subisomorphic_lad.c	[TEST] ← ISO
+11	-17	tests/unit/igraph_to_prufer.c	[TEST]
+2	-2	tests/unit/igraph_transitive_closure.c	[TEST]
+1	-1	tests/unit/igraph_transitivity_avglocal_undirected.c	[TEST]
+1	-1	tests/unit/igraph_transitivity_barrat.c	[TEST]
+1	-1	tests/unit/igraph_triangular_lattice.c	[TEST]
+4	-6	tests/unit/igraph_trussness.c	[TEST]
+1	-2	tests/unit/igraph_turan.c	[TEST]
+1	-1	tests/unit/igraph_unfold_tree.c	[TEST]
+7	-8	tests/unit/igraph_union.c	[TEST]
+1	-1	tests/unit/igraph_vector_floor.c	[TEST] ← DS-VECTOR
+1	-1	tests/unit/igraph_vector_lex_cmp.c	[TEST] ← DS-VECTOR
+2	-2	tests/unit/igraph_vertex_disjoint_paths.c	[TEST]
+2	-2	tests/unit/igraph_voronoi.c	[TEST]
+24	-33	tests/unit/igraph_weighted_adjacency.c	[TEST] ← CONSTRUCTORS
+85	-92	tests/unit/igraph_weighted_adjacency.out	[TEST] ← CONSTRUCTORS
+108	-0	tests/unit/igraph_weighted_biadjacency.c	[TEST] ← CONSTRUCTORS
+75	-0	tests/unit/igraph_weighted_biadjacency.out	[TEST] ← CONSTRUCTORS
+18	-18	tests/unit/igraph_weighted_cliques.c	[TEST] ← CLIQUES
+3	-3	tests/unit/igraph_wheel.c	[TEST]
+3	-3	tests/unit/igraph_write_graph_dimacs_flow.c	[TEST]
+1	-1	tests/unit/igraph_write_graph_dot.c	[TEST]
+1	-2	tests/unit/igraph_write_graph_leda.c	[TEST]
+1	-1	tests/unit/inclist.c	[TEST]
+1	-1	tests/unit/is_coloring.c	[TEST]
+22	-23	tests/unit/isoclasses.c	[TEST]
+19	-19	tests/unit/isoclasses2.c	[TEST]
+16	-22	tests/unit/isomorphism_test.c	[TEST]
+1	-1	tests/unit/jdm.c	[TEST]
+1	-1	tests/unit/kary_tree.c	[TEST]
+4	-5	tests/unit/knn.c	[TEST]
+4	-5	tests/unit/levc-stress.c	[TEST]
+2	-3	tests/unit/lineendings.c	[TEST]
+2	-3	tests/unit/marked_queue.c	[TEST]
+2	-3	tests/unit/matrix.c	[TEST] ← DS-MATRIX
+4	-5	tests/unit/matrix2.c	[TEST] ← DS-MATRIX
+1	-2	tests/unit/matrix3.c	[TEST] ← DS-MATRIX
+8	-9	tests/unit/matrix_complex.c	[TEST] ← DS-MATRIX
+240	-0	tests/unit/max_results.c	[TEST] ← CLIQUES
+5	-5	tests/unit/maximal_cliques_callback.c	[TEST] ← CLIQUES
+1	-1	tests/unit/maximal_cliques_hist.c	[TEST] ← CLIQUES
+88	-0	tests/unit/minimum_spanning_tree.c	[TEST] ← MISC
+14	-0	tests/unit/minimum_spanning_tree.out	[TEST] ← MISC
+1	-1	tests/unit/mycielskian.c	[TEST]
+1	-1	tests/unit/ncol.c	[TEST]
+23	-10	tests/unit/null_communities.c	[TEST] ← COMM
+2	-2	tests/unit/overflow.c	[TEST]
+3	-4	tests/unit/pajek.c	[TEST] ← IO
+1	-2	tests/unit/pajek2.c	[TEST] ← IO
+2	-3	tests/unit/pajek_bipartite.c	[TEST] ← IO
+1	-2	tests/unit/pajek_bipartite2.c	[TEST] ← IO
+30	-30	tests/unit/pajek_bipartite2.out	[TEST] ← IO
+1	-2	tests/unit/pajek_signed.c	[TEST] ← IO
+10	-10	tests/unit/pajek_signed.out	[TEST] ← IO
+1	-1	tests/unit/paths.c	[TEST]
+17	-17	tests/unit/percolation.c	[TEST]
+11	-2	tests/unit/prop_caching.c	[TEST] ← GRAPH
+5	-5	tests/unit/random_sampling.c	[TEST]
+1	-1	tests/unit/random_spanning_tree.c	[TEST] ← MISC
+2	-2	tests/unit/reachability.c	[TEST]
+13	-13	tests/unit/rich_club.c	[TEST]
+1	-2	tests/unit/ring.c	[TEST]
+3	-4	tests/unit/rng_init_destroy_max_bits_name_set_default.c	[TEST]
+1	-1	tests/unit/rng_reproducibility.c	[TEST]
+4	-5	tests/unit/set.c	[TEST]
+1	-1	tests/unit/simplify_and_colorize.c	[TEST]
+5	-6	tests/unit/single_target_shortest_path.c	[TEST] ← PATHS
+3	-6	tests/unit/spinglass.c	[TEST]
+1	-2	tests/unit/stack.c	[TEST]
+5	-5	tests/unit/strvector_set_len_remove_print.c	[TEST] ← DS-STRVECTOR
+1	-1	tests/unit/symmetric_tree.c	[TEST]
+110	-74	tests/unit/test_utilities.c	[TEST]
+16	-6	tests/unit/test_utilities.h	[TEST]
+1	-2	tests/unit/tls1.c	[TEST]
+1	-2	tests/unit/tls2.c	[TEST]
+1	-2	tests/unit/topological_sorting.c	[TEST]
+6	-6	tests/unit/tree_game.c	[TEST]
+5	-12	tests/unit/triad_census.c	[TEST]
+3	-4	tests/unit/trie.c	[TEST]
+25	-39	tests/unit/vector.c	[TEST] ← DS-VECTOR
+4	-7	tests/unit/vector.out	[TEST] ← DS-VECTOR
+12	-4	tests/unit/vector2.c	[TEST] ← DS-VECTOR
+5	-2	tests/unit/vector2.out	[TEST] ← DS-VECTOR
+1	-2	tests/unit/vector3.c	[TEST] ← DS-VECTOR
+22	-22	tests/unit/vector4.c	[TEST] ← DS-VECTOR
+2	-3	tests/unit/vector_list.c	[TEST] ← DS-VECTOR
+2	-3	tests/unit/vector_ptr.c	[TEST] ← DS-VECTOR
+1	-2	tests/unit/vector_ptr_sort_ind.c	[TEST] ← DS-VECTOR
+3	-4	tests/unit/vector_sort_ind.c	[TEST] ← DS-VECTOR
+1	-1	tests/unit/vertex_selectors.c	[TEST]
+7	-7	tests/unit/watts_strogatz_game.c	[TEST]
+7	-7	tests/unit/widest_paths.c	[TEST]
+1	-1	tests/unit/zapsmall.c	[TEST]
+1	-1	tests/unit/zero_allocs.c	[TEST]
+111	-0	tools/sampling_uniformity_test/test.cpp	[TOOL-SAMPLING]
+2	-0	vendor/CMakeLists.txt	[VENDOR-OTHER]
+2	-2	vendor/cs/cs.h	[VENDOR-OTHER]
+0	-2	vendor/cs/cs_randperm.c	[VENDOR-OTHER]
+2	-1	vendor/f2c/s_cat.c	[VENDOR-OTHER]
+4	-2	vendor/f2c/s_copy.c	[VENDOR-OTHER]
+16	-0	vendor/infomap/CITATION.cff	[VENDOR-INFOMAP]
+48	-0	vendor/infomap/CMakeLists.txt	[VENDOR-INFOMAP]
+674	-0	vendor/infomap/LICENSE_GPLv3.txt	[VENDOR-INFOMAP]
+162	-0	vendor/infomap/README.rst	[VENDOR-INFOMAP]
+103	-0	vendor/infomap/src/Infomap.h	[VENDOR-INFOMAP]
+240	-0	vendor/infomap/src/core/BiasedMapEquation.cpp	[VENDOR-INFOMAP]
+180	-0	vendor/infomap/src/core/BiasedMapEquation.h	[VENDOR-INFOMAP]
+165	-0	vendor/infomap/src/core/FlowData.h	[VENDOR-INFOMAP]
+26	-0	vendor/infomap/src/core/InfoEdge.cpp	[VENDOR-INFOMAP]
+47	-0	vendor/infomap/src/core/InfoEdge.h	[VENDOR-INFOMAP]
+405	-0	vendor/infomap/src/core/InfoNode.cpp	[VENDOR-INFOMAP]
+374	-0	vendor/infomap/src/core/InfoNode.h	[VENDOR-INFOMAP]
+2182	-0	vendor/infomap/src/core/InfomapBase.cpp	[VENDOR-INFOMAP]
+586	-0	vendor/infomap/src/core/InfomapBase.h	[VENDOR-INFOMAP]
+137	-0	vendor/infomap/src/core/InfomapConfig.h	[VENDOR-INFOMAP]
+766	-0	vendor/infomap/src/core/InfomapOptimizer.h	[VENDOR-INFOMAP]
+113	-0	vendor/infomap/src/core/InfomapOptimizerBase.h	[VENDOR-INFOMAP]
+339	-0	vendor/infomap/src/core/MapEquation.h	[VENDOR-INFOMAP]
+451	-0	vendor/infomap/src/core/MemMapEquation.cpp	[VENDOR-INFOMAP]
+174	-0	vendor/infomap/src/core/MemMapEquation.h	[VENDOR-INFOMAP]
+271	-0	vendor/infomap/src/core/MetaMapEquation.cpp	[VENDOR-INFOMAP]
+185	-0	vendor/infomap/src/core/MetaMapEquation.h	[VENDOR-INFOMAP]
+329	-0	vendor/infomap/src/core/StateNetwork.cpp	[VENDOR-INFOMAP]
+216	-0	vendor/infomap/src/core/StateNetwork.h	[VENDOR-INFOMAP]
+238	-0	vendor/infomap/src/core/iterators/InfomapIterator.cpp	[VENDOR-INFOMAP]
+341	-0	vendor/infomap/src/core/iterators/InfomapIterator.h	[VENDOR-INFOMAP]
+32	-0	vendor/infomap/src/core/iterators/IterWrapper.h	[VENDOR-INFOMAP]
+369	-0	vendor/infomap/src/core/iterators/infomapIterators.h	[VENDOR-INFOMAP]
+628	-0	vendor/infomap/src/core/iterators/treeIterators.h	[VENDOR-INFOMAP]
+189	-0	vendor/infomap/src/io/ClusterMap.cpp	[VENDOR-INFOMAP]
+52	-0	vendor/infomap/src/io/ClusterMap.h	[VENDOR-INFOMAP]
+264	-0	vendor/infomap/src/io/Config.cpp	[VENDOR-INFOMAP]
+268	-0	vendor/infomap/src/io/Config.h	[VENDOR-INFOMAP]
+990	-0	vendor/infomap/src/io/Network.cpp	[VENDOR-INFOMAP]
+214	-0	vendor/infomap/src/io/Network.h	[VENDOR-INFOMAP]
+629	-0	vendor/infomap/src/io/Output.cpp	[VENDOR-INFOMAP]
+36	-0	vendor/infomap/src/io/Output.h	[VENDOR-INFOMAP]
+362	-0	vendor/infomap/src/io/ProgramInterface.cpp	[VENDOR-INFOMAP]
+423	-0	vendor/infomap/src/io/ProgramInterface.h	[VENDOR-INFOMAP]
+87	-0	vendor/infomap/src/io/SafeFile.h	[VENDOR-INFOMAP]
+69	-0	vendor/infomap/src/utils/Date.h	[VENDOR-INFOMAP]
+50	-0	vendor/infomap/src/utils/FileURI.cpp	[VENDOR-INFOMAP]
+54	-0	vendor/infomap/src/utils/FileURI.h	[VENDOR-INFOMAP]
+898	-0	vendor/infomap/src/utils/FlowCalculator.cpp	[VENDOR-INFOMAP]
+75	-0	vendor/infomap/src/utils/FlowCalculator.h	[VENDOR-INFOMAP]
+17	-0	vendor/infomap/src/utils/Log.cpp	[VENDOR-INFOMAP]
+110	-0	vendor/infomap/src/utils/Log.h	[VENDOR-INFOMAP]
+153	-0	vendor/infomap/src/utils/MetaCollection.h	[VENDOR-INFOMAP]
+45	-0	vendor/infomap/src/utils/Random.h	[VENDOR-INFOMAP]
+103	-0	vendor/infomap/src/utils/Stopwatch.h	[VENDOR-INFOMAP]
+82	-0	vendor/infomap/src/utils/VectorMap.h	[VENDOR-INFOMAP]
+216	-0	vendor/infomap/src/utils/convert.h	[VENDOR-INFOMAP]
+57	-0	vendor/infomap/src/utils/infomath.h	[VENDOR-INFOMAP]
+19	-0	vendor/infomap/src/version.h	[VENDOR-INFOMAP]
+1	-2	vendor/lapack/fortran_intrinsics.c	[VENDOR-OTHER]
+80	-36	vendor/mini-gmp/mini-gmp.c	[VENDOR-OTHER]
+1	-0	vendor/mini-gmp/mini-gmp.h	[VENDOR-OTHER]
+2813	-0	vendor/nanoflann/nanoflann.hpp	[VENDOR-NANOFLANN]
+2	-2	vendor/plfit/gss.h	[VENDOR-OTHER]
+2	-2	vendor/plfit/hzeta.h	[VENDOR-OTHER]
+2	-2	vendor/plfit/kolmogorov.h	[VENDOR-OTHER]
+7	-7	vendor/plfit/lbfgs.h	[VENDOR-OTHER]
+0	-1	vendor/plfit/plfit.c	[VENDOR-OTHER]
+2	-3	vendor/plfit/plfit.h	[VENDOR-OTHER]
+6	-6	vendor/plfit/plfit_decls.h	[VENDOR-OTHER]
+2	-2	vendor/plfit/plfit_error.h	[VENDOR-OTHER]
+2	-2	vendor/plfit/plfit_mt.h	[VENDOR-OTHER]
+2	-2	vendor/plfit/plfit_sampling.h	[VENDOR-OTHER]
+12	-0	vendor/qhull/CHANGES.md	[VENDOR-QHULL]
+48	-0	vendor/qhull/CMakeLists.txt	[VENDOR-QHULL]
+39	-0	vendor/qhull/COPYING.txt	[VENDOR-QHULL]
+720	-0	vendor/qhull/README.txt	[VENDOR-QHULL]
+69	-0	vendor/qhull/libqhull_r/accessors_r.c	[VENDOR-QHULL]
+2302	-0	vendor/qhull/libqhull_r/geom2_r.c	[VENDOR-QHULL]
+1284	-0	vendor/qhull/libqhull_r/geom_r.c	[VENDOR-QHULL]
+189	-0	vendor/qhull/libqhull_r/geom_r.h	[VENDOR-QHULL]
+2268	-0	vendor/qhull/libqhull_r/global_r.c	[VENDOR-QHULL]
+4128	-0	vendor/qhull/libqhull_r/io_r.c	[VENDOR-QHULL]
+166	-0	vendor/qhull/libqhull_r/io_r.h	[VENDOR-QHULL]
+1754	-0	vendor/qhull/libqhull_r/libqhull_r.c	[VENDOR-QHULL]
+1281	-0	vendor/qhull/libqhull_r/libqhull_r.h	[VENDOR-QHULL]
+566	-0	vendor/qhull/libqhull_r/mem_r.c	[VENDOR-QHULL]
+235	-0	vendor/qhull/libqhull_r/mem_r.h	[VENDOR-QHULL]
+5589	-0	vendor/qhull/libqhull_r/merge_r.c	[VENDOR-QHULL]
+238	-0	vendor/qhull/libqhull_r/merge_r.h	[VENDOR-QHULL]
+3959	-0	vendor/qhull/libqhull_r/poly2_r.c	[VENDOR-QHULL]
+1448	-0	vendor/qhull/libqhull_r/poly_r.c	[VENDOR-QHULL]
+310	-0	vendor/qhull/libqhull_r/poly_r.h	[VENDOR-QHULL]
+161	-0	vendor/qhull/libqhull_r/qhull_ra.h	[VENDOR-QHULL]
+1383	-0	vendor/qhull/libqhull_r/qset_r.c	[VENDOR-QHULL]
+515	-0	vendor/qhull/libqhull_r/qset_r.h	[VENDOR-QHULL]
+249	-0	vendor/qhull/libqhull_r/random_r.c	[VENDOR-QHULL]
+41	-0	vendor/qhull/libqhull_r/random_r.h	[VENDOR-QHULL]
+854	-0	vendor/qhull/libqhull_r/rboxlib_r.c	[VENDOR-QHULL]
+727	-0	vendor/qhull/libqhull_r/stat_r.c	[VENDOR-QHULL]
+563	-0	vendor/qhull/libqhull_r/stat_r.h	[VENDOR-QHULL]
+617	-0	vendor/qhull/libqhull_r/user_r.c	[VENDOR-QHULL]
+1061	-0	vendor/qhull/libqhull_r/user_r.h	[VENDOR-QHULL]
+102	-0	vendor/qhull/libqhull_r/usermem_r.c	[VENDOR-QHULL]
+68	-0	vendor/qhull/libqhull_r/userprintf_r.c	[VENDOR-QHULL]
+53	-0	vendor/qhull/libqhull_r/userprintf_rbox_r.c	[VENDOR-QHULL]
```