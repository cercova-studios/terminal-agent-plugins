# Tech Stack Rewrite Recommendation: [Project Name]

**Date:** [YYYY-MM-DD]
**Analyst:** Claude Code (Deep Architecture Analysis)
**Current Version:** [version/commit]

---

## Executive Summary

**Primary Recommendation:** [One-sentence recommendation]

**Expected Improvements:**
- Performance: [X]% improvement
- Complexity: [Y]% reduction
- Cost: [Z]% reduction
- Developer velocity: [Impact]

**Migration Timeline:** [X months]
**Risk Level:** [Low/Medium/High]

---

## 1. Problem Analysis

### 1.1 Core Problem Statement

**What does this software actually do?**
```
Primary function: [Description]

Core operations:
1. [Operation 1]
2. [Operation 2]
3. [Operation 3]

User-facing value: [What problem does it solve for users?]
```

### 1.2 Scale & Requirements

**Current scale:**
```
Users: [N daily/monthly active]
Requests: [N per second/minute/hour]
Data volume: [X records, Y GB/TB]
Geographic distribution: [Single region / Multi-region / Global]
```

**Future scale (12 months):**
```
Expected users: [N] ([X]% growth)
Expected requests: [N] ([X]% growth)
Expected data: [X] ([Y]% growth)
```

**Non-functional requirements:**
- Performance: [SLAs, latency targets]
- Reliability: [Uptime targets]
- Security: [Compliance needs]
- Maintainability: [Team size, expertise]

### 1.3 Current Pain Points

| Pain Point | Impact | Root Cause | Addressable by Rewrite? |
|------------|--------|------------|-------------------------|
| | | | |
| | | | |

---

## 2. Current Stack Assessment

### 2.1 Current Technology Stack

| Component | Technology | Version | Age |
|-----------|------------|---------|-----|
| Language | | | |
| Framework | | | |
| Database | | | |
| Infrastructure | | | |
| Build/Deploy | | | |

### 2.2 Stack Evaluation

**Language: [Current]**
- ✓ Strengths: [What it does well]
- ✗ Weaknesses: [Where it falls short]
- Fit for problem: [Good/Acceptable/Poor]
- Verdict: [Keep/Replace]

**Framework: [Current]**
- ✓ Strengths: [What it does well]
- ✗ Weaknesses: [Where it falls short]
- Fit for problem: [Good/Acceptable/Poor]
- Verdict: [Keep/Replace/Simplify]

**Database: [Current]**
- ✓ Strengths: [What it does well]
- ✗ Weaknesses: [Where it falls short]
- Fit for problem: [Good/Acceptable/Poor]
- Verdict: [Keep/Replace/Optimize]

[Continue for each major component]

### 2.3 Major Mismatches

1. **[Technology X] for [Use Case Y]**
   - Problem: [Why mismatch]
   - Impact: [Performance/Complexity/Cost impact]
   - Better fit: [Alternative technology]

2. **[Technology A] for [Use Case B]**
   - Problem: [Why mismatch]
   - Impact: [Performance/Complexity/Cost impact]
   - Better fit: [Alternative technology]

---

## 3. First Principles Stack Design

### 3.1 Minimal Viable Stack

**Starting from zero, what's the simplest stack that works?**

```
Problem: [Restate core problem]
Essential requirements: [List]

Minimal stack:
- Language: [Choice] - Reason: [Why]
- Framework: [Minimal/None] - Reason: [Why]
- Database: [Choice] - Reason: [Why]
- Architecture: [Monolith/Services] - Reason: [Why]
- Infrastructure: [VMs/Containers/Serverless] - Reason: [Why]

Expected characteristics:
- LOC: [~X] (vs. current [Y])
- Dependencies: [~A] (vs. current [B])
- Complexity: [Low/Medium] (vs. current [High])
- Can handle: [N requests/sec, M users]
```

### 3.2 Progressive Complexity Justification

**Adding complexity only when justified:**

| Added Complexity | Reason | Scale Threshold | Current Need |
|------------------|--------|-----------------|--------------|
| Load balancer | High traffic | >1000 req/sec | [Yes/No/Future] |
| Cache layer | Expensive queries | >100ms avg query | [Yes/No/Future] |
| Message queue | Async processing | >100 jobs/sec | [Yes/No/Future] |
| Microservices | Independent scaling | >5 services needed | [Yes/No/Future] |
| Kubernetes | Complex orchestration | >10 services | [Yes/No/Future] |

✓ = Include in initial rewrite
Future = Add when threshold reached
No = Not needed

---

## 4. Alternative Stack Evaluation

### 4.1 Alternative A: [Name, e.g., "High Performance"]

**Stack:**
```
Language: [e.g., Rust/Go]
Framework: [Minimal, e.g., Axum/stdlib]
Database: [e.g., PostgreSQL]
Infrastructure: [e.g., Docker containers on VMs]
```

