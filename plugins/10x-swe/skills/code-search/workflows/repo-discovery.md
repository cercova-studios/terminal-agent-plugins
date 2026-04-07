<required_reading>
Read these reference files now:
1. `references/tool-selection.md`
2. `references/repo-discovery.md`
</required_reading>

<objective>
Map the repository enough to choose the next search strategy without over-reading the codebase.
</objective>

<process>
<step number="1">
Check whether `fff-mcp` is available by following its help output. If it is available, use it for a repo overview and candidate file discovery.
</step>

<step number="2">
If `fff-mcp` is not available, fall back to `rg --files`, `glob`, and targeted `rg` searches to identify entry points, configs, tests, and likely source directories.
</step>

<step number="3">
Summarize the repo shape, the most likely entry points, and which search workflow should run next.
</step>
</process>

<success_criteria>
- The assistant knows where the repo root, key source files, and configuration live.
- The next search workflow is obvious from the overview.
</success_criteria>
