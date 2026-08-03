# Verification

A claim that something works is not evidence that it works. Nothing is reported as done until it has been observed to run.

## Never report as complete

- Code that has not been executed in this session.
- A number that was not read from actual output.
- A file that has not been confirmed to exist and be non-empty.
- A fix that has not been re-run after the fix.

## Always report

- The exact command that was run.
- The relevant lines of output, not a summary of them.
- The row count of any dataset that was created or modified.

## Sample size discipline

After every filter, join, merge, reshape, or subset:

- Rows in, rows out.
- Unmatched records on each side of a join.
- If more than 2% of either side is unmatched, stop and say so before continuing.

Silent sample loss is the most common serious error in applied work, and it does not announce itself.

## Uncertainty

If something cannot be verified, say so plainly. "I could not run this because Stata is not reachable from the shell" is a useful sentence. Producing plausible output instead is not.

## Before saying a task is finished

- [ ] Every script ran, in order, without error
- [ ] Sample sizes reported and sensible
- [ ] Outputs exist on disk and were opened
- [ ] Nothing was reported that was not observed
