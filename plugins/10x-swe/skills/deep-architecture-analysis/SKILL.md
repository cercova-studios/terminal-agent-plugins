---
name: deep-architecture-analysis
description: Performs comprehensive reverse engineering and architecture analysis of GitHub repositories and application binaries. Identifies inefficiencies, bloat, vulnerabilities, and architectural patterns. Deconstructs from first principles to recommend optimal tech stacks for rewrites and modernization.
---

<essential_principles>
## Purpose

This skill performs deep architectural analysis and reverse engineering for the purpose of understanding existing systems to rebuild them better. This is legitimate software reengineering work used for:
- **Migration planning** - Understanding legacy systems to inform modernization
- **Tech debt assessment** - Identifying bloat, inefficiencies, and architectural debt
- **Security auditing** - Finding vulnerabilities and attack surfaces (authorized contexts only)
- **Architecture modernization** - Deconstructing from first principles to recommend better approaches
- **Performance optimization** - Identifying bottlenecks and inefficient patterns

## Core Analysis Pillars

1. **Architecture Understanding** - Map the overall system design, dependencies, and data flows
2. **Efficiency Analysis** - Identify computational waste, bloat, and over-engineering
3. **Security Assessment** - Find potential vulnerabilities, leaks, and attack surfaces
4. **First Principles Deconstruction** - Question every complexity and rebuild from fundamentals
5. **Tech Stack Evaluation** - Assess if current technologies are optimal for the problem domain

## Methodological Approach

**Start broad, go deep, synthesize findings:**
- Repository analysis: Structure → Dependencies → Code patterns → Data flows
- Binary analysis: Architecture → System calls → Memory patterns → Reverse engineering
- Evaluation: What's necessary vs. bloat? What's elegant vs. technical debt?
- Recommendation: What's the minimal viable architecture? What tech stack fits best?

## Ethical Guidelines

This skill performs analysis for **authorized, constructive purposes**:
- ✓ Analyzing your own software or with explicit authorization
- ✓ Open source software analysis for learning and improvement
- ✓ CTF challenges and educational reverse engineering
- ✓ Authorized security testing and vulnerability research
- ✗ Unauthorized exploitation or malicious reverse engineering
- ✗ Bypassing security for malicious purposes
</essential_principles>

<intake>
What would you like to analyze?

1. **GitHub repository** - Analyze codebase architecture, patterns, and inefficiencies
2. **Application binary** - Reverse engineer compiled binary (ELF, PE, Mach-O, etc.)
3. **Both repository + binaries** - Full-spectrum analysis of both source and compiled artifacts
4. **Tech stack recommendation** - Evaluate current stack and recommend optimal alternatives for rewrite

If you have a specific GitHub URL or binary path, provide it now. Otherwise, specify the type of analysis.

**Wait for response before proceeding.**
</intake>

<routing>
| Response | Next Action | Workflow |
|----------|-------------|----------|
| 1, "repository", "repo", "github", "codebase" | workflows/analyze-repository.md |
| 2, "binary", "executable", "ELF", "PE", "Mach-O" | workflows/analyze-binary.md |
| 3, "both", "full", "complete" | workflows/full-analysis.md |
| 4, "recommend", "tech stack", "rewrite", "alternatives" | workflows/recommend-tech-stack.md |

**Intent-based routing (if user provides URL or path directly):**
- If github.com URL provided → workflows/analyze-repository.md
- If binary path provided → workflows/analyze-binary.md
- If "analyze X for rewrite" → workflows/full-analysis.md

**After routing to workflow, follow it exactly.**
</routing>

<quick_reference>
## Analysis Capabilities

**Repository Analysis:**
- Architecture mapping (components, layers, boundaries)
- Dependency analysis (direct, transitive, bloat detection)
- Code quality patterns (anti-patterns, over-engineering)
- Performance hotspots (algorithmic complexity, I/O patterns)
- Security surface (input validation, auth flows, data exposure)
- Bloat identification (unused code, redundant abstractions, unnecessary dependencies)

**Binary Analysis:**
- Architecture detection (x86, x64, ARM, ARM64, RISC-V, etc.)
- Format analysis (ELF, PE, Mach-O structure and metadata)
- System call tracing (syscall patterns, I/O operations)
- Library dependencies (shared objects, dynamic linking)
- String/constant analysis (config, endpoints, secrets)
- Disassembly and control flow (function signatures, logic patterns)
- Memory analysis (heap/stack patterns, potential leaks)

**Tech Stack Evaluation:**
- Problem-domain fit (is the current stack appropriate?)
- Complexity vs. requirements (over-engineering detection)
- Performance characteristics (is this tech optimized for the workload?)
- Ecosystem maturity (library support, tooling, community)
- First principles reconstruction (what's the simplest stack that could work?)
</quick_reference>

<reference_index>
## Domain Knowledge

All in `references/`:

**Analysis Techniques:**
- repository-analysis-methods.md - Systematic codebase exploration strategies
- binary-analysis-tools.md - Reverse engineering toolchain and techniques
- bloat-detection-patterns.md - Common sources of unnecessary complexity

**Evaluation Frameworks:**
- first-principles-analysis.md - Deconstructing architecture from fundamentals
- tech-stack-evaluation-matrix.md - Framework for assessing technology choices
- architecture-patterns-catalog.md - Common patterns and their trade-offs

**Tooling:**
- static-analysis-tools.md - Tools for code analysis (semgrep, codeql, etc.)
- binary-analysis-tools.md - Disassemblers, debuggers, tracers
- visualization-tools.md - Architecture diagrams and flow visualization
</reference_index>

<workflows_index>
## Workflows

All in `workflows/`:

| Workflow | Purpose |
|----------|---------|
| analyze-repository.md | Deep analysis of GitHub repositories |
| analyze-binary.md | Reverse engineering of compiled binaries |
| full-analysis.md | Combined repository + binary analysis |
| recommend-tech-stack.md | Evaluate and recommend optimal tech stack for rewrite |
</workflows_index>

<output_templates>
## Analysis Report Templates

All in `templates/`:

- architecture-analysis-report.md - Comprehensive architecture breakdown
- efficiency-audit-report.md - Performance and bloat analysis
- security-surface-report.md - Attack surface and vulnerability assessment
- rewrite-recommendation.md - Tech stack recommendation and migration plan
</output_templates>

<success_criteria>
A successful analysis includes:
- Complete architecture map with component boundaries and data flows
- Identified inefficiencies with quantified impact (complexity, performance, memory)
- Security surface assessment with prioritized findings
- Clear bloat identification with removal recommendations
- First principles deconstruction explaining what complexity is unnecessary
- Actionable tech stack recommendation with migration strategy
- All findings backed by evidence from code/binary analysis
</success_criteria>
