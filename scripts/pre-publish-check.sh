#!/usr/bin/env bash
set -euo pipefail

# Pre-publish validation script
# NOTE: This script ONLY validates - it does NOT regenerate documentation
# For doc regeneration, use: npm run regen-docs (manual only)

echo "🔎 Node/npm:"
node -v || true
npm -v || true

echo "📦 Install deps"
npm ci

echo "🔤 Typecheck"
npm run typecheck

echo "🧹 Lint"
npm run lint

echo "🏗️ Build"
npm run build

echo "🧪 Install Playwright browsers"
npx playwright install chromium webkit

echo "🧭 E2E"
npm run test:e2e

echo "✅ All validation checks passed!"
