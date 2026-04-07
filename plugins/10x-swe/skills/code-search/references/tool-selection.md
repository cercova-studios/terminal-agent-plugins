<objective>
Choose the lightest search tool that still answers the question.
</objective>

<tool_map>
<row>
<task>Know the repo layout</task>
<tool>fff-mcp if available, otherwise rg --files and glob</tool>
</row>
<row>
<task>Search by meaning or intent</task>
<tool>osgrep</tool>
</row>
<row>
<task>Search by structure or syntax</task>
<tool>ast-grep</tool>
</row>
<row>
<task>Search for exact text or identifiers</task>
<tool>ripgrep</tool>
</row>
</tool_map>

<rules>
- Start with repo discovery when the shape of the codebase is unclear.
- Prefer osgrep for conceptual searches once the repo is anchored.
- Use ast-grep when syntax matters more than wording.
- Use ripgrep when the literal text is already known.
- Escalate only when the current tool cannot answer the question well.
</rules>
