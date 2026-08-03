# Plan before acting

For anything touching more than one file, or taking more than a few minutes, produce a plan and wait for approval before editing.

## The plan states

1. What changes, and in which files.
2. In what order.
3. How the result will be verified.
4. What could go wrong, and what would signal it.

## When to skip

Single-file edits, typo fixes, and questions. Do not ceremonially plan a one-line change.

## Save plans that matter

A plan for work spanning more than one session goes in `docs/plans/YYYY-MM-DD_short-description.md`, with a status line of DRAFT, APPROVED, or DONE. Plans on disk survive context compression. Plans in the conversation do not.

## After a compression or a new session

Read the most recent plan in `docs/plans/`, then `git log --oneline -10`, then state what you understand the current task to be before doing anything.
