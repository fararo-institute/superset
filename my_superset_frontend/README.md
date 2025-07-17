# My Superset Frontend

A minimal Next.js frontend that connects to the FastAPI backend.

## Features

- List datasets, charts, and dashboards
- Submit SQL queries via SQL Lab page
- Simple JWT login using FastAPI Users

## Development

1. Install dependencies
   ```bash
   npm install
   ```
2. Copy `.env.local.example` to `.env.local` and set `NEXT_PUBLIC_API_URL`
3. Start the dev server
   ```bash
   npm run dev
   ```

The frontend expects the backend available at the URL specified in `NEXT_PUBLIC_API_URL` (default `http://localhost:8000`).

### Docker

A basic `Dockerfile` is provided. When using Docker Compose from the backend folder it will build the frontend service automatically.

### Testing the API

Use the pages under `/datasets`, `/charts`, `/dashboards`, and `/sql-lab` to interact with the backend. If you encounter CORS issues or a 401 error, check that the backend is running and the URL is correct.
