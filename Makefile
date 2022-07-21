.PHONY: export-diagrams
export-diagrams:
	@docker-compose run --rm plantuml /usr/docs/assets/diagrams/*.puml -o /usr/docs/assets/images
