# Starter kit

Everything a research project needs on day one, plus the skills and agents the
guide recommends.

## The easy way

Do not copy this by hand. Open Claude Code in the folder you want to set up and
paste the bootstrap prompt from the appendix of the guide. It fetches these
files, builds the folder structure, writes your `CLAUDE.md`, installs the skills
at user level, and initialises git. About a minute, and it works on an empty
folder or on one with years of work in it.

## What is here

```
CLAUDE.md              standing instructions, read every session
MEMORY.md              things learned that should survive
CHANGELOG.md           dated record of what changed
TASKS.md               what is next
.gitignore             keeps data out of git
SOURCES.md             who these ideas and files came from

.claude/
  settings.json        permissions and the raw-data hook
  hooks/               protect-raw-data.py, refuses writes to data/raw/
  rules/               13 files
  skills/              15 folders
  agents/               9 files
  references/          journal-profiles.md
```

**Rules (13).** Ten cover the workflow: `plan-first-workflow`,
`verification-protocol`, `quality-gates`, `session-logging`,
`replication-protocol`, `cross-artifact-review`, `proofreading-protocol`,
`inference-robustness`, `post-flight-verification`, `single-source-of-truth`.
Three are coding conventions, for R, Stata, and Python. Delete the two languages
you do not use.

**Skills (15).** `data-analysis`, `review-r`, `code-review`, `proofread`,
`end-session`, `handoff`, `review-paper`, `review-writing`,
`respond-to-referees`, `devils-advocate`, `grill-me`, `validate-bib`,
`humanize`, `coauthor-brief`, `stata-replication`.

**Agents (9).** Not installed deliberately. The skills call them, so they travel
together: `claim-verifier`, `domain-referee`, `editor`, `humanize-auditor`,
`methods-referee`, `proofreader`, `r-reviewer`, `review-writing`, `verifier`.

**References (1).** `journal-profiles.md`, the calibration data `review-paper
--peer` uses. It covers five economics journals. Extend it for your own field.

## Two skills the guide covers that are not here

`beautiful_deck` is in [MixtapeTools](https://github.com/scunning1975/MixtapeTools),
which has no licence file, so nothing from it is redistributed. Copy it yourself.

`honest-thinking-partner` ships with Claude rather than coming from a public
repository. There is no file to copy and you already have it.

## Where things go

The four Markdown files, `.gitignore`, and `.claude/rules/`, `.claude/hooks/`,
`.claude/settings.json` belong in **the project**.

`.claude/skills/`, `.claude/agents/`, and `.claude/references/` belong in **your
user folder**, `~/.claude/` on Mac or `C:\Users\<you>\.claude\` on Windows, so
they load in every project rather than just this one.

On Windows, `.claude` is hidden in File Explorer. Turn on **View > Show > Hidden
items** or you will think the copy failed.

## Read them, then change them

Thirteen rules is already a lot to load into every session. Delete the ones you
disagree with. A rule you do not believe in is worse than no rule, because you
will start ignoring the output that enforces it.

The skills are other people's judgement, written down. They are a starting point,
not scripture. Attribution and licences are in `SOURCES.md`.

## One caveat on the bundled skills

They are copied close to verbatim from upstream, so a few contain cross-references
to skills that are not bundled here (`/slide-excellence`, `/audit-reproducibility`,
`/qa-quarto`). Those pointers will not resolve. They appear in "see also" notes
rather than in the working steps, so the skills still run correctly.
