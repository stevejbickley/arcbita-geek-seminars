---
name: end-session
description: Close out a working session. Writes a session log and brings TASKS.md, MEMORY.md, CHANGELOG.md and README.md up to date. Use whenever the user says they are stopping, wrapping up, done for the day, or asks to close the session.
allowed-tools: ["Read", "Grep", "Glob", "Edit", "Write", "Bash"]
---

# End session

Summarise what happened and write it down, so the next session does not start from nothing. Work through this without asking for approval at each step. Present one summary at the end.

## 1. Work out what actually happened

Do not rely on memory of the conversation. Check.

```bash
git log --oneline -20
git status
git diff --stat
```

Read anything that changed. The goal is a factual account, not an optimistic one.

## 2. Write the session log

To `docs/session_logs/YYYY-MM-DD_short-description.md`. Create the folder if needed. If a log already exists for today, append rather than overwrite.

```markdown
# YYYY-MM-DD — [what this session was about]

**Goal:** one sentence.

**Done:**
- concrete outcomes, with file names

**Decisions:** what was chosen, and why. This is the part that gets
forgotten and the part that matters most.

**Problems:** what broke, what was worked around, what is still broken.

**Unverified:** anything produced but not checked. Say so plainly.

**Next:** what the next session should start with.
```

## 3. Update the project files

**`TASKS.md`** — tick off what was finished, add what came up, and put the immediate next step at the top.

**`MEMORY.md`** — add anything learned that will still be true next month. A data quirk, a package version that breaks something, the reason a variable is built the way it is. Not a diary and not a summary of this session. Only things that would be annoying to work out twice.

**`CHANGELOG.md`** — a dated entry, newest first, saying what changed in the project. One or two lines.

**`README.md`** — only if the project's description or structure is now wrong.

## 4. Report

Six lines at most:

- What was accomplished
- What is unverified or unfinished
- Files updated
- The single most useful thing to do next

## Rules

- Never record something as done that was not verified. If a script was written but never run, the log says so.
- Do not commit anything. That is a separate decision.
- Keep `MEMORY.md` short. If it passes about a hundred lines, prune it rather than appending.
