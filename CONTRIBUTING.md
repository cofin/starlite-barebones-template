# Guidelines

To contribute code changes or update the documentation, please follow these steps:

1. Fork the upstream repository and clone the fork locally.
2. Install [poetry](https://python-poetry.org/), and install the project's dependencies
   with `poetry install`.
3. Install [pre-commit](https://pre-commit.com/) and install the hooks by running `pre-commit install` in the
   repository's hook.
4. Make your changes. Commits should follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.
5. Create a pull request to the main repository with an explanation of your changes. Include the issue number if
   applicable using the `#` followed by the issue number (e.g. `Fixes #123`).
6. $$$

> !! Note: Contributions to this project should not introduce unneeded complexity. The goal of the project
> is to provide a simple, barebones template that can be easily understood.

## Code Contribution Guidelines

1. If you are adding or modifying existing code, please make sure to write tests for .
2. All functions and methods should be documented with a doc string.
3. Add/Update the documentation.

## Project Documentation

The documentation is located under the `/docs` folder

### Running the Docs Locally

To run or build the docs locally, you need to first install the required dependencies:

`poetry install --with docs`

Then you can serve the documentation with `make docs-serve`, or (re)build them with `make docs`

### Checking Test Coverage

You can check the unit test coverage by running: `make test`
