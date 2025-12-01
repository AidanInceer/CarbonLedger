# CarbonLedger

A Python project combining a Machine Learning engine (placeholder) with a Django web application for tracking carbon footprint transactions.

## Project Structure

- **`src/ml_project/`**: Lightweight ML engine (placeholder for future development)
- **`src/web_app/`**: Django web application for transaction tracking
- **`tests/`**: Unit tests
- **`data/`**: Data files (ignored by git)
- **`models/`**: Trained models (ignored by git)
- **`notebooks/`**: Jupyter notebooks

## Setup

### 1. Install `uv`
```bash
pip install uv
```

### 2. Install dependencies
```bash
uv sync
```

### 3. Set up the database (Django)
```bash
cd src/web_app
uv run python manage.py migrate
```

### 4. Load sample data
```bash
uv run python manage.py loaddata sample_data
```

This loads 10 sample transactions across different categories (beverages, food, merchandise).

### 5. Run the Django server
```bash
uv run python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## Running the ML Engine

```bash
uv run python src/ml_project/main.py
```

## Testing

```bash
uv run pytest
```

## Linting

```bash
uv run ruff check .
uv run ruff check . --fix  # Auto-fix issues
```
