<objective>
Find the shape of the repository quickly enough to choose the next search tool.
</objective>

<discovery_steps>
- Look for the repo root, source directories, configs, tests, and package manifests.
- Prefer the lowest-cost overview that reveals likely entry points.
- Use `fff-mcp` when it exists; otherwise use `rg --files`, `glob`, and targeted `rg` searches.
</discovery_steps>

<signals>
- A small set of top-level entry files usually identifies the main application path.
- Config files often reveal framework, language, and test conventions.
- Test files and fixture names often reveal the strongest identifiers for follow-up searches.
</signals>
