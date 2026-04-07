<objective>
Document the ast-grep rule syntax needed for structural searches and refinements.
</objective>

<rule_categories>
<atomic>
<pattern>Match by code pattern with metavariables.</pattern>
<kind>Match by AST node type.</kind>
<regex>Match by node text when structure is not enough.</regex>
</atomic>

<relational>
<inside>Match a node inside another matching node.</inside>
<has>Match a node that has a matching descendant.</has>
<precedes>Match a node before another matching node.</precedes>
<follows>Match a node after another matching node.</follows>
</relational>

<composite>
<all>All sub-rules must match.</all>
<any>Any sub-rule may match.</any>
<not>Exclude matches that satisfy a sub-rule.</not>
</composite>
</rule_categories>

<core_rules>
<rule_object>
Every rule needs at least one positive key such as `pattern` or `kind`.
</rule_object>

<stop_by>
Use `stopBy: end` for relational rules when the full subtree or enclosing scope matters.
</stop_by>

<metavariables>
<single>$NAME</single>
<multi>$$$ITEMS</multi>
Use metavariables to capture identifiers, expressions, arguments, or statement lists.
</metavariables>
</core_rules>

<examples>
<example>
<rule>pattern: console.log($ARG)</rule>
</example>
<example>
<rule>
kind: function_declaration
has:
  pattern: await $EXPR
  stopBy: end
</rule>
</example>
<example>
<rule>
all:
  - kind: function_declaration
  - has:
      pattern: await $EXPR
      stopBy: end
  - not:
      has:
        pattern: try { $$$ } catch ($E) { $$$ }
        stopBy: end
</rule>
</example>
</examples>

<validation>
When a rule does not match, simplify it, confirm the language kind, and inspect the AST with `--debug-query` before adding more logic.
</validation>
