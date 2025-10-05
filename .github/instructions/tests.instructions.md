---
applyTo: "src/**/*.test.ts*"
---

# Unit/Component Tests — Rules

- Use Vitest + @testing-library/react
- No network: mock `src/services/*`
- Assert roles/labels; avoid brittle selectors
- One behavior per test; keep small and isolated

Example:
```ts
import { render, screen } from "@testing-library/react";
import { ProposalCard } from "../components/ProposalCard";
import userEvent from "@testing-library/user-event";

it("calls onVote", async () => {
  const onVote = vi.fn();
  render(<ProposalCard id="p1" title="Test" createdAtISO="2025-10-02T00:00:00Z" tally={{approve:0,reject:0,abstain:0}} needsVote onVote={onVote}/>);
  await userEvent.click(screen.getByRole('button', {name:/approve/i}));
  expect(onVote).toHaveBeenCalledWith("approve");
});
```
