---
name: code-search
description: Routes code search requests to semantic, structural, repo-discovery, or text-search workflows. Use when the user wants to find code, inspect repository layout, or search by meaning or syntax.
---

<objective>
Help the assistant choose the right code-search strategy for the task: start with repo discovery when needed, prefer osgrep for semantic search, use ast-grep for structural matching, and fall back to ripgrep for exact text search.
</objective>

<quick_start>
<default_order>
1. If the repo layout is unclear, load `workflows/repo-discovery.md`.
2. If the user wants "find code by meaning", load `workflows/semantic-search.md`.
3. If the user wants a structural pattern, load `workflows/structural-search.md`.
4. If the user wants a literal match, load `workflows/text-search.md`.
</default_order>

<priority>
Default to osgrep for semantic code search. If the repo does not have a usable root index, create or refresh it before searching. Use `fff-mcp --help` to confirm availability; if it is unavailable, fall back to ripgrep-based discovery.
</priority>
</quick_start>

<intake>
What kind of code search do you want?

1. Find code by meaning or concept
2. Find code by structure or AST shape
3. Get the lay of the land in a repo
4. Find exact text or identifier matches

Wait for the answer, then follow the matching workflow.
</intake>

<routing>
| Response | Workflow |
|----------|----------|
| 1, "meaning", "semantic", "concept", "osgrep" | `workflows/semantic-search.md` |
| 2, "structure", "ast", "ast-grep", "pattern" | `workflows/structural-search.md` |
| 3, "layout", "overview", "repo", "land" | `workflows/repo-discovery.md` |
| 4, "text", "literal", "identifier", "grep", "ripgrep" | `workflows/text-search.md` |
</routing>

<reference_index>
<files>
- `references/tool-selection.md` - Tool priorities and fallback rules
- `references/osgrep.md` - Semantic search workflow and index expectations
- `references/ast-grep.md` - Practical ast-grep workflow, rewrites, and CLI usage
- `references/ast-grep-rules.md` - Detailed ast-grep rule syntax and metavariables
- `references/repo-discovery.md` - Layout discovery and repo mapping guidance
</files>
</reference_index>

<workflows_index>
<files>
- `workflows/repo-discovery.md` - Find entry points, project shape, and candidate files
- `workflows/semantic-search.md` - Use osgrep to search by meaning after confirming index state
- `workflows/structural-search.md` - Use ast-grep to search by syntax, structure, and rewrites
- `workflows/text-search.md` - Use ripgrep for exact matches and lightweight fallback searches
</files>
</workflows_index>

<success_criteria>
The right workflow is selected, the search strategy matches the task, and the assistant avoids using a heavier tool when a simpler one is enough.
</success_criteria>
