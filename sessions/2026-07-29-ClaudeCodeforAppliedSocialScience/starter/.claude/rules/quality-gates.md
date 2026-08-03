# Quality gates

A definition of done, so that "finished" means the same thing every time.

## Levels

| Gate | Applies to | Must hold |
|---|---|---|
| **Draft** | Work in progress | Runs without error. Sample sizes reported. |
| **Shareable** | Going to a co-author | Draft, plus reviewed, commented, outputs regenerated from scratch. |
| **Submission** | Going to a journal | Shareable, plus every number traced to an output file, every citation verified, full pipeline re-run from raw data on a clean checkout. |

Nothing leaves your machine below Shareable.

## Before Shareable

- [ ] Every script runs in order, from raw data, without manual intervention
- [ ] Sample size reported at every transformation
- [ ] No absolute paths, no hardcoded values that should be parameters
- [ ] Comments explain why, not what
- [ ] Outputs deleted and rebuilt successfully
- [ ] Reviewed by a fresh-context reviewer, not the session that wrote it

## Before Submission

- [ ] Every number in the manuscript exists in `scripts/_outputs/`
- [ ] Every citation opened and verified, not just checked for plausible formatting
- [ ] Tables and figures regenerate identically
- [ ] Environment recorded in `docs/environment.txt`
- [ ] Clean clone reproduces everything

## On failing a gate

Say which gate failed and why. Do not report partial success as success. A result that fails Submission but passes Shareable is a useful, honest thing to hand over.
