.PHONY: test
test:
	python -m pytest

.PHONY: lint
lint:
	mypy
	black -v src/ tests/
