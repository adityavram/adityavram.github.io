
I cataloged the patterns that make AI writing read as AI, and built a skill that flags them in any draft.

I kept noticing my own drafts read as AI even when I had written them myself. So I pulled the common tells from the research and the existing catalogs, organized them, and turned them into an OpenCode skill that scans a draft and rewrites the hits.

## The tells

Five families.

Vocabulary is the easiest. Delve, leverage, navigate, landscape, tapestry, nuanced, robust, seamless, powerful. Replace with a specific number or name, or cut. Next, the signposts: "it's worth noting", "it's important to remember", "at the end of the day". They announce information instead of delivering it. Delete them and the sentence says the same thing in fewer words.

Punctuation: em dashes. One per few hundred words is fine. Several per paragraph is the tell. The mark is not the crime. Using it as a rhythmic crutch is.

Structure shows up next. The rule of three reaches for three items whether the world offers two or seven. "Fast, scalable, and secure." Pick the one that matters. Then "not X, it is Y" contrast where the negation adds nothing. Then announce-then-answer ("This piece will examine..."), signposting ("more on that below"), and section-end summaries ("As we can see, caching is effective"). End on the last real point.

Rhetoric and tone round it out. Rhetorical questions as openers. Passive voice. Hedging stacks. Meta-references. Marketing language. Paired adjectives with "yet" (simple yet powerful). "Excited to announce." Corporate and internet cliches. Exclamation clusters.

## Models differ

The families have different defaults. GPT reaches for delve, tapestry, realm, and sets of three inside sentences. It builds symmetrical structure: an intro, three to five evenly weighted sections, a conclusion that restates the intro. It scattered em dashes. It does less now.

Claude hedges and narrates its own reasoning. "I should note", "that said", "the nuance is". It acknowledges the reader before answering. It writes longer, clause-heavy sentences. It surfaces trade-offs unprompted. It says "I'm not certain" more readily than others. It still overuses em dashes. It reaches for metaphor where a plain phrase would do.

Gemini formats first and writes second. Bold lead-ins, nested bullets, tables for simple answers. Encyclopedic tone. Cautious disclaimers. List-first where a paragraph would do.

GLM is less cataloged in English prose. The documented tells are from fiction: code-switching, local vividness overwriting prior state, resolution templates over causality.

## The density principle

A single tell is not evidence. Humans use em dashes, write lists of three, and say "delve" once. The tell is density and co-occurrence. Three "robust" tokens in one paragraph. "It's worth noting" plus an em dash plus "simple yet powerful" in the same paragraph. Flag the cluster, not the word.

Over-correcting makes a new tell. Text stripped to nothing but commas and periods reads as flattened. Keep good tools when they are deliberate.

## The skill

The skill is `anti-ai-writing`. Load it with `skill("anti-ai-writing")` before revising a draft. It runs the catalog above against the text and applies the editing protocol: mark every hit, cluster by paragraph, rewrite the clusters, replace vocabulary tells with something specific, cut signposts and summaries, collapse rule-of-three lists, vary sentence length, take a side, re-read once.
