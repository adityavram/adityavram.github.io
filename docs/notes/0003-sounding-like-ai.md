
Most advice on spotting AI writing is a banned-word list. It is the wrong approach. A single "delve" or em dash proves nothing, and a human who uses either gets accused of using AI. The real signal is when several tells land in the same paragraph. That cluster is what gives a text away. Hunting individual words instead of clusters produces false accusations against real writers and misses AI text that simply avoids the banned words.

I started noticing my own drafts read as AI even when I had written them myself. The banned-word check found nothing. The cluster check found the problem. So I pulled the tells from the existing catalogs and the research, and I now scan every draft for clusters before I publish.

## What to count

The tells fall into five families, and a cluster usually draws from more than one. Vocabulary is the family people know: delve, leverage, navigate, landscape, tapestry, nuanced, robust, seamless, powerful. The signpost family pads without adding information. "It's worth noting", "it's important to remember", "at the end of the day" each set up a point the sentence then makes anyway. Cut the signpost and the sentence underneath says the same thing in fewer words. Punctuation is em dashes used as the default way into a punchline, several per paragraph. Structure is the rule of three. It reaches for three items whether the world offers two or seven. It also includes "not X, it is Y" contrast that adds nothing, announce-then-answer, signposting, and section-end summaries. Rhetoric and tone cover rhetorical questions as openers, passive voice, hedging stacks, meta-references, marketing language, paired adjectives with "yet", "excited to announce", and exclamation clusters.

What to count is the cluster, not any single tell. Three "robust" tokens in one paragraph is a hit. "It's worth noting" plus an em dash plus "simple yet powerful" in the same paragraph is a hit. One of each is not.

## The over-correction trap

Stripping every tell makes a new tell. Text reduced to nothing but commas and periods reads as flattened, and flattened text is its own AI signal. Keep em dashes and lists when they are deliberate choices rather than crutches.

## Models leave fingerprints

The model families have different defaults, so the cluster shape points at which model wrote the draft. GPT reaches for delve, tapestry, realm, and sets of three inside sentences. It builds symmetrical structure: an intro, three to five evenly weighted sections, a conclusion that restates the intro. Claude hedges and narrates its own reasoning ("I should note", "that said", "the nuance is"), acknowledges the reader before answering, writes longer clause-heavy sentences, surfaces trade-offs unprompted, and still overuses em dashes. Gemini formats first and writes second: bold lead-ins, nested bullets, tables for simple answers, encyclopedic tone, cautious disclaimers. GLM is less cataloged in English prose; the documented tells are from fiction generation.

## The skill

I packaged the catalog and the cluster protocol as an OpenCode skill, `anti-ai-writing`. Load it with `skill("anti-ai-writing")` before revising a draft. It marks every tell, clusters by paragraph, rewrites the clusters, replaces vocabulary tells with something specific, cuts signposts and summaries, collapses rule-of-three lists, varies sentence length, and takes a side. Then it re-reads once, because over-correction is its own tell.
