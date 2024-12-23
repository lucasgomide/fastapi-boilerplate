
# FastAPI Boilerplate

This project serves as a boilerplate for building web applications using FastAPI, a modern, fast (high-performance) web framework for Python.

## Features

- **FastAPI**: Leverages FastAPI for building APIs quickly with automatic interactive documentation.
- **SQLAlchemy**: Utilizes SQLAlchemy for ORM (Object Relational Mapping) to interact with the database.
- **Alembic**: Includes Alembic for database migrations.
- **Poetry**: Manages dependencies and virtual environments using Poetry.
- **Testing**: Configured with pytest for writing and running tests.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.13
- Poetry

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/lucasgomide/fastapi-boilerplate.git
   cd fastapi-boilerplate
   ```

2. **Install dependencies**:

   ```bash
   poetry install
   ```

3. **Set up the database**:

   - You can either configure your database settings in `alembic.ini` or set a default value inf Setting() class
   - Run migrations:

     ```bash
     make migrate
     ```

4. **Run the application**:

   ```bash
   make run-server
   ```

   Access the application at `http://127.0.0.1:8000`.

## Project Structure

```plaintext
fastapi-boilerplate/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   ├── routers/
│   └── schemas/
├── migrations/
├── tests/
├── alembic.ini
├── pyproject.toml
└── README.md
```

- `app/`: Contains the main application code.
  - `models/`: Database models.
  - `routers/`: API route definitions.
  - `schemas/`: Pydantic models for request and response validation.
- `migrations/`: Database migration scripts managed by Alembic.
- `tests/`: Test cases for the application.

## Running Tests

Execute the following command to run tests: (make sure your database connection was properly set)

```bash
make test
```