.PHONY: export-diagrams
export-diagrams:
	@docker-compose run --rm plantuml /usr/docs/assets/diagrams/*.puml

.PHONY: serve
serve:
	@uvicorn src.app:app --host=0.0.0.0 --port=8000 --reload

.PHONY: makemigrations
makemigrations:
	@alembic revision --autogenerate -m "$(message)"

.PHONY: migrate
migrate:
	@alembic upgrade head

.PHONY: test
test:
	@pytest -vv