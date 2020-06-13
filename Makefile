help:
	@echo "ci-test - run the Continuous Integration (CI) pipeline (check-only)"
	@echo "format - format Python code with isort/Black"
	@echo "lint - check style with flake8"
	@echo "mypy - run the static type checker"
	@echo "pytest - run the tests and measure the code coverage"
	@echo "test - run the code formatter, linter, type checker, tests and coverage"

.PHONY: ci-test
ci-test:
	poetry run isort --recursive --check-only ethnic_residential_dynamics tests
	poetry run black --check ethnic_residential_dynamics tests
	make lint
	make mypy
	make pytest

.PHONY: format
format:
	poetry run isort -rc ethnic_residential_dynamics tests
	poetry run black ethnic_residential_dynamics tests

.PHONY: lint
lint:
	poetry run flake8 ethnic_residential_dynamics tests

.PHONY: mypy
mypy:
	poetry run mypy ethnic_residential_dynamics tests

.PHONY: pytest
pytest:
	poetry run pytest

.PHONY: test
test: format lint mypy pytest
