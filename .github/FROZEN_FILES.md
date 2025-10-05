# Frozen Files Policy

## Overview
To prevent recursive regeneration loops in CI/CD, the following files are **frozen** and should NOT be automatically regenerated during build/test runs.

## Frozen Files (Source of Truth)

### Documentation
- `README.md` - Main project documentation
- `BRAVE_CODEX.md` - Core Brave Codex documentation (if present)
- `IMPLEMENTATION_STATUS.md` - Implementation tracking

### Configuration & Instructions
- `.github/instructions/react-components.instructions.md`
- `.github/instructions/tests.instructions.md`
- `.github/instructions/e2e.instructions.md`
- `.github/copilot-instructions.md`
- `.github/copilot-setup-steps.yml`

### Build Scripts
- `scripts/pre-publish-check.sh` - Validation only, no regeneration
- `.github/workflows/test.yml` - CI workflow

## Build Pipeline Behavior

### ✅ Allowed During CI/Build
- Install dependencies (`npm ci`)
- Type checking (`npm run typecheck`)
- Linting (`npm run lint`)
- Building (`npm run build`)
- Testing (`npm run test:e2e`)
- Reading/using frozen files

### ❌ NOT Allowed During CI/Build
- Modifying any frozen documentation files
- Regenerating instruction files
- Updating README or setup files
- Any script that writes to source-controlled docs

## Manual Documentation Updates

If documentation needs to be regenerated or updated:

1. **Manual only**: Use `npm run regen-docs`
2. **Review changes**: Check git diff before committing
3. **Commit separately**: Doc updates separate from code changes
4. **Avoid during CI**: Never in automated workflows

## Preventing Loops

The following safeguards are in place:

1. **scripts/pre-publish-check.sh**: Comments clearly state "NO regeneration"
2. **copilot-setup-steps.yml**: Comments indicate frozen steps
3. **scripts/regen-docs.sh**: Separate script with confirmation prompt
4. **This file**: Documents the policy for all contributors

## Why This Matters

Recursive regeneration loops occur when:
- Build scripts modify source files
- Modified files trigger new builds
- New builds modify files again
- Loop continues indefinitely

By freezing files and separating validation from regeneration, we ensure:
- Stable, predictable builds
- Fast CI/CD pipelines
- No infinite loops
- Clear audit trail of changes

## Questions?

If you need to update frozen files, please:
1. Make changes manually with a text editor
2. Test locally with `npm run prepublish-check`
3. Commit with clear description
4. Never automate documentation changes in CI
