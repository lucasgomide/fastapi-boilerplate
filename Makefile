run-server:
	@poetry run uvicorn app.main:app --reload --workers 1 --host 0.0.0.0

test:
	poetry run pytest -s 

style:
	poetry run ruff check --fix
	poetry run ruff format
