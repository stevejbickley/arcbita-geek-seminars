---
paths:
  - "**/*.R"
  - "**/*.Rmd"
  - "**/*.qmd"
---

# R conventions

## Every script starts the same way

```r
# 02_clean.R — harmonise waves and build the analysis sample
# Reads:  data/raw/survey_*.csv
# Writes: data/clean/analysis.rds

library(tidyverse)
library(fixest)

set.seed(20260728)          # once, at the top, YYYYMMDD

in_dir  <- file.path("data", "raw")
out_dir <- file.path("data", "clean")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
```

- `library()`, never `require()`. A missing package should stop the script.
- Paths relative to the project root, built with `file.path()`.
- The header comment says what the script reads and writes. This is what makes the pipeline readable without running it.

## Sample size discipline

Every merge, filter, and reshape reports what it did.

```r
n_before <- nrow(df)
df <- df |> filter(!is.na(income))
message(sprintf("Dropped %d rows with missing income (%d -> %d)",
                n_before - nrow(df), n_before, nrow(df)))
```

For joins, report unmatched records on both sides. `dplyr::anti_join()` is the quick way to see them.

## Numerical care

- Never `==` on doubles. Use `all.equal()` or `abs(a - b) < tol`.
- Clamp probabilities before passing them to `qnorm()`: `p <- pmin(1 - 1e-12, pmax(1e-12, p))`.
- Integer literals for counts: `n <- 1000L`.
- Pre-allocate before loops: `out <- numeric(n)`. Never grow with `c()`.
- Explicit `na.rm =`. Never rely on the default.
- Write `TRUE` and `FALSE`, never `T` and `F`. They are variables and can be reassigned.

## Style

- `snake_case` throughout. Functions are verbs.
- Lines under 100 characters, except formulas where breaking would hurt readability. Comment those.
- Comments say why, not what.
- Functions that do real work get a Roxygen header.

## Outputs

Everything a script produces goes to `scripts/_outputs/`, and nothing else writes there.

```r
saveRDS(results, file.path(out_dir, "results_main.rds"))
ggsave(file.path(out_dir, "fig_trend.pdf"), p, width = 7, height = 4.5)
```

Save the estimated object, not only the formatted table. A future session should be able to reformat without re-estimating.

## Checklist

```
[ ] Header comment names inputs and outputs
[ ] library() at top, set.seed() once
[ ] All paths relative
[ ] Row counts reported at every transformation
[ ] No float equality, no T/F, explicit na.rm
[ ] Every result object saved to _outputs/
```
