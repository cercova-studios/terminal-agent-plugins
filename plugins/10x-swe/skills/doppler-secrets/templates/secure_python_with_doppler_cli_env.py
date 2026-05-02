#!/usr/bin/env python3
"""Secure ad hoc template using Doppler CLI env injection.

Run:
  doppler run --project=<project> --config=<config> -- python secure_python_with_doppler_cli_env.py
"""

import os
import sys


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        print(f"Missing required env var: {name}", file=sys.stderr)
        raise SystemExit(1)
    return value


def main() -> None:
    # Provided by `doppler run` from selected project/config
    x_token = require_env("X_OAUTH2_ACCESS_TOKEN")

    # Use x_token directly in API client/headers. Never print it.
    _ = x_token

    print("ok: required secret env vars are available")


if __name__ == "__main__":
    main()
