import { useState } from 'react';
import api from '../lib/api';
import { useRouter } from 'next/router';

export default function Login() {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    try {
      const { data } = await api.post('/auth/jwt/login', new URLSearchParams({
        username: email,
        password,
      }));
      localStorage.setItem('token', data.access_token);
      router.push('/');
    } catch (err) {
      setError('Invalid credentials');
    }
  };

  return (
    <main style={{ padding: '1rem' }}>
      <h1>Login</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={submit}>
        <div>
          <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
        </div>
        <div>
          <input placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} />
        </div>
        <button type="submit">Login</button>
      </form>
    </main>
  );
}
