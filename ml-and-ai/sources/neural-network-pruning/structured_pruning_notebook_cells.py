# ============================================================
# STRUCTURED PRUNING - Drop these cells into your notebook
# ============================================================

# Cell 1: Define the pruning functions
# ------------------------------------------------------------

def compute_node_importance(model):
    """L1 norm of outgoing weights as node importance."""
    importance = {}
    dense_layers = [(i, layer) for i, layer in enumerate(model.layers) 
                    if isinstance(layer, Dense)]
    
    for idx, (layer_idx, layer) in enumerate(dense_layers[:-1]):  # Skip output layer
        weights = layer.get_weights()[0]
        importance[layer_idx] = np.sum(np.abs(weights), axis=0)
    return importance


def build_pruned_model(original_model, keep_fraction, l2_reg=0.0001):
    """
    Build a structurally smaller model by removing entire nodes.
    """
    dense_layers = [(i, layer) for i, layer in enumerate(original_model.layers) 
                    if isinstance(layer, Dense)]
    
    importance = compute_node_importance(original_model)
    
    # Determine nodes to keep per layer
    nodes_to_keep = {}
    new_sizes = []
    for layer_idx, scores in importance.items():
        n_keep = max(1, int(len(scores) * keep_fraction))
        keep_idx = sorted(np.argsort(scores)[-n_keep:])
        nodes_to_keep[layer_idx] = keep_idx
        new_sizes.append(n_keep)
    
    input_dim = dense_layers[0][1].get_weights()[0].shape[0]
    
    # Build smaller model
    new_model = Sequential()
    prev_kept = None
    
    for idx, (layer_idx, layer) in enumerate(dense_layers):
        W, b = layer.get_weights()
        
        if idx < len(dense_layers) - 1:  # Hidden layers
            keep_idx = nodes_to_keep[layer_idx]
            n_units = len(keep_idx)
            
            if idx == 0:
                new_model.add(Dense(n_units, activation='relu',
                                   kernel_regularizer=regularizers.l2(l2_reg),
                                   input_dim=input_dim))
                new_W = W[:, keep_idx]
            else:
                new_model.add(Dense(n_units, activation='relu',
                                   kernel_regularizer=regularizers.l2(l2_reg)))
                new_W = W[np.ix_(prev_kept, keep_idx)]
            
            new_model.layers[-1].set_weights([new_W, b[keep_idx]])
            new_model.add(Dropout(0.3))
            prev_kept = keep_idx
        else:  # Output layer
            new_model.add(Dense(1, activation='sigmoid'))
            new_model.layers[-1].set_weights([W[prev_kept, :], b])
    
    orig_sizes = [dense_layers[i][1].units for i in range(len(dense_layers)-1)]
    return new_model, {'original': orig_sizes, 'pruned': new_sizes}


def fine_tune_model(model, X_train, y_train, epochs=10, verbose=0):
    """
    Fine-tune the pruned model to let remaining weights adapt.
    Safe for structured pruning - can't resurrect removed nodes.
    """
    X_tr, X_val, y_tr, y_val = train_test_split(
        X_train, y_train, test_size=0.2, random_state=42
    )
    
    model.compile(
        loss='binary_crossentropy',
        optimizer=Adam(learning_rate=0.0001),
        metrics=['accuracy']
    )
    
    model.fit(
        X_tr, y_tr,
        validation_data=(X_val, y_val),
        epochs=epochs,
        batch_size=32,
        verbose=verbose,
        callbacks=[EarlyStopping(patience=5, restore_best_weights=True)]
    )
    return model


# Cell 2: Run the experiments - Compare with and without fine-tuning
# ------------------------------------------------------------

SPARSITY_LEVELS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
FINE_TUNE_EPOCHS = 10

pruning_results = []

