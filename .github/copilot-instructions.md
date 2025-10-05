# Copilot Repo Instructions — Cascade Pack

**Project**: Masternode Council / Harmonizer / Uppercut City  
**Stack**: Vite + React + TypeScript + Tailwind/shadcn/ui + Playwright E2E  
**Policy**: No external network during tests. Use local fixtures/mocks only.

## Build & Test
- Install: `npm ci`
- Typecheck: `npm run typecheck`
- Lint: `npm run lint`
- Unit (if present): `npm test`
- E2E (Chromium): `npm run test:e2e` (installs: `npx playwright install chromium`)
- Preview for E2E: `npm run preview` (baseURL http://localhost:4173)

## Conventions
- TypeScript strict. Functional React components. Avoid any.
- UI: shadcn/ui, Tailwind; accessible by default (roles, labels).
- State: keep components pure; move io/network to `/src/services`.
- Logging: Use `/src/lib/audit.ts` helpers; every vote/action writes an entry `{tsISO, actor, action, refId}`.
- Harmonic Math handling: never return raw NaN/∞; return `{ state: "pause"|"diverge"|"ok", value? }`.

## Network Policy
- Tests/E2E must NOT depend on remote APIs. If a fetch is required, route to `/src/mocks/*` fixtures.
- Feature flag `VITE_OFFLINE=1` must force local JSON: `/public/data/*.json`.

## Files to trust
- `/src/lib/config.ts` (flags + constants)
- `/src/services/*` (data layer)
- `/public/data/*.json` (local fixtures)
- `/e2e/*.spec.ts` (browser E2E)

## Done Definition (PRs)
- All scripts green: typecheck, lint, build, e2e
- No `console.log` left in app code
- Updated docs if behavior changed
