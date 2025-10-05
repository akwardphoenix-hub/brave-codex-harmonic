---
applyTo: "src/**/*.tsx"
---

# React Components — House Rules

- Use TypeScript FCs with explicit props.
- Prefer composition over inheritance; keep components small and pure.
- Accessibility: give interactive elements roles/aria-labels; form controls must have labels.
- Styling: Tailwind utility classes; keep layout in parent, logic in child.
- Side-effects: isolate in hooks; no fetch in render.

### Patterns
- Use `useEffect` with cleanups; no stale timers.
- Use `useMemo`/`useCallback` to prevent re-render storms on big lists.
- Error states obvious: show fallback, don't explode.

### Example
```tsx
type ProposalCardProps = {
  id: string; title: string; createdAtISO: string;
  tally: { approve: number; reject: number; abstain: number };
  needsVote: boolean;
  onVote: (v: "approve"|"reject"|"abstain") => void;
};
export function ProposalCard(p: ProposalCardProps) {
  const created = new Date(p.createdAtISO).toLocaleString();
  return (
    <section className={`rounded-md p-4 border ${p.needsVote?'border-amber-500':'border-zinc-800'}`}>
      <header className="flex items-center justify-between">
        <h3 className="font-semibold">{p.title}</h3>
        {p.needsVote && <span className="text-amber-500 text-xs">Vote needed</span>}
      </header>
      <p className="text-xs opacity-70">Created: {created}</p>
      <div className="mt-3 flex gap-2">
        <button onClick={()=>p.onVote("approve")} className="px-2 py-1 bg-green-600 rounded">✅ Approve</button>
        <button onClick={()=>p.onVote("reject")} className="px-2 py-1 bg-red-600 rounded">❌ Reject</button>
        <button onClick={()=>p.onVote("abstain")} className="px-2 py-1 bg-zinc-600 rounded">⚪ Abstain</button>
      </div>
    </section>
  );
}
```