for model_name, model in best_models.items():
    print(f"\nStructured Pruning: {model_name}")
    print("=" * 50)
    data = datasets[model_name]
    
    for sparsity in SPARSITY_LEVELS:
        if sparsity == 0.0:
            # Baseline - no pruning
            y_pred = (model.predict(data['X_test'], verbose=0) > 0.5).astype(int).flatten()
            arch = {'original': [], 'pruned': []}
            
            result = {
                'Model': model_name,
                'Sparsity': sparsity,
                'Fine_Tuned': False,
                'Architecture': 'Original',
                'Accuracy': accuracy_score(data['y_test'], y_pred),
                'Precision': precision_score(data['y_test'], y_pred, zero_division=0),
                'Recall': recall_score(data['y_test'], y_pred, zero_division=0),
                'F1': f1_score(data['y_test'], y_pred, zero_division=0)
            }
            pruning_results.append(result)
            print(f"  {sparsity:.0%} (baseline): Acc={result['Accuracy']:.3f}, F1={result['F1']:.3f}")
        else:
            # Build pruned model
            pruned, arch = build_pruned_model(model, keep_fraction=1.0-sparsity)
            
            # --- Without fine-tuning ---
            y_pred_no_ft = (pruned.predict(data['X_test'], verbose=0) > 0.5).astype(int).flatten()
            
            result_no_ft = {
                'Model': model_name,
                'Sparsity': sparsity,
                'Fine_Tuned': False,
                'Architecture': str(arch['pruned']),
                'Accuracy': accuracy_score(data['y_test'], y_pred_no_ft),
                'Precision': precision_score(data['y_test'], y_pred_no_ft, zero_division=0),
                'Recall': recall_score(data['y_test'], y_pred_no_ft, zero_division=0),
                'F1': f1_score(data['y_test'], y_pred_no_ft, zero_division=0)
            }
            pruning_results.append(result_no_ft)
            
            # --- With fine-tuning ---
            # Rebuild fresh (fine_tune modifies in place)
            pruned_ft, _ = build_pruned_model(model, keep_fraction=1.0-sparsity)
            pruned_ft = fine_tune_model(pruned_ft, data['X_train'], data['y_train'], 
                                        epochs=FINE_TUNE_EPOCHS, verbose=0)
            
            y_pred_ft = (pruned_ft.predict(data['X_test'], verbose=0) > 0.5).astype(int).flatten()
            
            result_ft = {
                'Model': model_name,
                'Sparsity': sparsity,
                'Fine_Tuned': True,
                'Architecture': str(arch['pruned']),
                'Accuracy': accuracy_score(data['y_test'], y_pred_ft),
                'Precision': precision_score(data['y_test'], y_pred_ft, zero_division=0),
                'Recall': recall_score(data['y_test'], y_pred_ft, zero_division=0),
                'F1': f1_score(data['y_test'], y_pred_ft, zero_division=0)
            }
            pruning_results.append(result_ft)
            
            print(f"  {sparsity:.0%}: {arch['pruned']}")
            print(f"       No FT:   Acc={result_no_ft['Accuracy']:.3f}, F1={result_no_ft['F1']:.3f}")
            print(f"       With FT: Acc={result_ft['Accuracy']:.3f}, F1={result_ft['F1']:.3f}")

pruning_df = pd.DataFrame(pruning_results)
pruning_df


# Cell 3: Visualize - Compare Fine-Tuned vs Not
# ------------------------------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for idx, model_name in enumerate(pruning_df['Model'].unique()):
    ax = axes[idx]
    subset = pruning_df[pruning_df['Model'] == model_name]
    
    # Plot without fine-tuning
    no_ft = subset[subset['Fine_Tuned'] == False]
    ax.plot(no_ft['Sparsity'] * 100, no_ft['F1'], 
            marker='o', linestyle='--', label='No Fine-Tuning', color='tab:blue')
    
    # Plot with fine-tuning (skip baseline which has no FT variant)
    with_ft = subset[subset['Fine_Tuned'] == True]
    ax.plot(with_ft['Sparsity'] * 100, with_ft['F1'], 
            marker='s', linestyle='-', label='With Fine-Tuning', color='tab:orange')
    
    ax.set_xlabel('Sparsity (%)')
    ax.set_ylabel('F1 Score')
    ax.set_title(f'{model_name}: Effect of Fine-Tuning')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('structured_pruning_ft_comparison.png', dpi=150, bbox_inches='tight')
plt.show()


# Cell 3b: Absolute metrics (with fine-tuning only, cleaner view)
# ------------------------------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# Use fine-tuned results for the "main" view
pruning_df_ft = pruning_df[(pruning_df['Fine_Tuned'] == True) | (pruning_df['Sparsity'] == 0.0)]

