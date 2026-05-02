# Architecture Analysis Report: [Project Name]

**Analysis Date:** [YYYY-MM-DD]
**Analyst:** Claude Code (Deep Architecture Analysis)
**Repository:** [URL or path]
**Version/Commit:** [git commit hash]

---

## Executive Summary

[3-5 bullet points summarizing key findings]
-
-
-
-
-

**Overall Assessment:** [Brief overall assessment of architecture quality]

**Primary Recommendation:** [One-sentence primary recommendation]

---

## 1. Project Overview

### 1.1 Basic Information
- **Name:** [project name]
- **Purpose:** [what does it do?]
- **Language(s):** [primary languages with LOC breakdown]
- **Framework(s):** [main frameworks used]
- **Age:** [repository age, commit count]
- **Activity:** [active/maintained/stale]
- **Team size:** [estimated from git history]

### 1.2 Repository Statistics
```
Total Lines of Code: [X]
Number of Files: [Y]
Number of Commits: [Z]
Contributors: [N]
Repository Size: [MB/GB]
```

### 1.3 Technology Stack
| Component | Technology | Version |
|-----------|------------|---------|
| Language | | |
| Framework | | |
| Database | | |
| Build Tool | | |
| Package Manager | | |
| Testing | | |
| CI/CD | | |

---

## 2. Architecture Analysis

### 2.1 System Architecture

[Describe overall architecture: monolith, microservices, serverless, etc.]

**Architecture Diagram:**
```
[ASCII art or Mermaid diagram]

Example Mermaid:
graph TB
    Client[Client]
    API[API Server]
    DB[Database]
    Cache[Cache]

    Client --> API
    API --> DB
    API --> Cache
```

### 2.2 Component Breakdown

| Component | Purpose | LOC | Complexity | Dependencies |
|-----------|---------|-----|------------|--------------|
| | | | | |
| | | | | |

### 2.3 Layer Structure

[Describe layers: presentation, business logic, data access, etc.]

```
Layers (top to bottom):
1. [Layer name] - [Purpose] - [LOC]
2. [Layer name] - [Purpose] - [LOC]
3. [Layer name] - [Purpose] - [LOC]
...

Abstraction depth: [N layers]
Assessment: [Appropriate / Over-layered / Under-layered]
```

### 2.4 Data Flow

[Describe how data flows through the system]

```
Typical request flow:
1. [Step 1]
2. [Step 2]
3. [Step 3]
...

Critical paths:
- [Path 1]: [description]
- [Path 2]: [description]
```

### 2.5 Integration Points

| Integration | Type | Protocol | Purpose |
|-------------|------|----------|---------|
| | | | |

---

## 3. Dependency Analysis

### 3.1 Direct Dependencies
```
Total direct dependencies: [N]
```

| Dependency | Version | Size | Purpose | Essential? |
|------------|---------|------|---------|------------|
| | | | | |

### 3.2 Transitive Dependencies
```
Total dependencies (direct + transitive): [N]
Dependency explosion ratio: [transitive/direct]
```

### 3.3 Dependency Bloat Assessment

**Heavy dependencies (>1MB):**
- [Dependency name]: [Size] - [Purpose] - [Assessment: Essential/Replaceable/Bloat]

**Unused dependencies detected:**
- [List]

**Overlapping dependencies:**
- [Example: lodash + underscore both provide utilities]

**Total dependency size:** [X MB]

**Bloat score:** [percentage]%
```
Calculation:
Minimal viable dependencies: [N]
Current dependencies: [M]
Bloat = (M - N) / M × 100% = [X]%
```

---

## 4. Code Quality & Patterns

### 4.1 Design Patterns

**Positive patterns identified:**
- [Pattern name]: [Location] - [Assessment]

**Anti-patterns identified:**
- [Anti-pattern name]: [Location] - [Impact]

### 4.2 Code Complexity

**Cyclomatic Complexity:**
```
Average: [X]
Highest: [Y] in [file:function]
Files with complexity > 10: [N]
```

**File Size Distribution:**
```
< 100 LOC: [N files]
100-500 LOC: [N files]
500-1000 LOC: [N files]
> 1000 LOC: [N files] ← God objects
```

**Largest files:**
1. [file path]: [LOC] - [Assessment]
2. [file path]: [LOC] - [Assessment]

### 4.3 Code Duplication

```
Duplication ratio: [X]%
Duplicate blocks: [N]
```

**Major duplications:**
- [Location 1] ↔ [Location 2]: [Lines duplicated]

### 4.4 Dead Code Estimate

```
Estimated dead code: [X]% of codebase
Sources:
- Unused exports: [N]
- Unreachable code: [N]
- Commented code blocks: [N]
- TODO/FIXME from >1 year ago: [N]
```

---

## 5. Efficiency & Bloat Analysis

### 5.1 Bloat Summary

| Category | Current | Minimal | Bloat | Impact |
|----------|---------|---------|-------|--------|
| LOC | | | | |
| Files | | | | |
| Dependencies | | | | |
| Build size | | | | |

### 5.2 Code Bloat

**Over-abstraction examples:**
```
[File:line] - [Description]
Example:
src/repository/UserRepositoryInterface.ts:10
- Abstract interface with single implementation
- Can be replaced with direct implementation
- Bloat: 50 LOC of unnecessary abstraction
```

**Excessive configuration:**
```
Configuration options: [N]
Actually used: [M]
Unused: [N-M]
```

### 5.3 Algorithmic Inefficiencies

**O(n²) or worse:**
```
[File:line] - [Description]
Impact: [High/Medium/Low]
```

**N+1 query patterns:**
```
[File:line] - [Description]
Impact: [High/Medium/Low]
```

