PORT ?= 8000

install:
	poetry install

lint:
	poetry run flake8

test:
	poetry run pytest -vv tests

check: test lint

run:
	poetry run flask --app main --debug run --port 8000