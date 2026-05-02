---
name: doppler-secrets
description: Enforces secure Doppler secret usage patterns for ad hoc scripting and API calls. Use when a task needs secrets and must avoid exposing them in logs, prompts, command history, or tool output.
---

<objective>
Provide a strict, reusable workflow for handling secrets safely with the Doppler CLI.
</objective>

<essential_rules>
1) Use Doppler CLI, not Doppler MCP.
- This workflow assumes Doppler MCP is not used for secret access.
- Use `doppler` CLI for name validation and runtime env injection.

2) Never expose secrets.
- Never print secrets to stdout/stderr.
- Never include secret values in LLM/tool message bodies.
- Never serialize secrets into files, prompts, stack traces, shell history, or debug dumps.

3) Prefer env injection over direct value retrieval.
- Primary pattern: `doppler run --project=<p> --config=<c> -- <command>`
- Application reads required env vars internally.
- Do not echo secret-bearing env vars.
</essential_rules>

<quick_start>
1. Confirm `doppler` CLI is installed and authenticated.
2. Validate required secret names (names only, no values).
3. Execute target script through `doppler run` for env injection.
4. Keep all outputs sanitized.
</quick_start>

<workflow>
<step_1_preflight>
Check CLI availability and auth:
```bash
command -v doppler >/dev/null || { echo "doppler CLI missing" >&2; exit 1; }
doppler configs >/dev/null 2>&1 || { echo "doppler auth/config missing" >&2; exit 1; }
```
</step_1_preflight>

<step_2_validate_required_names>
Validate secret names only (safe):
```bash
doppler secrets --project=<project> --config=<config> --only-names --json
```

Compare required names against this list. Do not retrieve secret values during validation.
</step_2_validate_required_names>

<step_3_execute_with_env_injection>
Preferred execution pattern:
```bash
doppler run --project=<project> --config=<config> -- python /path/to/script.py
```

Alternative for shell commands:
```bash
doppler run --project=<project> --config=<config> --command "python /path/to/script.py"
```
</step_3_execute_with_env_injection>

<step_4_safe_python_pattern>
Use env variables inside Python, never print them:

```python
import os
import sys

required = ["X_OAUTH2_ACCESS_TOKEN"]
missing = [k for k in required if not os.getenv(k)]
if missing:
    print(f"Missing required secret env vars: {', '.join(missing)}", file=sys.stderr)
    raise SystemExit(1)

x_token = os.environ["X_OAUTH2_ACCESS_TOKEN"]
# Use x_token directly in client headers; never print it.
```
</step_4_safe_python_pattern>

<step_5_output_sanitization>
Allowed outputs:
- counts, ids, timestamps
- usernames or non-sensitive identifiers
- summarized findings

Forbidden outputs:
- token strings
- secret values or env dumps
- auth headers / full credentialed request dumps
</step_5_output_sanitization>
</workflow>

<common_failures_and_fixes>
- Failure: `doppler: command not found`.
  - Fix: install Doppler CLI via official Doppler docs, then retry.

- Failure: auth/config not initialized.
  - Fix: run `doppler login` and/or configure project+config before execution.

- Failure: script logs secrets while debugging.
  - Fix: remove debug prints; redact exceptions; avoid dumping env/headers.

- Failure: secrets missing at runtime.
  - Fix: verify names exist in selected project/config and rerun with correct `doppler run --project --config`.
</common_failures_and_fixes>

<verification_checklist>
- [ ] Doppler CLI present and authenticated
- [ ] Secret names validated without reading values
- [ ] Script executed through `doppler run`
- [ ] No secret output in logs/messages/files
- [ ] Final response sanitized
</verification_checklist>

<success_criteria>
Agents complete secret-backed ad hoc tasks quickly using Doppler CLI env injection while preserving strict non-disclosure guarantees.
</success_criteria>
