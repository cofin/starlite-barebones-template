# -*- coding: utf-8 -*-
"""Basic application for Starlite ASGI Framework"""
from starlite import Starlite, get


@get("/")
def hello_world() -> dict[str, str]:
    """A simple hello world endpoint."""
    return {"hello": "world"}


app = Starlite(route_handlers=[hello_world])
