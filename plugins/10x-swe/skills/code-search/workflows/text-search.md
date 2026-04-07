<required_reading>
Read this reference file now:
1. `references/tool-selection.md`
</required_reading>

<objective>
Use ripgrep for exact text, literal identifiers, and lightweight fallback searches.
</objective>

<process>
<step number="1">
Choose focused patterns and constrain the search with file globs whenever possible.
</step>

<step number="2">
Use surrounding context only as needed to confirm the match.
</step>

<step number="3">
If the result set is noisy, tighten the pattern or switch to ast-grep for structure or osgrep for meaning.
</step>
</process>

<success_criteria>
- The search is fast and specific.
- Exact matches are found without unnecessary tooling overhead.
- The assistant knows when to escalate to a deeper workflow.
</success_criteria>
