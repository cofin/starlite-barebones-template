# Installation Guide

This guide will walk you through the steps to install and run the project locally.
This project includes a `Makefile` with some useful commands (available by running `make help`)

## Prerequisites
- Python 3.8+
- Poetry
  - Install with `make install`

## Getting Started
- Run `poetry install`
- Run `uvicorn app.asgi:app --reload` to start the app.
