
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

The full skill is below. Paste it into `~/.config/opencode/skills/anti-ai-writing/SKILL.md` to install, then load it with `skill("anti-ai-writing")` before revising a draft.

```
---
name: anti-ai-writing
description: Use when writing or revising prose that must read as human. Catches and removes the vocabulary, punctuation, structural, and rhetorical patterns that make text sound AI-generated. Apply to any draft before publishing.
---

# Anti AI Writing

Removes the patterns that make prose read as AI-generated. Use it on any draft meant for human readers.

## When to use

- Before publishing a note, post, or email
- When revising an AI-assisted draft
- When a reader has called the text "AI slop" or "AI-coded"

## How to use

Scan the draft for the patterns below. Delete or rewrite each hit. One tell in isolation is not evidence. A cluster is. Fix the cluster, not the single word.

## Vocabulary tells

Words AI reaches for far more often than humans do. Replace with something specific, or cut.

- delve, leverage, navigate, landscape, tapestry, realm, underscore, showcase, testament
- nuanced, robust, seamless, powerful, comprehensive, holistic, multifaceted, pivotal
- "it's worth noting", "it's important to note", "it's important to remember"
- "at the end of the day", "in today's landscape", "the reality is"
- boosters with no anchor: significantly, substantially, remarkably, notably, considerably

## Punctuation tells

- Em dash overuse. About one per 300 to 500 words is fine. Several per paragraph is the tell. Use a comma, a period, or a parenthesis instead.
- Curly quotes where straight quotes would do
- Bold inside body copy for emphasis
- Emoji in headings or as emphasis
- Decorative unicode (arrows, box-drawing characters)

## Structural tells

- The rule of three. "Fast, scalable, and secure." Three items whether the world offers two or seven. Pick the one that matters.
- "Not X, it is Y" contrast where the negation adds nothing. "This is not about speed, it is about reliability." Say "This is about reliability."
- Announce-then-answer. "This piece will examine..." Start with the first claim.
- Signposting. "more on that below", "as we'll see". Delete.
- Section-end summaries. "As we can see, caching is effective." End on the last real point.
- Uniform paragraph rhythm. Four paragraphs of the same length. Vary on purpose.
- Fluff sandwich. A generality, the content, a restated generality. Keep the middle.
- Paragraph-final restatement. "Ultimately, ..." / "In short, ...". Cut.
- Mechanical transitions. "Furthermore", "Moreover", "Additionally" at the start of every paragraph. Connect naturally or split into separate sentences.

## Rhetorical tells

- Rhetorical questions as section openers. Replace with a statement.
- Passive voice as habit. "It was determined that the leak originated in the cache." Say "We traced the leak to the cache."
- Hedging stacks. "It could perhaps maybe arguably..." Make the claim or drop it.
- Meta-references. "In this article, we'll explore..." The reader knows they are reading the article.
- Faux-conversational pivots. "Here's the thing:", "Let me be clear:", "The truth is:". Cut them. Start with the point.

## Tone tells

- Marketing language. Powerful, seamless, revolutionary, game-changing. These describe anything, so they describe nothing. Use the number instead.
- Paired adjectives with "yet". "Simple yet powerful." Pick one.
- "Excited to announce" / "thrilled to share". State what happened.
- "Whether you're X or Y" false inclusivity. Address the actual reader.
- Corporate cliches. Move the needle, synergy, paradigm shift, growth mindset.
- Internet cliches. Hits different, chef's kiss, rent-free, let that sink in.
- Exclamation clusters. More than one per paragraph reads as performed excitement.

## Model-specific tells

Model families have different defaults. Stack the tells from the family that wrote the draft.

### OpenAI / GPT

- Vocabulary: delve, tapestry, realm, navigate, underscore, testament
- Sets of three inside sentences
- Symmetrical structure: an intro, three to five evenly weighted body sections, a conclusion that restates the intro
- Heading emoji
- "I hope this email finds you well"
- Confident, polished neutrality. Rarely sounds like a specific person
- Em dashes: historically heavy, reduced in current versions

### Claude

- Hedging and meta-commentary: "I should note", "that said", "the nuance is"
- Acknowledgment before answering: "great question", "genuinely tricky area"
- Longer, clause-heavy sentences
- Trade-offs surfaced unprompted: "on one hand / on the other"
- "I'm not certain" more readily than other models
- Em dashes: still overuses. Claude is the only family above human rates in a 2026 Economist comparison
- Mannered prose: metaphor where a plain phrase would do ("a dial worth turning" for "a parameter worth varying")

### Gemini

- Formats first, writes second. Bold lead-ins, nested bullets, tables for simple answers
- Encyclopedic, briefing tone
- Cautious, policy-aware disclaimers ("consult a professional")
- List-first answers where a paragraph would do

### GLM

- Less cataloged in English prose. Documented tells are from fiction generation: code-switching, local vividness overwriting prior state, resolution templates over causality
- Treat as Claude and GPT tells until more is known

## The density principle

A single tell is not evidence. Humans use em dashes, write lists of three, and say "delve" once. The tell is density and co-occurrence. Three "robust" tokens in one paragraph. "It's worth noting" plus an em dash plus "simple yet powerful" in the same paragraph. Flag the cluster, not the word.

Over-correcting makes a new tell. Text stripped to nothing but commas and periods reads as flattened. Keep good tools (em dashes, lists) when they are deliberate choices.

## What is not a tell

- A single em dash, or the word "delve" once
- Correct grammar, curly quotes, polish
- Ordinary transitions (however, so, because)
- One list of three, when the three are genuinely distinct
- Bullets for steps, specs, comparisons
- Formal vocabulary, contractions or none
- Non-native English patterns. A person's English is never a tell

## Editing protocol

1. Read the draft once. Mark every tell.
2. Cluster by paragraph. Two or more tells in one paragraph means rewrite the paragraph.
3. Replace vocabulary tells with something specific: a number, a name, a concrete action.
4. Cut signposts, meta-references, section-end summaries.
5. Collapse rule-of-three lists to the item that matters.
6. Vary sentence and paragraph length. Break uniform rhythm.
7. Take a side. If a paragraph could appear on a competitor's page unchanged, it says nothing distinctive.
8. Re-read once more. Over-correction is its own tell.

## Sources

- Adam Dunkels, "It Isn't The Emdashes" (32-pattern catalog, 2026)
- David S. Kemp, "The AI Tells Reference Sheet" (2026)
- The Economist, "How to spot AI writing" (2026)
- Graphite Five Percent, "AI Tells" (model-family comparison, 2026)
- Molixa, "Which AI Wrote This" (model fingerprints, 2026)
- Dynatrace Content Style Guide, "Remove AI writing patterns"
- Reinhart et al., PNAS 2025, "Do LLMs write like humans?"
```
