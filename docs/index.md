# Starlite Barebones Template
A production-ready, minimal template for the [Starlite API Framework](https://github.com/starlite-api/starlite)

## Starlite Upstream Status
[![PyPI version](https://badge.fury.io/py/starlite.svg)](https://badge.fury.io/py/starlite)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/starlite-api/starlite/publish.yaml)](https://img.shields.io/github/actions/workflow/status/starlite-api/starlite/publish.yaml)



> Key:
>
> - [x] = Included
>
> - [ ] = Not Included (Yet)
>
> If you don't see a specific package it probably means it is not planned (Want it? [Open an issue!](https://github.com/JacobCoffee/starlite-barebones-template/issues/new/choose))


## Features

- [x] [Starlite API Framework](https://starlite-api.github.io/starlite/) plus some extras:
    * [`uvicorn`](https://www.uvicorn.org/)
    * [`python-dotenv`](https://github.com/theskumar/python-dotenv)
    * [`structlog`](https://www.structlog.org/en/stable/)
    * [`TailwindCSS`](https://tailwindcss.com/)
- CI via GitHub Actions
    - [x] CI Testing
    - [x] Document Generation
- Development
  - [ ] `docker-compose` for local development
    - [ ] [GitHub Codespaces](https://github.com/features/codespaces) for local development
    - [x] `Makefile` with useful commands
    - [x] `pyproject.toml` for compatibility with both [pip](https://pip.pypa.io/en/stable/) and [poetry](https://python-poetry.org/docs/)
    - `pre-commit` hooks
        - [x] `ruff`, `pylint`, and `isort` configurations for compatibility with the [black](https://black.readthedocs.io/en/stable/) auto-formatter
        - [x] `ruff` for linting
        - [x] `black` for auto-formatting
        - [x] `isort` for import sorting
        - [x] `codespell` for spell checking
        - [x] `conventional-pre-commit` for commit message linting to enforce [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
        - [ ] `mypy` for static type checking
    - Testing and Coverage
        - [x] Test coverage reports are generated during every commit and pull request using [coverage](https://coverage.readthedocs.io/en/6.4.1/) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/). All reports are automatically uploaded and archived on [codecov.io](https://about.codecov.io/).
        - [x] `pytest` for unit testing and `mypy` for static type checking
        - [x] `pytest-asyncio` for testing asynchronous code
        - [x] `pytest-cov` for test coverage
    - Documentation Management
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
- Front End
  - [x] `tailwindcss` for beautiful CSS
  - [x] `Jinja2` for templating
