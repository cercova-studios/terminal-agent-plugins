# Bloat Detection Patterns

## Overview
Common patterns and indicators of unnecessary complexity, excessive dependencies, dead code, and over-engineering in software systems.

## Dependency Bloat

### 1. Transitive Dependency Explosion
**Pattern:** Small direct dependencies pulling in hundreds of transitive dependencies

**Detection:**
```bash
# Node.js
npm ls --all | wc -l
# If > 500 packages for simple app: investigate

# Python
pip list | wc -l
pipdeptree

# Go
go mod graph | wc -l
```

**Red flags:**
- 100+ direct dependencies for medium app
- 1000+ total dependencies (direct + transitive)
- Multiple versions of same package
- Dependencies larger than your code

### 2. Heavy Dependencies for Simple Tasks
**Pattern:** Using full framework when stdlib suffices

**Examples:**
```javascript
// Bloat
import moment from 'moment';  // 67KB
import lodash from 'lodash';  // 71KB
import axios from 'axios';    // 13KB

// Minimal
const date = new Date().toISOString();
const map = arr.map(x => x * 2);
const resp = await fetch(url);
```

**Detection:**
```bash
# Find large dependencies
npm list --depth=0 --parseable | xargs du -sh | sort -h | tail -20

# Python
pip list --format=freeze | while read pkg; do
  pip show $pkg | grep -E "Name|Size"
done | paste - - | sort -k4 -h
```

### 3. Unused Dependencies
**Pattern:** Dependencies declared but never imported

**Detection:**
```bash
# Node.js
npx depcheck

# Python
pip-autoremove --list
pipenv check --unused

# Go
go mod tidy  # Removes unused
```

### 4. Overlapping Dependencies
**Pattern:** Multiple packages doing same thing

**Examples:**
- `moment` + `date-fns` + `dayjs` (all date libraries)
- `lodash` + `underscore` (same utility functions)
- `axios` + `node-fetch` + `request` (all HTTP clients)

**Detection:**
```bash
# List all dependencies
npm ls --depth=0
# Manually identify overlaps
```

## Code Bloat

### 1. Dead Code
**Pattern:** Code that's never executed

**Detection:**
```bash
# Find unused exports (JavaScript)
npx ts-prune  # TypeScript
npx findead   # JavaScript

# Find unused functions (Python)
vulture .

# Coverage-based dead code
# Run tests with coverage, find 0% covered code
pytest --cov=. --cov-report=html
# Check htmlcov/index.html for untested code
```

**Indicators:**
- Functions/classes never called
- Imports never used
- Commented-out code
- TODO/FIXME with old dates

### 2. Duplicate Code
**Pattern:** Same logic repeated multiple times

**Detection:**
```bash
# Find copy-paste
jscpd . --min-lines 5

# Language-agnostic
simian **/*.py **/*.js

# Python-specific
pylint --disable=all --enable=duplicate-code .
```

**Red flags:**
- >5% duplication ratio
- Same logic in 3+ places
- Near-identical files

### 3. Over-Abstraction
**Pattern:** Abstractions that hide no complexity

**Indicators:**
```
AbstractFactoryManagerFactoryProvider
- Single implementation
- No polymorphism
- Just forwards calls
```

**Detection:**
```bash
# Find "Abstract", "Manager", "Handler", "Wrapper"
Grep: "Abstract.*|.*Manager|.*Handler|.*Wrapper|.*Factory" -i

# Classes with single implementation
# Check if interface/abstract class has only 1 concrete class
```

**Examples:**
```python
# Bloat
class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_user(self, id): pass

class DatabaseUserRepository(UserRepositoryInterface):
    def get_user(self, id):
        return db.query(User).get(id)

user_repo = DatabaseUserRepository()  # Only implementation

# Minimal
def get_user(id):
    return db.query(User).get(id)
```

### 4. Excessive Configurability
**Pattern:** Configuration for things that never change

**Indicators:**
- 100+ config options
- Config files larger than code
- Environment variables for constants
- Feature flags that are always on

**Detection:**
```bash
# Count config options
grep -E "config\[|getenv\(|Config\." -r src/ | wc -l

# Find feature flags
Grep: "feature_flag|FeatureFlag|if.*config"
```

## File System Bloat

### 1. Large Files
**Pattern:** God objects / files doing too much

**Detection:**
```bash
# Find large files (>500 LOC is suspicious)
fd -t f | xargs wc -l | sort -n | tail -20

# Files with many classes/functions
# Python
Grep: "^def |^class " *.py | cut -d: -f1 | uniq -c | sort -n
```

**Red flags:**
- >1000 LOC in single file
- >20 functions in single file
- >10 classes in single file

### 2. Unused Files
**Pattern:** Files not imported anywhere

**Detection:**
```bash
# Find files not referenced in imports
# Create list of all files
fd -e py -e js -e ts > /tmp/all_files

# Find files never imported
# (Check if filename appears in any import statement)
while read file; do
  basename=$(basename "$file" | sed 's/\..*//')
  git grep -q "from.*$basename\|import.*$basename" || echo "$file"
done < /tmp/all_files
```

