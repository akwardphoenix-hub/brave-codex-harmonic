import { test, expect } from '@playwright/test';

test('app loads and shows proposals', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByText(/Masternode Council/i)).toBeVisible();
  // example: proposal titles from fixture
  await expect(page.getByText(/Harmonic Kernel/i)).toBeVisible();
});
