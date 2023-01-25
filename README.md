# [Starlite API Framework](https://github.com/starlite-api/starlite) Barebones Template

## WIP

#### Provides a basic template for a Starlite API Framework project including these options out-of-the-box:
- [x] Starlite API Framework
- [x] `uvicorn`
- [x] `python-dotenv`
- [x] `structlog`
- [x] `msgspec`
- [x] `pydantic`

#### Optional Extras:
- [redis](https://redis.io/) with `poetry install --with cache`
- [saq](https://github.com/tobymao/saq/) with `poetry install --with worker`
- [sqlalchemy](https://www.sqlalchemy.org/) , [asyncpg](https://magicstack.github.io/asyncpg/) with `poetry install --with db` 
- all extras with `poetry install --all-extras`

___

## Getting Started
1. Run `poetry install` (optionally, you can pass in addons listed above [Optional Extras](#optional-extras))
2. Run `uvicorn app.asgi:app --reload` to start the app.
___

## Documentation
All documentation is generated under the `/docs` folder

To run or build the docs locally, you need to first install the required dependencies:

`poetry install --with docs`

Then you can serve the documentation with `make docs-serve`, or (re)build them with `make docs`

___

## Contributing
To contribute to this project, please read the [contributing guidelines](CONTRIBUTING.md).
