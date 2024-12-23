run-server:
	@poetry run uvicorn app.main:app --reload --workers 1 --host 0.0.0.0

test:
	DATABASE_URL=postgresql://lucasgomide:@localhost:5432/database_test poetry run pytest -s 

style:
	poetry run ruff check --fix
	poetry run ruff format

generate_migrations:
	poetry run alembic revision --autogenerate

migrate:
	poetry run alembic upgrade head