**Rationale:** [Why this stack, e.g., "Maximum performance, minimal overhead"]

**Pros:**
- [Pro 1]
- [Pro 2]
- [Pro 3]

**Cons:**
- [Con 1]
- [Con 2]

**Metrics:**
| Metric | Value |
|--------|-------|
| Estimated LOC | |
| Dependencies | |
| Build time | |
| Binary size | |
| Memory footprint | |
| Throughput | |
| Latency | |
| Dev ramp-up time | |

### 4.2 Alternative B: [Name, e.g., "Developer Velocity"]

**Stack:**
```
Language: [e.g., Python/TypeScript]
Framework: [e.g., Django/Next.js]
Database: [e.g., PostgreSQL]
Infrastructure: [e.g., PaaS like Vercel/Heroku]
```

**Rationale:** [Why this stack, e.g., "Rapid development, rich ecosystem"]

**Pros:**
- [Pro 1]
- [Pro 2]
- [Pro 3]

**Cons:**
- [Con 1]
- [Con 2]

**Metrics:**
| Metric | Value |
|--------|-------|
| Estimated LOC | |
| Dependencies | |
| Build time | |
| Binary size | |
| Memory footprint | |
| Throughput | |
| Latency | |
| Dev ramp-up time | |

### 4.3 Alternative C: [Name, e.g., "Cloud Native"]

**Stack:**
```
Language: [e.g., Go/TypeScript]
Framework: [e.g., stdlib/Express]
Database: [e.g., DynamoDB/Firestore]
Infrastructure: [e.g., Serverless Lambda]
```

**Rationale:** [Why this stack, e.g., "Zero ops, auto-scaling"]

**Pros:**
- [Pro 1]
- [Pro 2]
- [Pro 3]

**Cons:**
- [Con 1]
- [Con 2]

**Metrics:**
| Metric | Value |
|--------|-------|
| Estimated LOC | |
| Dependencies | |
| Cold start | |
| Warm latency | |
| Cost (at current scale) | |
| Cost (at 10x scale) | |
| Dev ramp-up time | |

### 4.4 Comparison Matrix

| Criteria | Current | Alt A | Alt B | Alt C | Weight |
|----------|---------|-------|-------|-------|--------|
| Performance | | | | | 0.2 |
| Simplicity | | | | | 0.15 |
| Dev velocity | | | | | 0.15 |
| Operational overhead | | | | | 0.15 |
| Scalability | | | | | 0.1 |
| Cost (infra) | | | | | 0.1 |
| Team expertise | | | | | 0.1 |
| Ecosystem maturity | | | | | 0.05 |
| **Weighted Score** | | | | | |

*Rating scale: 1-5 (1=Poor, 5=Excellent)*

---

## 5. Primary Recommendation

### 5.1 Recommended Stack

**Chosen Alternative: [A/B/C]**

**Stack:**
```
Language: [Chosen]
Framework: [Chosen]
Database: [Chosen]
Infrastructure: [Chosen]
CI/CD: [Recommendation]
Monitoring: [Recommendation]
```

### 5.2 Rationale

**Why this stack:**
1. [Reason 1 - tied to problem domain]
2. [Reason 2 - tied to requirements]
3. [Reason 3 - tied to constraints]

**Key trade-offs accepted:**
- ✓ Gain: [Benefit]
- ✗ Lose: [Cost] - Mitigation: [How to address]

### 5.3 Expected Improvements

**Quantified benefits:**

```
Performance:
- Response time: [Current Xms] → [Target Yms] ([Z]% improvement)
- Throughput: [Current N req/s] → [Target M req/s] ([P]% improvement)

Complexity:
- LOC: [Current X] → [Target Y] ([Z]% reduction)
- Dependencies: [Current A] → [Target B] ([C]% reduction)
- Deployment steps: [Current N] → [Target M]

Cost:
- Infrastructure: $[X]/month → $[Y]/month ([Z]% reduction)
- Developer time: [Impact on velocity]

Reliability:
- Error rate: [Current X]% → [Target Y]%
- Deployment frequency: [Current] → [Target]
```

---

## 6. Migration Strategy

### 6.1 Approach

**Chosen strategy:** [Big Bang / Incremental / Strangler Fig Pattern]

**Rationale:** [Why this approach]

### 6.2 Phased Plan

**Phase 1: Foundation (Weeks 1-X)**
```
Goal: Core infrastructure and domain logic

Tasks:
- [ ] Set up new infrastructure
- [ ] Database schema design and migration
- [ ] Core domain models
- [ ] Authentication/authorization
- [ ] Basic API endpoints

Deliverable: Working skeleton with core functionality
Risk: [Low/Medium/High]
```

