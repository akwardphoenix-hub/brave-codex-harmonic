---
applyTo: "e2e/**/*.spec.ts"
---

# Playwright E2E — Rules

- Use Chromium only by default to keep CI fast.
- Serve built app with `npm run preview` (http://localhost:4173).
- Never call remote APIs. If data needed, place JSON into `/public/data/` and load relative paths in app.

Good patterns:
- `page.goto('/')` then wait for role/text not timeouts.
- Use `getByRole`, `getByText`, `getByTestId`.
- Keep tests idempotent; reset localStorage between tests.
