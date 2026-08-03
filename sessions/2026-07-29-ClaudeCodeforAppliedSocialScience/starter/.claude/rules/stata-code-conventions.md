---
paths:
  - "**/*.do"
  - "**/*.ado"
---

# Stata conventions

## Read this first

Claude usually cannot run Stata and read its own output. That breaks the loop that makes this tool useful, so Stata code needs more human checking than R or Python code, not less.

Two consequences. Write do-files that log everything, so the log can be pasted back. And never accept a Stata result that nobody has watched execute.

## Every do-file starts the same way

```stata
* 02_clean.do — harmonise waves and build the analysis sample
* Reads:  data/raw/survey_*.dta
* Writes: data/clean/analysis.dta

version 18
clear all
set more off
set seed 20260728

local in  "data/raw"
local out "data/clean"
cap mkdir "`out'"

log using "docs/logs/02_clean.log", replace text
```

- `version` at the top so the file still runs in five years.
- Paths relative, in locals. Never a `cd` to an absolute path.
- Always log. The log is how anyone verifies what happened.
- Close the log at the end with `log close`.

## Sample size discipline

Stata makes silent sample loss very easy. Counter it explicitly.

```stata
count
local n_before = r(N)

merge 1:1 municipality year using "`in'/turnout.dta"
tab _merge
assert _merge == 3 | _merge == 1
keep if _merge == 3
drop _merge

count
di "Merged: `n_before' -> " r(N)
```

Never use `merge` without inspecting `_merge`. Never `keep if _merge==3` without first tabulating it.

## Assertions instead of trust

```stata
assert !missing(id)
isid municipality year
assert inrange(share_yes, 0, 1)
```

`isid` after every reshape and merge. An assertion that fails stops the script, which is what you want.

## Style

- `snake_case` for variables and locals.
- One command per line. Use `///` for continuation.
- Label every variable and value you create.
- Comment why, not what.
- Prefer `frames` or explicit `tempfile` over overwriting the data in memory.

## Outputs

```stata
esttab est1 est2 using "scripts/_outputs/tab_main.tex", replace ///
    booktabs se star(* 0.10 ** 0.05 *** 0.01)

file open f using "scripts/_outputs/att_main.tex", write replace
file write f %4.1f (100 * _b[treat])
file close f
```

Write single numbers to their own file so the manuscript can `\input` them. See `single-source-of-truth.md`.

## Checklist

```
[ ] version, clear all, set seed at top
[ ] log using ... , and log close at the end
[ ] All paths relative, in locals
[ ] _merge tabulated and asserted after every merge
[ ] isid after every merge and reshape
[ ] Variables and values labelled
[ ] Results written to scripts/_outputs/
[ ] A human has read the log
```
