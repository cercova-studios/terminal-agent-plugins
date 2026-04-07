<required_reading>
Read these reference files now:
1. `references/tool-selection.md`
2. `references/ast-grep.md`
3. `references/ast-grep-rules.md`
</required_reading>

<objective>
Find code by syntax and structure with ast-grep when text search is too blunt.
</objective>

<process>
<step number="1">
Clarify the language, the code shape, and what should be included or excluded from matches.
</step>

<step number="2">
Translate the request into a small example snippet, then express that shape as an ast-grep rule.
</step>

<step number="3">
Start with the simplest possible rule. Add `has`, `inside`, `all`, `any`, or `not` only when needed.
</step>

<step number="4">
Test the rule on a minimal example before running it across the repository.
</step>

<step number="5">
Use the rule to search the codebase, then refine it based on misses or false positives.
</step>

<step number="6">
If the user wants a rewrite, use ast-grep's rewrite flow after the search rule is proven.
</step>
</process>

<success_criteria>
- The rule matches the intended structure.
- The query is precise enough to avoid noisy text matches.
- The assistant can explain why ast-grep is the right tool here.
</success_criteria>
