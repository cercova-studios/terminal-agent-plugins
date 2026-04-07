<required_reading>
Read these reference files now:
1. `references/tool-selection.md`
2. `references/osgrep.md`
3. `references/repo-discovery.md`
</required_reading>

<objective>
Search by concept, behavior, or intent using osgrep after the repository layout is understood.
</objective>

<process>
<step number="1">
Confirm whether a usable osgrep index exists at the repo root. If not, create or refresh the index before searching.
</step>

<step number="2">
Use repo-discovery output to anchor the search with file paths, symbols, or subsystem names when possible.
</step>

<step number="3">
Run osgrep with a semantic query that describes the behavior, not just the literal identifier.
</step>

<step number="4">
If results are too broad, add concrete anchors such as filenames, symbols, or subsystem names. If results are too narrow, widen the query and remove unnecessary constraints.
</step>

<step number="5">
If semantic search is not sufficient, fall back to ast-grep for structure or ripgrep for exact text.
</step>
</process>

<success_criteria>
- The search uses osgrep as the default semantic tool.
- A missing root index is handled before the search proceeds.
- The result set is usable for follow-up investigation.
</success_criteria>
