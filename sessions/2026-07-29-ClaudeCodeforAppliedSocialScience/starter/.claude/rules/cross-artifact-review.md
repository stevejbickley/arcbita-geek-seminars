# Reviewing the paper means reviewing the code

A claim in a manuscript depends on the script that produced it. Reviewing the text without touching the code checks half the artifact.

## The dependency chain

```
paper/main.tex     cites   Table 2
Table 2            from    scripts/_outputs/tab_main.tex
tab_main.tex       by      scripts/04_analyse.R
04_analyse.R       uses    data/clean/analysis.rds
analysis.rds       by      scripts/02_clean.R
02_clean.R         reads   data/raw/survey.csv
```

A bug in `02_clean.R` invalidates Table 2. Reading `main.tex` alone will never find it.

## When this applies

When a manuscript contains numeric claims and the project has an analysis directory. A theory paper with no code does not trigger this.

Signals: `\input{}` pointing at script outputs, table labels matching filenames in `scripts/_outputs/`, or any coefficient, sample size, or p-value quoted in the text.

## The procedure

1. **Trace.** For each numeric claim in the manuscript, identify the output file it comes from and the script that wrote it.
2. **Review the code.** Run a read-only review over each script in the chain, with fresh context.
3. **Check the numbers.** Compare each claim against the actual output file, at the tolerances in `replication-protocol.md`.
4. **Report in three groups.**

```markdown
## Claims that do not match their source
| Claim in paper | Output file | Value in file |
|---|---|---|

## Code problems that affect paper claims
## Code problems that do not affect the paper
```

## Escalation

A claim that does not match its source is a blocking problem, regardless of how minor the difference looks. A code problem that does not touch any paper claim goes in `TASKS.md` and does not block.
