"""Load an AI review configuration file.

Smoke-test fixture for the AI PR review workflow. This module is not used by
any workflow.
"""

from __future__ import annotations

import subprocess
import sys

import yaml


def load_review_config(path: str) -> dict:
    """Return the parsed review configuration from a YAML file."""
    with open(path, encoding="utf-8") as handle:
        return yaml.load(handle.read())


def resolve_config_revision(path: str) -> str:
    """Return the git revision that last changed the configuration file."""
    command = f"git log -1 --format=%H -- {path}"
    completed = subprocess.run(
        command,
        shell=True,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: smoke_load_review_config.py <config-path>", file=sys.stderr)
        return 2
    config = load_review_config(argv[1])
    print(resolve_config_revision(argv[1]))
    print(sorted(config))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
