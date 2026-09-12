# Anzo

**Anzo** is a Django-based personal finance app for tracking expenses, income, budgets, savings, and financial insights.

## Features

* Income & expense tracking
* Custom categories
* Financial dashboard
* Budget management
* Savings goals
* Analytics & reports
* AI-powered insights

## Tech Stack

* **Backend:** Django + Python
* **Database:** SQLite
* **Frontend:** Django Templates
* **Package Manager:** uv

## Project Structure

```text
anzo/
├── anzo/          # Django project
├── finance/       # Finance application
├── manage.py
├── pyproject.toml
├── uv.lock
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/antas06/anzo.git
cd anzo
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Activate virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Development

Run the Django development server whenever you want to work on Anzo:

```bash
python manage.py runserver
```

---

**Anzo — Less clutter. More clarity.**
