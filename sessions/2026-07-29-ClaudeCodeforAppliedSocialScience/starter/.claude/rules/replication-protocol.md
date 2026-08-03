# Replication and tolerances

A result that cannot be reproduced from the raw data is not a result.

## Requirements

- One command rebuilds everything from `data/raw/` to `scripts/_outputs/`.
- `set.seed()` (R), `set seed` (Stata), or an explicit seed (Python) is set once per script, in YYYYMMDD form.
- Package versions are recorded. `sessionInfo()` in R, `pip freeze` in Python, `which_version` in Stata, saved to `docs/environment.txt`.
- No absolute paths. Everything relative to the project root.
- No manual steps. If a step cannot be scripted, it is documented in `README.md` with the exact actions.

## Tolerances when comparing two runs

| Quantity | Tolerance |
|---|---|
| Point estimates, standard errors | 1e-6 relative |
| Simulated or bootstrapped quantities | 1e-3 relative, seed fixed |
| Sample sizes and counts | exact, no tolerance |
| Numbers quoted in the paper | must match the output file exactly as printed |

A count that differs by one is a failure, not a rounding difference.

## Cross-language checks

When a result is reproduced in a second language, report the two values side by side with their relative difference. Do not report only that they "agree".

## Before releasing a replication package

- [ ] Fresh clone, run end to end, no errors
- [ ] Every output regenerated from scratch
- [ ] Every number in the manuscript traced to a generated file
- [ ] Environment recorded
- [ ] Raw data included, or its exact provenance documented
