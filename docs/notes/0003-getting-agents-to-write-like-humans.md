
I frequently found that my agents wrote like agents. Instructing them to write better changed nothing. Banning the words that mark machine prose made it worse: the agent stripped the banned words and kept the padding. What worked was a revision skill: write the draft, read the finished text back as input, cut it against a list of specific mistakes. Details below.

## How to write well

Writing well is two things: capture the reader's interest, and get to the point. Ideally you do nothing else.

Agents fail at both. The first cause is the corpus: they learn prose from the web, where a cooking blog buries the recipe under nine paragraphs about the blogger's childhood and a home-decor post spends three hundred words on its "design journey" before showing a single room. This corpus is the agent's sense of normal prose. The padding transfers.

The second cause is worse: instruction cannot fix it. An agent generates and perceives one token at a time. It cannot step back and see the whole draft, so it never notices a paragraph taking twice the words its point needs. Telling it to be concise fails: it already believes it is concise, because from inside, every next token looks reasonable.

The fix follows from the cause. If the agent cannot perceive the whole draft while writing, revision must be a separate step that takes the finished text back as input. Read back, the draft is whole, all at once. Padding invisible during writing is visible during reading.

The first version of this note was written by an agent that had been told all of this in advance. It restated the rule against the rule of three as a rule of three. Told to stop, it produced a stack of four short sentences. Asked to be plain, it offered a euphemism, "land". Instruction never reached the habit. Reading the draft back did.

## The skill

The skill names the two jobs and the mistakes that break them, concretely enough to search for. It audits the finished draft, never the drafting.

The full skill is below. Paste it into `~/.config/opencode/skills/write-human/SKILL.md` to install, then load it with `skill("write-human")` when revising.

```
---
name: write-human
description: Use when writing or revising prose for human readers: notes, posts, documentation, email. States the two jobs of writing, names the failure modes agents fall into by default, and audits the finished draft against them. Run on every draft before publishing.
---

# Write Human

Writing well is two things: capture the reader's interest, and get to the point. Ideally you do nothing else. Everything below follows from that.

Agents fail at both. They learn prose from a corpus that winds on: cooking blogs, home-decor posts, SEO filler. And they generate one token at a time, which means they cannot perceive their own verbosity. From inside the generation, every next token looks reasonable. You will not catch this in your own draft while writing. The audit happens after, on the finished text, read back as input: whole, all at once, as a stranger deciding whether to keep reading.

## The rules

1. **Get to the point.** The first sentence gives the reader the finding or the use of the piece. If nothing is lost by skipping the first paragraph, the first paragraph is in the way.
2. **Be insightful.** One specific, true observation beats balanced coverage. The reader trades time for something they did not already have.
3. **Be blunt.** State the claim. If it might be wrong, verify it or drop it. Never wrap it in hedges.
4. **Use fewer words.** Revise to fewer words rather than more. Every word must do work.

## Failure modes to audit for

Grouped by the rule they break. Mark every hit, then fix by rule.

**Against "get to the point."**

- The draft announces itself: "This piece will examine...", "In this article, we'll explore..." Start with the first claim.
- A generic opening that could begin any piece on the subject. Open with the specific fact instead.
- Sections end by restating themselves. End on the last real point.
- Signposts: "more on that below", "as we'll see". Delete.
- A conclusion that restates the introduction. Cut the weaker one.

**Against "be insightful."**

- Balanced coverage where one observation would do. Pick the observation.
- Claims that sound profound and name nothing specific. Replace with the number, the example, or the name.
- Adjective inflation: robust, seamless, comprehensive, powerful, holistic. These describe anything, so they describe nothing.
- Vocabulary the model reaches for far more often than people do: delve, leverage, navigate, landscape, tapestry, showcase, testament. Use the plain word.

**Against "be blunt."**

- Hedges: "perhaps", "arguably", "it could be that". Make the claim or drop it.
- Postponing signposts: "it's worth noting that", "it's important to remember". Delete. The sentence underneath already carries the point.
- Passive voice that hides the actor: "it was determined that". Name who did it.
- Faux-conversational pivots: "Here's the thing:", "Let me be clear:". Start with the point.
- Rhetorical questions where a statement belongs.
- "Excited to announce", "thrilled to share". State what happened.
- Caveat sections. State the finding. Readers who want to replicate will check the sample size themselves.

**Against "use fewer words."**

- Triples that exist for the rhythm. Keep three items when they are genuinely distinct; otherwise cut to the one that carries the point.
- Paired adjectives: "simple yet powerful", "elegant and robust". Pick the one that matters.
- The thesis restated in every section. Make the point once, in its strongest place.
- "very", "really", "actually", "quite". Cut.
- Paragraph-final restatement: "Ultimately...", "In short...". Cut.

**Against "capture the reader's interest": rhythm and format.** Read the draft aloud.

- Stacks of short punchy sentences read as performed. Break the stack.
- Uniform paragraph lengths read as machine output. Vary deliberately.
- Three or more sentences opening with the same word. Keep one, recast the rest.
- Em dashes used as the default route to a punchline, several per paragraph. A period usually does the job.
- Emoji in headings, decorative unicode, bold inside body copy, exclamation clusters. Cut.

## Model defaults

Families reach for different crutches. Audit your own family's list hardest, because you reach for it without noticing.

- **GPT:** sets of three, symmetrical structure (intro, evenly weighted sections, a conclusion that restates the intro), heading emoji, "I hope this email finds you well".
- **Claude:** hedging and meta-commentary ("I should note", "that said"), clause-heavy sentences, warmth before substance, em dashes.
- **Gemini:** bullets and bold where prose belongs, encyclopedic tone, cautious disclaimers.
- **GLM:** less cataloged in English prose. Assume the GPT and Claude lists until better known.

## What not to fix

- A single em dash, a single "delve", one list of three genuine items. The tell is density, not occurrence.
- Correct grammar and polish. They are not tells.
- A step list or spec that happens to be a list. That content is a list.
- Non-native English. A person's English is never a tell.

## Protocol

1. Draft without this skill open. Drafting against a checklist produces stiff prose.
2. Put the draft down. Come back and read it as a stranger deciding whether to keep reading.
3. Mark every failure mode above. Two or more in one paragraph means rewrite the paragraph.
4. Check the first sentence first: finding or use, not preamble.
5. Delete hedges, signposts, caveats, and restatements.
6. Collapse padded triples to the item that carries the point.
7. Read the rhythm aloud. Break uniform stacks in both directions.
8. Cut ten percent of the words. If the piece survives, cut ten percent more.
9. Before publishing, answer the reader's questions: Did you get to the point? Did you give the reader a reason to care? Does the detail that follows stay relevant to an interested reader?
```
