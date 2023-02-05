# Starlite Barebones Template
A production-ready, minimal template for the [Starlite API Framework](https://github.com/starlite-api/starlite)

## Starlite Upstream Status
[![PyPI version](https://badge.fury.io/py/starlite.svg)](https://badge.fury.io/py/starlite)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/starlite-api/starlite/publish.yaml)](https://img.shields.io/github/actions/workflow/status/starlite-api/starlite/publish.yaml)

## Features

> Key: [x] = Included, [ ] = Not Included (Yet), Unlisted = Not Planned (Want it? Open an issue!)

- [x] Starlite API Framework plus some extras:
    - [x] `uvicorn`
    - [x] `python-dotenv`
    - [x] `structlog`
    - [x] `msgspec`
    - [x] `pydantic`
- [x] GitHub Actions
    - [x] CI Testing
    - [x] Document Generation
- [x] `Makefile` with useful commands
- [x] `pyproject.toml` for compatibility with both [pip](https://pip.pypa.io/en/stable/) and [poetry](https://python-poetry.org/docs/)
- [x] `pre-commit` hooks
    - [x] `ruff`, `pylint`, and `isort` configurations for compatibility with the [black](https://black.readthedocs.io/en/stable/) auto-formatter
    - [x] `ruff` for linting
    - [x] `black` for auto-formatting
    - [x] `isort` for import sorting
    - [x] `codespell` for spell checking
    - [x] `conventional-pre-commit` for commit message linting to enforce [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
    - [ ] `mypy` for static type checking
- [x] Testing and Coverage
    - [x] Test coverage reports are generated during every commit and pull request using [coverage](https://coverage.readthedocs.io/en/6.4.1/) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/). All reports are automatically uploaded and archived on [codecov.io](https://about.codecov.io/).
    - [x] `pytest` for unit testing and `mypy` for static type checking
    - [x] `pytest-asyncio` for testing asynchronous code
    - [x] `pytest-cov` for test coverage
- [x] Documentation Management
    - [x] `mkdocs` for documentation generation
    - [x] `mkdocs-material` for documentation theme
    - [x] `mkdocstrings` for documentation generation from docstrings
    - [x] `mkdocstrings-python` for documentation generation from Python docstrings
    - [x] Docs are automatically deployed to [GitHub Pages](https://docs.github.com/en/pages) during every release
- Release Management
    - [x] `bump2version` for automatic versioning
    - [x] `poetry` for dependency management
    - [ ] Package releases to [PyPI](https://pypi.org/) with dynamic versioning provided by [bump2version](https://github.com/c4urself/bump2version) begin automatically whenever a new tag is created in github.
    - [ ] Metadata and dependency information is stored in the pyproject.toml for compatibility with both [pip](https://pip.pypa.io/en/stable/) and [poetry](https://python-poetry.org/docs/).
