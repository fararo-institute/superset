# My Superset FastAPI

A modular FastAPI backend inspired by Apache Superset with a lightweight Next.js frontend.

## Development

### Backend

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Run the API
   ```bash
   uvicorn main:app --reload
   ```

### Frontend

1. Change to the frontend folder
   ```bash
   cd ../my_superset_frontend
   npm install
   ```
2. Copy `.env.local.example` to `.env.local` and adjust `NEXT_PUBLIC_API_URL` if needed
3. Start Next.js
   ```bash
   npm run dev
   ```

### Docker Compose

From the `my_superset_fastapi` folder run:

```bash
docker-compose up --build
```

This starts Postgres, Redis, the FastAPI API, Celery worker, and the Next.js frontend at `http://localhost:3000`.

The application expects environment variables defined in `.env` (see `.env.example`).

### Testing API calls

Use the frontend pages or interact with the API directly, for example:

```bash
curl http://localhost:8000/api/v1/datasets
```

### Troubleshooting

- **CORS or 401 errors**: ensure the backend URL in `.env.local` matches the running API and that the API is running.
- **Containers fail to start**: try `docker-compose build --no-cache`.
