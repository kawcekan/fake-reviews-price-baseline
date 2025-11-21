# Fake Reviews Detection & Original Price Estimation

Building trust in online shopping.

## Features
- **Fake review detection:** NLP-driven trust scores and flags.
- **Price baseline estimation:** MSRP + historical blend with regime awareness.
- **Dashboard:** Plotly charts, review table, buy-window verdict.
- **API:** FastAPI endpoints for integration.
- **Infra:** PostgreSQL + Docker Compose for easy deploy.

## Quick start
1. **Clone:** `git clone <repo> && cd fake-reviews-price-baseline`
2. **Run:** `docker-compose up --build`
3. **Seed:** `docker-compose exec backend python -m app.seeds.seed_data`
4. **Open:** Frontend http://localhost:5173, API docs http://localhost:8000/docs

## Config
- **DB_URL:** Postgres connection string
- **MSRP_WEIGHT, HIST_WEIGHT:** Baseline blend weights
- **VITE_API_URL:** Frontend -> API endpoint

## License
MIT
