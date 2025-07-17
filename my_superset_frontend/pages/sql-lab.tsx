import { useState } from 'react';
import api from '../lib/api';

export default function SqlLab() {
  const [sql, setSql] = useState('');
  const [result, setResult] = useState<any>(null);
  const [jobId, setJobId] = useState<string | null>(null);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    const { data } = await api.post('/api/v1/queries', { sql });
    setJobId(data.id);
    poll(data.id);
  };

  const poll = async (id: string) => {
    const interval = setInterval(async () => {
      const { data } = await api.get(`/api/v1/queries/${id}`);
      if (data.status === 'finished') {
        clearInterval(interval);
        setResult(data.result);
      }
    }, 1000);
  };

  return (
    <main style={{ padding: '1rem' }}>
      <h1>SQL Lab</h1>
      <form onSubmit={submit}>
        <textarea rows={5} cols={60} value={sql} onChange={e => setSql(e.target.value)} />
        <div>
          <button type="submit">Run</button>
        </div>
      </form>
      {jobId && !result && <p>Running job {jobId}...</p>}
      {result && (
        <pre style={{ whiteSpace: 'pre-wrap' }}>{JSON.stringify(result, null, 2)}</pre>
      )}
    </main>
  );
}
