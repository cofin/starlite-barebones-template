# Workflow Guide

This guide will walk you through the workflow of the project.

## Prerequisites
- Python 3.8+
- Poetry
  - Install with `make install`
- `precommit` and other development dependencies
  - Run `poetry install --with dev`
  - Run `pre-commit install` to install the pre-commit hooks

## Development
- Make commands are available by running `make help`
  - Run `make install` to install the project in development mode
  - Run `make build` to build the project
  - Run `make test` to run the tests
  - Run `make coverage` to run the tests with coverage
  - Run `make lint` to run linting
  - Run `make pre-release` to run the pre-release cycle
  - Run `make upgrade` to upgrade all dependencies to the latest stable versions
- Change Lifecycle:
  - Create a new branch
  - Make and commit changes
  - The pre-commit hooks will run automatically
  - Push the changes to the remote branch
  - Create a pull request
  - The CI will run automatically
  - Merge the pull request after the CI passes and the PR is approved
  - Delete the branch

## Documentation
- Ensure you have the `docs` dependencies installed
  - Run `poetry install --with docs`
- Run `make docs` to build the docs or `make docs-serve` to build and serve them locally
- Run `make docs-clean` to clean the static doc files
- Run `make docs-serve` to serve the docs locally

## Production
- Run `make runtime-only` to install the project in production mode
- Run `make migrations` to run the migrations
- Run `make migrate` to migrate the database
- Run `make squash-migrations` to squash the migrations
- Run `make clean` to clean the project
- Run `make docs` to build the docs or `make docs-serve` to build and serve them locally
