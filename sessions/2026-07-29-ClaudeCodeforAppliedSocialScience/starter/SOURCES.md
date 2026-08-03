# Where this came from

Almost nothing here is original. The structure and most of the substance come
from people who published their setups. Files copied from their work are listed
below with the licence that permits it.

## Pedro H. C. Sant'Anna

[claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow), MIT.
[The guide](https://psantanna.com/claude-code-my-workflow/workflow-guide.html).

**Copied close to verbatim** into `.claude/skills/`: `proofread`, `review-r`,
`review-paper`, `respond-to-referees`, `devils-advocate`, `validate-bib`,
`humanize`, `data-analysis`, `coauthor-brief`, `stata-replication`.

**Copied into `.claude/agents/`**, because the skills above call them:
`claim-verifier`, `domain-referee`, `editor`, `humanize-auditor`,
`methods-referee`, `proofreader`, `r-reviewer`, `verifier`.

**Copied into `.claude/references/`**: `journal-profiles.md`, the calibration
data behind `review-paper --peer`.

**Adapted, not copied**, in `.claude/rules/`: the two-tier rules idea, the
plan-first workflow, quality gates, session logging, the cross-artifact
protocol, replication tolerances, and post-flight verification. Those files are
shorter rewrites aimed at applied social science rather than an econometrics
course, so the wording is mine and the thinking is his.

His repository holds far more than this. Clone it and read it.

## Matt Pocock

[mattpocock/skills](https://github.com/mattpocock/skills), MIT.

**Copied verbatim** into `.claude/skills/`: `grill-me`, `handoff`,
`code-review`. Written for software engineering and they transfer to research
work unchanged.

They are also installable as a plugin, which keeps them updated:

```
/plugin marketplace add mattpocock/skills
/plugin install mattpocock-skills@mattpocock
```

## Paul Goldsmith-Pinkham

[Claude Code for applied economists](https://markusacademy.substack.com/p/claude-code-for-applied-economists) and the [series on his Substack](https://paulgp.substack.com/).

No files taken. The guide's framing of verification as the bottleneck, the
argument for reviewing by git diff, the four-step method for building a personal
writing style file, the "comments not rewrites" instruction, the permissions
advice, and the Parquet-and-DuckDB approach to large data all come from him.

## Scott Cunningham

[MixtapeTools](https://github.com/scunning1975/MixtapeTools).

Referee 2, Blindspot, Bibcheck, Beautiful Deck. **The repository has no licence
file, so nothing from it is bundled here.** Copy it yourself from source.

## Anthropic

[Claude Code documentation](https://code.claude.com/docs/en/overview) and the
[skills repository](https://github.com/anthropics/skills).

`honest-thinking-partner`, which the guide recommends, is **not** in that
repository. It ships with Claude, so there is no file to redistribute.

## Mine

`end-session` and `review-writing` in `.claude/skills/`, the
`review-writing` agent, `.claude/hooks/protect-raw-data.py`, the four project
templates, and the wording of every file in `.claude/rules/`.

## A note on the copies

The bundled skills are close to their upstream versions, which means a few
contain cross-references to skills not included here (`/slide-excellence`,
`/audit-reproducibility`, `/qa-quarto`). Those pointers will not resolve. They
sit in "see also" notes rather than working steps, so the skills still run.
Editing them to match this smaller set would fork them from upstream and make
future updates painful, so they are left as they are.

Take any of it, change it, and do not feel obliged to keep a rule or a skill you
disagree with. These files are meant to be edited.
