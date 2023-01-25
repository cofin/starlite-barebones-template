# -*- coding: utf-8 -*-
"""Tests for asgi.py"""
from starlite.status_codes import HTTP_200_OK
from starlite.testing import TestClient

from app import asgi


def test_asgi_hello_world() -> None:
    """Test the basic hello-world endpoint"""
    with TestClient(app=asgi.app) as client:
        response = client.get("/")
        assert response.status_code == HTTP_200_OK
        assert response.json() == {"hello": "world"}
