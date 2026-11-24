
I wanted my agents to serve a frontier language model at a tenth the cost of naive deployment, at equal quality. Inference is the dominant cost of serving one, so a 10× win is a 10× drop in the dominant cost line. The deployable levers get you ~1.5 to 4×, not 10×. The 10× lives in serving without the full forward pass, and nobody has shipped that. This note is the honest map of where the cost win really lives, and the open frontier.

## The validated pareto

Speculative decoding gives ~1.5 to 1.9× throughput at equal quality, because the target model verifies every draft token, so the output distribution is the target's by construction. N-gram spec decode validated 1.55×; a real 0.5B draft model validated 1.9×. The technique stacks with cheaper hardware when it is in stock, for a cumulative ~3-4×.

Quantization is the other deployable lever, and it is a dead end at this scale. AWQ int4 gave a 5.57× cost win on paper, but a 72B judge significantly preferred the bf16 baseline on open-ended generation. The lore that "AWQ int4 loses under 1pp" comes from MMLU on larger models; at 7B, AWQ measurably degrades quality. Cost win with quality loss is a regression, not a pareto point.

## The moonshot

The 10× lives in serving without running the full forward pass. The hypothesis: the trained weights encode the function, and there may be a way to serve equivalent outputs by reading the weight structure directly rather than invoking it. The existence proof is the brain, which serves a lifetime of training at ~10⁶× the energy efficiency of re-running the equivalent dense pass.

The bridge architecture is the concrete attempt. Compose sparse-autoencoder features (which localize a circuit) with activation-grounded weight decompositions (which are editable). On a known circuit in GPT-2 Small, a genuinely sparse SAE reconstructs layer 8 with 100% of the crossentropy recovered, and 3 features causally carry the circuit. But steering those features into a control prompt does not induce the behavior. The features that read the computation are not the features you can write to reproduce it. The ASPD half is the complement: weight components are editable and effective, about 300-600× the SAE steering effect, but at toy scale they do not converge to sparse components. The two halves have complementary strengths. The bridge hypothesis is that composing them gets faithful, sparse, and writable simultaneously, and that is a GPU-scale experiment, not a toy.

## The ideal

The ideal is the ~3-4× you can ship today: spec decode on the cheapest hardware in stock. The 10× is research, not deployment, and the bridge is the moonshot that motivates it. A deployed 10× endpoint is not a near-term milestone. A mapped frontier with a validated pareto and a real dead end is the honest near-term result.
