# Inference

Getting the point estimate right is the easy half. These are the choices that are usually made silently and are usually wrong.

## State the choices, every time

For any reported estimate, the output must make clear:

- What the unit of observation is.
- What variation identifies the parameter.
- How standard errors are computed, and at what level clustering is applied.
- Whether weights are used, and which.
- What the sample restriction is, and how many observations each restriction removes.

If any of these is not stated, the result is not finished.

## Clustering

- Cluster at the level of treatment assignment, not the level of the observation.
- With few clusters (below roughly 40), the asymptotic standard errors are too small. Use wild cluster bootstrap and say so.
- Two-way clustering needs a reason. State it.
- Never cluster at the individual level in a panel and call it robust.

## Fixed effects

- Name what each set of fixed effects absorbs.
- Check that the variation of interest survives. A regressor that is nearly collinear with the fixed effects will produce a large, unstable, meaningless coefficient.
- Report the within R-squared and the number of absorbed groups.

## Generated regressors

If a right-hand-side variable is itself an estimate, the standard errors are wrong unless corrected. Bootstrap the whole procedure or say plainly that inference is conditional.

## Multiple hypotheses

If more than a handful of outcomes or subgroups are tested, report an adjustment or state that none was applied. Do not present the surviving coefficient as if it were the only one tried.

## Difference-in-differences

- With staggered adoption, the two-way fixed effects estimator is biased under heterogeneous effects. Use an estimator that handles this and name it.
- Show the event-study plot with pre-periods. Parallel trends is an assumption, and readers want to see the pre-trends.
- Report the number of treated and control units, and when treatment starts.

## Regression discontinuity

- Report the bandwidth, how it was chosen, and results at other bandwidths.
- Report the density test at the cutoff.
- Show the raw binned scatter, not only the fitted lines.

## The honest sentence

When a specification choice materially changes the result, say so in the text. A robustness table that quietly contains the failure is worse than not running it.
