# Every number has one home

No number is typed into the manuscript by hand. Every reported figure, coefficient, standard error, sample size, and table comes from a file written by a script.

## The chain

```
data/raw/            never modified
  -> scripts/0N_*.R  the only thing that transforms data
  -> scripts/_outputs/   tables, figures, and single numbers
  -> paper/            reads those files, never retypes them
```

Anything in `scripts/_outputs/` can be deleted and rebuilt by re-running the scripts. If that is not true, the project is not reproducible.

## In practice

Tables are written to file and pulled in:

```latex
\input{../scripts/_outputs/tab_main.tex}
```

Single numbers quoted in prose get the same treatment, so the sentence and the table cannot disagree:

```latex
The effect is \input{../scripts/_outputs/att_main.tex} percentage points.
```

In R, write the macro alongside the table:

```r
writeLines(sprintf("%.1f", att * 100),
           file.path(out_dir, "att_main.tex"))
```

## Rules

- Never copy a number from the console into a document.
- Never edit a file in `scripts/_outputs/` by hand.
- If a number appears in the paper, it must be greppable in `scripts/_outputs/`.
- Changing the sample means re-running everything, not patching the affected table.

## Word manuscripts

`\input` does not exist in Word, so this cannot be enforced. The fallback: every script appends its reported numbers to `scripts/_outputs/reported_numbers.md`, with a label. Before any submission, check the manuscript against that file line by line. Manual, and still better than having no authoritative list.
