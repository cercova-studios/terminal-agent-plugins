<objective>
Use osgrep for semantic code search once the repository has a usable index.
</objective>

<index_rules>
- Prefer an index at the root of the git repository.
- If the root index is missing, create or refresh it before searching.
- Confirm the exact index command with `osgrep --help` when needed.
</index_rules>

<search_rules>
- Phrase the query as the behavior or concept you want, not just the symbol name.
- Add file paths, subsystem names, or identifiers when the first pass is too broad.
- Remove constraints when the first pass is too narrow.
- Use the returned hits as anchors for a follow-up structural or text search.
</search_rules>

<fallbacks>
- If osgrep is unavailable or unsuitable, use ast-grep for structure or ripgrep for exact text.
- If the repo layout is unclear, run repo discovery first.
</fallbacks>
