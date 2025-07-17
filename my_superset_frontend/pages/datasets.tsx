import { useEffect, useState } from 'react';
import api from '../lib/api';

interface Dataset {
  id: number;
  name: string;
  database: string;
  is_virtual: boolean;
}

export default function Datasets() {
  const [datasets, setDatasets] = useState<Dataset[]>([]);

  useEffect(() => {
    api.get('/api/v1/datasets').then(r => setDatasets(r.data.items || []));
  }, []);

  return (
    <main style={{ padding: '1rem' }}>
      <h1>Datasets</h1>
      <ul>
        {datasets.map(ds => (
          <li key={ds.id}>{ds.name} - {ds.database} - {ds.is_virtual ? 'virtual' : 'physical'}</li>
        ))}
      </ul>
    </main>
  );
}
