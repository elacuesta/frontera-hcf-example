.PHONY: lint

lint:
	@python -m flake8 --exclude=.git,venv-* project
