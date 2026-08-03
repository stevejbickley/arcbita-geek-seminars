#!/usr/bin/env python3
"""Refuse any write to data/raw/.

Registered as a PreToolUse hook on Write and Edit. Claude Code sends the
proposed tool call as JSON on stdin. Exit 2 blocks the call and shows the
message on stderr to Claude, which then has to find another way.

Raw data is the one thing in a project that cannot be regenerated. This is
enforced by the software rather than asked for in a rule, so it cannot be
reasoned around mid-session.
"""

import json
import sys
from pathlib import PurePosixPath

# Folders that must never be written to, relative to the project root.
PROTECTED = ("data/raw",)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0  # Malformed input is not our problem. Do not block.

    path = payload.get("tool_input", {}).get("file_path")
    if not path:
        return 0

    # Normalise separators so Windows and POSIX compare the same way.
    parts = PurePosixPath(str(path).replace("\\", "/")).parts

    for folder in PROTECTED:
        needle = tuple(folder.split("/"))
        for i in range(len(parts) - len(needle) + 1):
            if parts[i:i + len(needle)] == needle:
                print(
                    f"Blocked: {path} is inside {folder}/, which is read-only.\n"
                    f"Raw data is never modified. Write the result to "
                    f"data/clean/ instead, and transform it in a script so the "
                    f"change is reproducible.",
                    file=sys.stderr,
                )
                return 2

    return 0


def self_test() -> int:
    """Run with --self-test to check the path matching still works."""
    import subprocess

    cases = [
        ("data/raw/survey.csv", 2),
        ("./data/raw/x.csv", 2),
        (r"C:\proj\data\raw\a.dta", 2),
        ("other/data/raw/x.csv", 2),
        ("data/clean/analysis.rds", 0),
        ("scripts/raw_helpers.R", 0),
    ]
    failed = 0
    for path, want in cases:
        got = subprocess.run(
            [sys.executable, __file__],
            input=json.dumps({"tool_input": {"file_path": path}}),
            capture_output=True, text=True,
        ).returncode
        ok = got == want
        failed += not ok
        print(f"{'ok  ' if ok else 'FAIL'} {path!r} exit={got} want={want}")
    print("all passed" if not failed else f"{failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(main())