### 5.4 Build Bloat

```
Build output size: [X MB]
Breakdown:
- Application code: [Y MB]
- Dependencies: [Z MB]
- Assets: [W MB]
- Debug info: [V MB]

Optimization opportunities:
- [Opportunity 1]: Potential [X MB] reduction
- [Opportunity 2]: Potential [Y MB] reduction
```

---

## 6. Security Analysis

### 6.1 Attack Surface

**Entry points:**
- HTTP endpoints: [N]
- CLI arguments: [N]
- File inputs: [N]
- Environment variables: [N]

**External integrations:**
- [Integration name]: [Protocol] - [Risk level]

### 6.2 Vulnerabilities Identified

| Severity | Type | Location | Description | Recommendation |
|----------|------|----------|-------------|----------------|
| Critical | | | | |
| High | | | | |
| Medium | | | | |
| Low | | | | |

### 6.3 Security Practices

**Input validation:** [Present/Inconsistent/Missing]
**Authentication:** [Method] - [Assessment]
**Authorization:** [Method] - [Assessment]
**Data encryption:** [At rest / In transit / None]
**Secret management:** [Method] - [Assessment]
**Dependency vulnerabilities:** [N found via audit]

### 6.4 Hardcoded Secrets

```
Potential secrets found: [N]
Locations:
- [File:line]: [Type of secret]
```

---

## 7. First Principles Deconstruction

### 7.1 Essential Problem

**What does this software actually do?**
```
Core operations:
1. [Operation 1]
2. [Operation 2]
3. [Operation 3]

Scale requirements:
- Requests: [N per second/minute/hour]
- Data volume: [X records/GB/TB]
- Users: [N concurrent/daily/monthly]
```

### 7.2 Complexity Audit

**Essential complexity:** [Components/features that MUST exist]
- [Component 1]: Reason for necessity
- [Component 2]: Reason for necessity

**Justified complexity:** [Adds value exceeding cost]
- [Component 3]: Benefit
- [Component 4]: Benefit

**Questionable complexity:** [Marginal benefit]
- [Component 5]: Limited benefit
- [Component 6]: Limited benefit

**Bloat / Accidental complexity:** [No clear benefit]
- [Component 7]: Remove in rewrite
- [Component 8]: Remove in rewrite

### 7.3 Minimal Viable Architecture

**If building from scratch today:**
```
Language: [Choice based on problem domain]
Framework: [Minimal or none]
Database: [Appropriate for data model]
Architecture: [Monolith/services based on scale]
Infrastructure: [Simplest that works]

Estimated LOC: [X] (vs. current [Y])
Estimated dependencies: [A] (vs. current [B])
Complexity score: [Low/Medium] (vs. current [High])
```

### 7.4 Gap Analysis

```
Current system complexity: [Score 1-10]
Minimal viable complexity: [Score 1-10]
Over-engineering factor: [X]x

Breakdown:
- Framework overhead: [X]% unnecessary
- Dependency bloat: [Y]% unnecessary
- Over-abstraction: [Z]% unnecessary
- Premature optimization: [W]% unnecessary
```

---

## 8. Recommendations

### 8.1 Quick Wins (Low effort, high impact)

1. **[Recommendation 1]**
   - Impact: [High/Medium/Low]
   - Effort: [Low]
   - Expected improvement: [Quantified]
   - Implementation: [Brief steps]

2. **[Recommendation 2]**
   - Impact: [High/Medium/Low]
   - Effort: [Low]
   - Expected improvement: [Quantified]
   - Implementation: [Brief steps]

### 8.2 Strategic Improvements (Medium-high effort)

1. **[Recommendation 3]**
   - Impact: [High]
   - Effort: [Medium/High]
   - Expected improvement: [Quantified]
   - Implementation: [Brief steps]

### 8.3 Rewrite Considerations

**Should this be rewritten?**
[Yes/No/Partial] - [Reasoning]

**If yes, recommended approach:**
- Tech stack: [Specific recommendations]
- Migration strategy: [Big bang/Incremental/Strangler fig]
- Timeline estimate: [X months]
- Risk level: [Low/Medium/High]

**If no, refactoring priorities:**
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

---

## 9. Metrics Summary

```
Code Metrics:
- Total LOC: [X]
- Bloat LOC: [Y] ([Z]%)
- Test coverage: [N]%
- Cyclomatic complexity: [Avg]
- Duplication: [N]%

Dependency Metrics:
- Total dependencies: [N]
- Unused dependencies: [M]
- Total size: [X MB]
- Bloat: [Y MB] ([Z]%)

Performance Metrics:
- Build time: [X sec]
- Binary size: [Y MB]
- Startup time: [Z ms]

Security Metrics:
- Vulnerabilities: [N] (Critical: [A], High: [B], Medium: [C], Low: [D])
- Attack surface score: [High/Medium/Low]
- Security features: [N/M implemented]
```

---

## 10. Conclusion

[Summary paragraph synthesizing all findings and primary recommendation]

**Overall Architecture Grade:** [A/B/C/D/F]

**Key Takeaways:**
1. [Takeaway 1]
2. [Takeaway 2]
3. [Takeaway 3]

**Next Steps:**
1. [Action item 1]
2. [Action item 2]
3. [Action item 3]

---

## Appendices

### Appendix A: Detailed Metrics
[Detailed metric tables and data]

### Appendix B: Tool Outputs
[Raw outputs from analysis tools]

### Appendix C: Code Samples
[Relevant code snippets for findings]

### Appendix D: Architecture Diagrams
[Additional diagrams if needed]

---

**Report generated by:** Claude Code Deep Architecture Analysis Skill
**Analysis duration:** [X hours]
**Tools used:** [List of tools]