for idx, metric in enumerate(['Accuracy', 'F1', 'Recall']):
    ax = axes[idx]
    for model_name in pruning_df_ft['Model'].unique():
        subset = pruning_df_ft[pruning_df_ft['Model'] == model_name]
        ax.plot(subset['Sparsity'] * 100, subset[metric], marker='o', label=model_name)
    ax.set_xlabel('Sparsity (%)')
    ax.set_ylabel(metric)
    ax.set_title(f'{metric} vs Pruning Level (Fine-Tuned)')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('structured_pruning_analysis.png', dpi=150, bbox_inches='tight')
plt.show()


# Cell 4: Change from Baseline Plot - All Metrics (Fine-Tuned)
# ------------------------------------------------------------

# Use fine-tuned results for delta analysis
pruning_df_ft = pruning_df[(pruning_df['Fine_Tuned'] == True) | (pruning_df['Sparsity'] == 0.0)].copy()

# Calculate change from baseline (0% sparsity) for each model
for model_name in pruning_df_ft['Model'].unique():
    mask = pruning_df_ft['Model'] == model_name
    baseline = pruning_df_ft.loc[mask & (pruning_df_ft['Sparsity'] == 0.0)]
    
    for metric in ['Accuracy', 'F1', 'Recall', 'Precision']:
        baseline_val = baseline[metric].values[0]
        pruning_df_ft.loc[mask, f'{metric}_Delta'] = pruning_df_ft.loc[mask, metric] - baseline_val
        pruning_df_ft.loc[mask, f'{metric}_PctChange'] = 100 * (pruning_df_ft.loc[mask, metric] - baseline_val) / baseline_val if baseline_val != 0 else 0

# Plot: One subplot per model, all metrics on each
models = pruning_df_ft['Model'].unique()
metrics = ['Accuracy', 'F1', 'Recall', 'Precision']
metric_colors = {'Accuracy': 'tab:blue', 'F1': 'tab:orange', 'Recall': 'tab:green', 'Precision': 'tab:red'}
metric_markers = {'Accuracy': 'o', 'F1': 's', 'Recall': '^', 'Precision': 'd'}

fig, axes = plt.subplots(1, len(models), figsize=(5 * len(models), 5))
if len(models) == 1:
    axes = [axes]

for ax, model_name in zip(axes, models):
    subset = pruning_df_ft[pruning_df_ft['Model'] == model_name]
    
    for metric in metrics:
        ax.plot(subset['Sparsity'] * 100, subset[f'{metric}_PctChange'], 
                marker=metric_markers[metric], color=metric_colors[metric],
                label=metric, linewidth=2, markersize=6)
    
    ax.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    ax.set_xlabel('Sparsity (%)')
    ax.set_ylabel('Percent Change from Baseline (%)')
    ax.set_title(f'{model_name}: All Metrics vs Pruning (Fine-Tuned)')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pruning_all_metrics_pct_change.png', dpi=150, bbox_inches='tight')
plt.show()


# Alternative view: One subplot per metric, all models on each
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()
model_colors = {'Imbalanced': 'tab:blue', 'Balanced': 'tab:orange', 'Simple': 'tab:green'}

for ax, metric in zip(axes, metrics):
    for model_name in models:
        subset = pruning_df_ft[pruning_df_ft['Model'] == model_name]
        ax.plot(subset['Sparsity'] * 100, subset[f'{metric}_PctChange'], 
                marker='o', color=model_colors.get(model_name, None),
                label=model_name, linewidth=2, markersize=6)
    
    ax.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    ax.set_xlabel('Sparsity (%)')
    ax.set_ylabel(f'{metric} Percent Change (%)')
    ax.set_title(f'{metric}: Change from Baseline by Model')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pruning_by_metric_pct_change.png', dpi=150, bbox_inches='tight')
plt.show()


# Print summary table of changes at key sparsity levels
print("\nAll Metrics - Percent Change from Baseline at Key Sparsity Levels (Fine-Tuned):")
print("=" * 80)
for model_name in models:
    print(f"\n{model_name}:")
    print("-" * 80)
    subset = pruning_df_ft[
        (pruning_df_ft['Model'] == model_name) & 
        (pruning_df_ft['Sparsity'].isin([0.0, 0.5, 0.7, 0.9]))
    ][['Sparsity', 'Accuracy_PctChange', 'F1_PctChange', 'Recall_PctChange', 'Precision_PctChange']].round(2)
    subset.columns = ['Sparsity', 'Acc %Δ', 'F1 %Δ', 'Recall %Δ', 'Precision %Δ']
    print(subset.to_string(index=False))
