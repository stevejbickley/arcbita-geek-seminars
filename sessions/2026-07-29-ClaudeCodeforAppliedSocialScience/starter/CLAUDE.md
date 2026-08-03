# [PROJECT NAME]

<!-- Read at the start of every session. Keep it under 100 lines.
     Everything here costs context on every single request, so vague
     instructions are worse than no instructions. Delete what does not
     apply to you. -->

## What this is

[Two or three sentences. The research question, the data, the method.
Write it so a co-author who has been away for six months is caught up.]

## Language and tools

- Analysis in [R / Stata / Python]
- Manuscript in [LaTeX / Quarto / Word]
- Conventions are in `.claude/rules/`. Follow them.

## Layout

```
data/raw/          never written to, never edited
data/clean/        produced by scripts, safe to delete and rebuild
scripts/           numbered, run in order
scripts/_outputs/  tables, figures, saved results
paper/             the manuscript
docs/              notes, logs, correspondence
```

## Standing rules

1. **Plan first.** Anything touching more than one file gets a plan I approve before you start.
2. **`data/raw/` is read-only.** A hook enforces this. Do not try to route around it.
3. **Report sample sizes.** Rows in and rows out at every merge, filter, and reshape. Unmatched records on both sides of every join.
4. **Nothing is done until it has run.** Do not describe output you have not seen. If you could not run something, say so.
5. **No number reaches the paper by hand.** Every reported figure comes from a file in `scripts/_outputs/`.
6. **Citations are verified, never remembered.** Do not produce a reference you have not confirmed exists.

## Things specific to this project

<!-- The quirks that took you an afternoon to work out. Add as you go. -->

- [e.g. The 2015 wave pads municipality IDs to four digits. Normalised in 02_clean.R.]
- [e.g. Standard errors cluster at the canton level, not the municipality level.]

## Never

- Commit without being asked.
- Install packages without saying so first.
- Edit anything in `scripts/_outputs/` by hand.
- Rewrite my prose when I asked for comments.
