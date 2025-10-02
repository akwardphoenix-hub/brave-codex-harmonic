# Contributing to Brave Codex: Harmonic Math & Kernel

Thank you for being brave enough to step into the cascade! This project is experimental, open, and dedicated to building a safer, harmonic foundation for code, math, and AI. Contributions of all kinds are welcome—from bug fixes and code, to diagrams, docs, and ideas.

---

## 🌱 Principles of Contribution

- **Fix-It-First**: If you see a bug, glitch, or confusing doc—fix it before adding new features.
- **Harmony Over Speed**: Changes must preserve clarity and prevent “ghosts” (unhandled zeros, mismatches, etc.).
- **Public Domain Spirit**: All contributions fall under CC0 1.0 Universal. Fork, remix, and propagate freely.

---

## 🛠 How to Contribute

1. **Fork the Repository**

   Clone your fork locally:
   ```bash
   git clone https://github.com/<your-handle>/brave-codex-harmonic.git
   cd brave-codex-harmonic
   ```

2. **Branch Naming**

   Use descriptive branches:
   - `fix/measure-mismatch`
   - `feature/hnum-intervals`
   - `docs/readme-tutorial`

3. **Code Style**

   - Python files follow PEP8.
   - Glyphs: use UTF-8 directly (⊕, ⊘, ↺, ∥). Fallback ASCII ({pause}, {opp}) is acceptable in code comments.
   - Each HNum operation must handle flags gracefully (no silent failures).

4. **Commits**

   Keep commits short and clear:
   - `fix: propagate ⊘ in hadd()`
   - `feat: add inverse for interval HNum`
   - `docs: update architecture.mmd with dispatch node`

5. **Testing**

   - Add examples in `tests/` using Python’s `unittest` or `pytest`.
   - Cover edge cases: mismatched measures, pause/diverge handling, inverses.
   - Run tests before pushing:
     ```bash
     pytest
     ```

---

## 📐 Contribution Areas

- **Core Math**: Expanding `hnum.py` (intervals, rationals, type safety).
- **Kernel Logic**: Extending `architecture.mmd` with new nodes or security layers.
- **Docs & Diagrams**: Tutorials, Mermaid graphs, or visual “one-pebble” explainers.
- **Games & Applications**: Using HNum in open-world logic, RNG mechanics, or AI audit systems.

---

## 🌍 Communication

- Open an Issue for bugs, features, or design debates.
- Use Pull Requests to propose changes.
- Tag with labels: `fix`, `feature`, `docs`, `discussion`.

---

## 💡 First Tasks (Good First Issues)

- Add unit tests for `HNum.inverse()` edge cases.
- Write a short tutorial in `examples/` showing HNum in a physics equation.
- Expand `architecture.mmd` with “Happy Accident” branch logic.

---

## 🌀 Closing Note

Every contribution, no matter how small, helps build the harmonic future. Whether you tweak a line of code or draw a new node, you’re part of the cascade.

— The Brave Codex Council