### 3. Build Artifacts Bloat
**Pattern:** Huge build outputs

**Detection:**
```bash
# Build directory sizes
du -sh dist/ build/ target/ node_modules/ .next/

# Bundle size analysis
# JavaScript
npx webpack-bundle-analyzer

# Check what's in the bundle
npx source-map-explorer dist/bundle.js
```

**Red flags:**
- 10MB+ JavaScript bundle
- 100MB+ Docker image for simple app
- node_modules/ > 500MB

## Algorithmic Bloat

### 1. Nested Loops
**Pattern:** O(n²) or worse complexity

**Detection:**
```bash
# Find nested loops
Grep: "for.*\n.*for|while.*\n.*while" -A 1

# More sophisticated: look for loops in loops
Grep: "    for |    while " -B 3 | grep -E "^for |^while "
```

### 2. N+1 Query Pattern
**Pattern:** Database query inside loop

**Detection:**
```bash
# Find potential N+1 issues
Grep: "for.*in.*:\n.*query\|for.*in.*:\n.*find\|for.*in.*:\n.*select"

# ORM-specific
Grep: "for.*in.*\.all\(\):" -A 2 | grep -E "\.get\(|\.filter\("
```

### 3. Inefficient Data Structures
**Pattern:** Wrong data structure for access pattern

**Indicators:**
```python
# Bloat: O(n) lookup
users = [...]
for user in users:
    if user.id == target_id:  # Linear search!
        return user

# Efficient: O(1) lookup
users = {user.id: user for user in users}
return users.get(target_id)
```

**Detection:**
```bash
# Find linear searches in loops
Grep: "for.*if.*==|for.*in.*if "
```

## Architecture Bloat

### 1. Microservices Over-Application
**Pattern:** Too many services for team size

**Rule of thumb:**
- 1-3 developers: Monolith
- 4-10 developers: Maybe 2-3 services
- 10+ developers: Microservices if needed

**Red flags:**
- Services > 2 × developers
- Services that only talk to 1 other service
- Services sharing database
- Services deployed together

### 2. Middleware Chain Bloat
**Pattern:** Long chain of middleware/interceptors

**Detection:**
```bash
# Count middleware
Grep: "app.use\(|@middleware|middleware ="

# Trace request through middleware
# Log execution of each middleware
```

**Red flags:**
- >10 middleware for simple app
- Middleware that do nothing (just pass through)
- Middleware order matters (tight coupling)

### 3. Layer Over-Proliferation
**Pattern:** Too many abstraction layers

**Example:**
```
API Controller
→ Service Layer
→ Business Logic Layer
→ Repository Interface
→ Repository Implementation
→ ORM
→ Database
```

**Red flags:**
- >4 layers for simple CRUD
- Layers with 1:1 function forwarding
- More abstraction than business logic

## Quantifying Bloat

### Bloat Score Calculation
```
Bloat Score = (Current - Minimal) / Current × 100%

Where:
- Current = actual LOC/dependencies/files
- Minimal = estimated necessary LOC/dependencies/files

Example:
- Current: 50K LOC, 200 dependencies
- Minimal: 15K LOC, 20 dependencies
- Bloat: (50-15)/50 × 100% = 70% code bloat
        (200-20)/200 × 100% = 90% dependency bloat
```

### Impact Assessment
```
For each bloat source:

1. Size impact: [X LOC, Y MB, Z dependencies]
2. Performance impact: [latency, memory, CPU]
3. Complexity impact: [learning curve, debugging difficulty]
4. Maintenance cost: [time to understand, modify, test]

Priority = Size × Performance × Complexity × Maintenance
```

## Bloat Reduction Strategies

### 1. Dependency Pruning
```
1. List all dependencies with sizes
2. For each dependency:
   - Is it used? (depcheck)
   - Can stdlib replace it? (often yes for utils)
   - Is smaller alternative available?
3. Remove unused
4. Replace heavy with light
5. Inline simple ones
```

### 2. Code Elimination
```
1. Find dead code (coverage-based)
2. Remove commented code (use git history)
3. Consolidate duplicates
4. Flatten over-abstractions
5. Delete unused files
```

### 3. Architectural Simplification
```
1. Merge microservices if traffic doesn't justify split
2. Remove unnecessary middleware
3. Collapse abstraction layers
4. Replace framework with stdlib where possible
```

## Red Flags Checklist

Quick checklist for bloat indicators:
- [ ] Dependencies > 100
- [ ] Dependency size > code size
- [ ] Single file > 1000 LOC
- [ ] Build output > 10MB (for web app)
- [ ] Docker image > 500MB (for simple app)
- [ ] >10 microservices for small team
- [ ] Nested loops in hot path
- [ ] Abstract base classes with single impl
- [ ] >50% test code coverage < 80% (suggests dead code)
- [ ] Config options > 50
- [ ] Middleware chain > 10
- [ ] More than 4 abstraction layers

If 5+ checked: significant bloat likely exists.
