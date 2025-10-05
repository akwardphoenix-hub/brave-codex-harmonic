import { useEffect, useState } from 'react';
import { getProposals, Proposal } from './services/councilData';
import { writeAuditLocal } from './lib/audit';

function App() {
  const [proposals, setProposals] = useState<Proposal[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getProposals()
      .then((data) => {
        setProposals(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  const handleVote = (proposalId: string, vote: string) => {
    writeAuditLocal({
      actor: 'local-user',
      action: 'vote',
      refId: proposalId,
      meta: { vote },
    });
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <header className="mb-8">
        <h1 className="text-4xl font-bold">Masternode Council</h1>
        <p className="text-gray-400 mt-2">Harmonic governance in action</p>
      </header>
      <main>
        <section className="space-y-4">
          {proposals.map((proposal) => (
            <article
              key={proposal.id}
              className="border border-gray-700 rounded-lg p-6 bg-gray-800"
            >
              <h2 className="text-2xl font-semibold mb-2">{proposal.title}</h2>
              {proposal.description && (
                <p className="text-gray-300 mb-4">{proposal.description}</p>
              )}
              <div className="text-sm text-gray-500 mb-4">
                <p>Created: {new Date(proposal.createdAt).toLocaleString()}</p>
                {proposal.votingEndsAt && (
                  <p>Ends: {new Date(proposal.votingEndsAt).toLocaleString()}</p>
                )}
              </div>
              <div className="flex gap-2">
                <button
                  onClick={() => handleVote(proposal.id, 'approve')}
                  className="px-4 py-2 bg-green-600 hover:bg-green-700 rounded"
                >
                  ✅ Approve
                </button>
                <button
                  onClick={() => handleVote(proposal.id, 'reject')}
                  className="px-4 py-2 bg-red-600 hover:bg-red-700 rounded"
                >
                  ❌ Reject
                </button>
                <button
                  onClick={() => handleVote(proposal.id, 'abstain')}
                  className="px-4 py-2 bg-gray-600 hover:bg-gray-700 rounded"
                >
                  ⚪ Abstain
                </button>
              </div>
            </article>
          ))}
        </section>
      </main>
    </div>
  );
}

export default App;
