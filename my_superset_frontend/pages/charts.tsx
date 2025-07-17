import { useEffect, useState } from 'react';
import api from '../lib/api';

interface Chart {
  id: number;
  name: string;
  chart_type: string;
}

export default function Charts() {
  const [charts, setCharts] = useState<Chart[]>([]);

  useEffect(() => {
    api.get('/api/v1/charts').then(r => setCharts(r.data.items || []));
  }, []);

  return (
    <main style={{ padding: '1rem' }}>
      <h1>Charts</h1>
      <ul>
        {charts.map(ch => (
          <li key={ch.id}>{ch.name} - {ch.chart_type}</li>
        ))}
      </ul>
    </main>
  );
}