**Phase 2: Feature Parity (Weeks X-Y)**
```
Goal: Replicate all existing features

Tasks:
- [ ] Migrate feature 1
- [ ] Migrate feature 2
- [ ] API compatibility layer (if needed)
- [ ] Integration tests
- [ ] Performance testing

Deliverable: New system with feature parity
Risk: [Low/Medium/High]
```

**Phase 3: Transition (Weeks Y-Z)**
```
Goal: Production cutover

Tasks:
- [ ] Load testing at production scale
- [ ] Monitoring and alerting setup
- [ ] Blue-green deployment
- [ ] Gradual traffic migration
- [ ] Rollback procedures

Deliverable: Production system on new stack
Risk: [Low/Medium/High]
```

**Phase 4: Decommission (Weeks Z+)**
```
Goal: Clean up old system

Tasks:
- [ ] Monitor new system for N weeks
- [ ] Address any issues
- [ ] Decommission old infrastructure
- [ ] Archive old code

Deliverable: Old system fully retired
Risk: [Low]
```

### 6.3 Timeline

```
Total duration: [X weeks/months]

Breakdown:
- Phase 1: [X weeks]
- Phase 2: [Y weeks]
- Phase 3: [Z weeks]
- Phase 4: [W weeks]

Team size required: [N developers]
Effort estimate: [M person-months]
```

### 6.4 Data Migration

**Strategy:** [One-time / Incremental / Dual-write]

```
Approach:
1. [Step 1 - e.g., Export from old DB]
2. [Step 2 - e.g., Transform data]
3. [Step 3 - e.g., Import to new DB]
4. [Step 4 - e.g., Verify data integrity]

Downtime required: [None / X minutes / X hours]
Rollback plan: [Description]
```

---

## 7. Risk Assessment

### 7.1 Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| | | | |
| | | | |

### 7.2 Organizational Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| | | | |

### 7.3 Business Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| | | | |

### 7.4 Overall Risk Level

**Risk score:** [Low/Medium/High]

**Confidence level:** [Low/Medium/High]

**Recommended risk mitigation:**
1. [Key mitigation 1]
2. [Key mitigation 2]
3. [Key mitigation 3]

---

## 8. Success Metrics

### 8.1 Technical Metrics

**Track these to validate rewrite success:**

```
Performance:
- [ ] Latency: [Target]
- [ ] Throughput: [Target]
- [ ] Error rate: [Target]
- [ ] Uptime: [Target]

Efficiency:
- [ ] Infrastructure cost: [Target]
- [ ] Build time: [Target]
- [ ] Deployment time: [Target]
- [ ] Memory usage: [Target]

Complexity:
- [ ] LOC: [Target]
- [ ] Dependencies: [Target]
- [ ] Test coverage: [Target]
- [ ] Cyclomatic complexity: [Target]
```

### 8.2 Developer Metrics

```
Velocity:
- [ ] Time to implement new feature: [Baseline → Target]
- [ ] Time to fix bug: [Baseline → Target]
- [ ] Onboarding time for new dev: [Baseline → Target]

Quality:
- [ ] Bug rate: [Baseline → Target]
- [ ] Incident frequency: [Baseline → Target]
- [ ] Code review time: [Baseline → Target]
```

### 8.3 Business Metrics

```
Impact:
- [ ] Customer satisfaction: [Measure]
- [ ] Feature delivery frequency: [Baseline → Target]
- [ ] Support ticket volume: [Baseline → Target]
- [ ] Total cost of ownership: [Baseline → Target]
```

---

## 9. Alternative Scenarios

### 9.1 If Constraints Change

**Scenario: Budget becomes critical constraint**
→ Consider [Alternative X] which optimizes for cost

**Scenario: Timeline becomes critical**
→ Consider incremental migration instead of full rewrite
→ Focus on highest-value components first

**Scenario: Team lacks expertise in recommended stack**
→ Consider [Alternative Y] aligned with current expertise
→ OR invest in training/hiring before starting

### 9.2 Deferred Decision Points

**Questions to revisit:**
- If scale exceeds [X threshold], reconsider [Y decision]
- If team grows to [N people], evaluate [Z architectural pattern]
- If [A requirement] emerges, consider [B technology]

---

## 10. Conclusion

**Bottom line:** [One paragraph summary and recommendation]

**Recommended action:** [Start rewrite / Defer / Refactor instead]

**Next immediate steps:**
1. [Action 1]
2. [Action 2]
3. [Action 3]

**Decision required by:** [Stakeholder] by [Date]

---

## Appendices

### Appendix A: Cost-Benefit Analysis
[Detailed financial analysis]

### Appendix B: Technology Deep Dives
[Detailed analysis of specific technologies]

### Appendix C: Reference Architectures
[Example architectures using recommended stack]

### Appendix D: Proof of Concept Results
[If POC was performed]

---

**Report generated by:** Claude Code Deep Architecture Analysis Skill
**Based on analysis from:** [Analysis report name/date]
