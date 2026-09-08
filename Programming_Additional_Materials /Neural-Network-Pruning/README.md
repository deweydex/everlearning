# Neural Network Pruning

`structured_pruning_notebook_cells.py` — a set of code cells (not a standalone notebook) implementing **structured pruning** for Keras/TensorFlow `Dense`-layer models: computing per-node importance (L1 norm of outgoing weights), rebuilding a structurally smaller model at a given `keep_fraction`, and plotting accuracy/F1/recall/precision vs. sparsity before and after fine-tuning.

This is graduate-level machine-learning content (model compression, structured vs. unstructured pruning) — nowhere near the QQI Level 5 MIT/PDP module descriptors, and unrelated even to general NumPy/matplotlib/OOP enrichment content, which doesn't cover model compression. The file is explicitly a fragment: it assumes a `model`, `Dense`, `np`, and `plt` already in scope from a notebook it was meant to be dropped into, which wasn't included in this upload.
