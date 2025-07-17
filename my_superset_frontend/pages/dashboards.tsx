import { useEffect, useState } from 'react';
import api from '../lib/api';

interface Dashboard {
  id: number;
  title: string;
  layout: string;
}

export default function Dashboards() {
  const [dashboards, setDashboards] = useState<Dashboard[]>([]);

  useEffect(() => {
    api.get('/api/v1/dashboards').then(r => setDashboards(r.data.items || []));
  }, []);

  return (
    <main style={{ padding: '1rem' }}>
      <h1>Dashboards</h1>
      <ul>
        {dashboards.map(db => (
          <li key={db.id}>{db.title}</li>
        ))}
      </ul>
    </main>
  );
}
