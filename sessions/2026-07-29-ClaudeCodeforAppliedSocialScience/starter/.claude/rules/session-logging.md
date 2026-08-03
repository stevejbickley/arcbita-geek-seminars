# Session logging

Context gets compressed and conversations get lost. Files do not.

## Three moments

**After a plan is approved.** Write the goal, the approach, and why that approach, to `docs/session_logs/YYYY-MM-DD_description.md`.

**During work.** Append one or two lines whenever a decision is made, a problem is solved, or the approach changes. Do not batch this to the end. The reason a choice was made is the thing that gets forgotten first.

**At the end.** Summary of what was done, what is unresolved, and what the next session should start with. Update `TASKS.md`, `MEMORY.md`, and `CHANGELOG.md` to match.

## What belongs where

| File | Holds |
|---|---|
| `docs/session_logs/` | What happened on a given day, and why |
| `MEMORY.md` | Learnings that stay true across sessions |
| `CHANGELOG.md` | Dated record of what changed in the project |
| `TASKS.md` | What is next |

`MEMORY.md` is for things that were hard to work out and would be annoying to work out twice. Coding quirks in a data wave. A package version that breaks something. The reason a variable is constructed the way it is. Not a diary.

## Format

Session log:

```markdown
# 2026-07-28 — Merge diagnostics

**Goal:** Work out why the municipality merge loses 198 rows.

**Found:** 2015 wave pads identifiers to 4 digits, earlier waves do not.

**Decision:** Normalise in 02_clean.R rather than at the merge, so
every downstream user gets the fixed version.

**Next:** Re-run 03 onwards and check the sample is 12,400 again.
```

Short is fine. Written down is the point.
