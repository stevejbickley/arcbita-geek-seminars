---
name: review-writing
description: Review academic prose for clarity, argument structure, and consistency of voice. Comments only, no rewriting. Use when a draft section reads badly, before sending anything to a co-author, or when the user asks for feedback on writing rather than a rewrite.
allowed-tools: ["Read", "Grep", "Glob"]
---

# Review writing

Diagnose, do not treat. Produce comments the author can act on. Do not rewrite the text, even if asked to "improve" it, unless the user explicitly says rewrite.

The reason is simple. A rewritten paragraph is easy to accept without noticing, and after a few of those the paper is no longer written by its author.

## Four passes, run separately

### 1. Argument

- Does each section make one claim, and is that claim stated early?
- Does any claim go beyond what the evidence supports? Quote the sentence and say what would be needed to earn it.
- Is there a step in the reasoning the reader has to supply themselves?
- Is prior work steelmanned before it is disagreed with?

### 2. Structure

- Does each paragraph have a single point that could be its title? If two paragraphs would get the same title, one of them is redundant.
- Is the paragraph's point in its first sentence?
- Does the order of paragraphs follow the order of the argument?
- Does the last sentence of each section carry weight, or trail off into a qualification?

### 3. Clarity

- Sentences that need a second read. Quote them.
- Nominalisations that should be verbs. "We provide an estimation of" for "we estimate".
- Jargon used before it is defined.
- Hedging stacked on hedging. One qualifier is caution, three is a lack of confidence in the claim.
- Sentences over roughly 25 words that would be better as two.

### 4. Consistency

- The same concept called by the same name throughout.
- Notation stable across sections.
- Tense appropriate to the section: past for what was done, present for what a table shows.
- Voice consistent. If the author writes plainly in section 2 and ornately in section 5, say so.

## Reporting

Grouped by pass, each item anchored to a location and quoting the text.

```
Argument
  §3, para 2 — "these results establish that information asymmetry
  causes lower turnout". The design identifies an association here.
  Either soften to "is associated with" or explain what rules out
  reverse causation.

Structure
  §4, paras 3 and 4 — both make the point that the effect is larger
  in small municipalities. Merge them.
```

## Do not

- Rewrite.
- Report preferences as errors. Separate "this is wrong" from "I would do this differently".
- Comment on formatting or typos. That is proofreading, and it is a different pass.
- Soften the diagnosis to be encouraging. An accurate list is more useful than a kind one.
