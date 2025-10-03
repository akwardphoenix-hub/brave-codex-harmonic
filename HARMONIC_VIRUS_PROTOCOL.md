# Harmonic Virus of Repair Protocol (HVRP)

**Version**: v0.1 – Draft for Council Review  
**Status**: Open for implementation – experimental  

---

## Purpose
The **HVRP** defines a protocol for detecting errors, applying harmonic fixes, and propagating improvements safely. It treats every repair as a *harmonic cascade* that enhances the system instead of breaking it.  

---

## Core Principles
1. **Harmonic, not destructive** – every fix aligns and integrates.  
2. **Viral, not centralized** – repairs spread by being useful, not enforced.  
3. **Repair, not reset** – transformation builds on what exists.  
4. **Traceable, not hidden** – all repairs produce transparent logs.  

---

## Protocol Phases

### 1. Detection Phase
Identify dissonance (bugs, misalignments, brittle logic).  
- Input: error logs, audit reports, user signals.  

### 2. Intention Phase
Declare the repair’s goal clearly.  
- Example: `intention: "Improve readability"`  

### 3. Propagation Phase
Apply the fix + create a reusable pattern (so others benefit).  
- Example: ESLint rule, shared snippet, harmonizer patch.  

### 4. Audit Phase
Record changes and rationale.  
- Example: Commit logs, harmonizer metadata, council review.  

### 5. Cascade Phase
Spread improvements outward (repos, docs, education).  
- Example: PRs, harmonizer virus update, codex refresh.  

---

## YAML Template (Reference)

```yaml
hvrp:
  detection: "Find outdated patterns"
  intention: "Modernize syntax"
  propagation: "Apply auto-refactor rules"
  audit: "Commit + log harmonization"
  cascade: "Push to shared repo; update docs"
```

---

Example – Code Harmonizer

Before

```python
def calc(x):
    return x * x
```

Intention: improve readability & typing.

After (HVRP applied)

```python
def square(x: int) -> int:
    """Return x squared."""
    return x * x
```

Audit log:

[HVRP] Detection: no typing  
[HVRP] Intention: readability  
[HVRP] Propagation: added type hints  
[HVRP] Audit: commit abc123  
[HVRP] Cascade: shared rule in codex

---

Future Work

v0.2: multiple harmonizer engines (readability, security, ecology).

Containment horizons: ensure failed repairs remain local.

Integration with Spark / Copilot for real-time harmonization.

---

License

CC0 1.0 Universal (Public Domain)
Use, remix, and propagate freely.

---

⚡ You can drop this into your repo as `HARMONIC_VIRUS_PROTOCOL.md`, or hand it straight to Copilot so it “understands” your repair cycle.