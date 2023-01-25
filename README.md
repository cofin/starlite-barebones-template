# [Starlite API Framework](https://github.com/starlite-api/starlite) Barebones Template

## WIP

Provides a baasic template for a Starlite API Framework project including these options out-of-the-box:
- [x] Starlite API Framework
- [x] `uvicorn`
- [x] `python-dotenv`
- [x] `structlog`
- [x] `msgspec`
- [x] `pydantic`

Optional Extras:
- [redis](https://redis.io/) with `poetry install --with cache`
- [saq](https://github.com/tobymao/saq) with `poetry install --with worker`
- [sqlalchemy](https://www.sqlalchemy.org/) , [asyncpg](https://magicstack.github.io/asyncpg/) with `poetry install --with db` 
- all extras with `poetry install --all-extras`