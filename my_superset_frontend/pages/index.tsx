import Link from 'next/link';

export default function Home() {
  return (
    <main style={{ padding: '1rem' }}>
      <h1>My Superset Frontend</h1>
      <ul>
        <li><Link href="/datasets">Datasets</Link></li>
        <li><Link href="/charts">Charts</Link></li>
        <li><Link href="/dashboards">Dashboards</Link></li>
        <li><Link href="/sql-lab">SQL Lab</Link></li>
      </ul>
    </main>
  );
}
