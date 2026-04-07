<objective>
Use ast-grep to search for code by structure, and to rewrite code when a structural pattern is the right entry point.
</objective>

<quick_start>
<basic_flow>
1. Turn the request into a tiny example of the code shape.
2. Express that shape as a simple `pattern` rule first.
3. Escalate to `kind`, `has`, `inside`, `all`, `any`, or `not` only when needed.
4. Test on a small example before searching the repo.
</basic_flow>

<search_first>
Use ast-grep when syntax matters more than wording: function forms, call patterns, control-flow shapes, or language-specific structures.
</search_first>
</quick_start>

<workflow>
<step number="1">
Clarify the language and the exact structure to match. Ask what should be included or excluded if the pattern is ambiguous.
</step>

<step number="2">
Write a minimal example snippet and confirm the AST shape with `--debug-query` when needed.
</step>

<step number="3">
Build the rule from the outside in: `pattern` first, then `kind`, then relational or composite logic.
</step>

<step number="4">
Use `stopBy: end` for relational rules that need to inspect the full enclosing scope.
</step>

<step number="5">
Search the repository once the rule matches the example.
</step>

<step number="6">
If the user wants a transformation, use ast-grep rewrite mode after the search rule is validated.
</step>
</workflow>

<common_patterns>
<pattern name="async-with-await">
Use `has` to find async functions containing `await`.
</pattern>

<pattern name="console-in-class">
Use `inside` to find a call inside a method or class context.
</pattern>

<pattern name="missing-try-catch">
Use `not` with `has` to find functions that contain `await` but do not contain `try/catch`.
</pattern>
</common_patterns>

<rewrite_workflow>
<step number="1">
Prefer `run --rewrite` for simple replacements.
</step>

<step number="2">
Use YAML rules with `fix` when the transformation depends on structure or metavariables.
</step>

<step number="3">
Use `--interactive` when each change should be reviewed before it is applied.
</step>
</rewrite_workflow>

<cli_examples>
<example>
<command>ast-grep run --pattern 'console.log($ARG)' --lang javascript /path/to/project</command>
</example>
<example>
<command>ast-grep scan --rule my_rule.yml /path/to/project</command>
</example>
<example>
<command>ast-grep run --pattern 'foo' --rewrite 'bar' --lang python</command>
</example>
</cli_examples>

<success_criteria>
- The rule is built from a small example first.
- The search is structural, not just lexical.
- The assistant knows when to stop at search and when to rewrite.
</success_criteria>
