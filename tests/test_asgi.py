# -*- coding: utf-8 -*-
"""Tests for asgi.py"""
from starlite.status_codes import HTTP_200_OK
from starlite.testing import TestClient

from app import asgi


def test_index() -> None:
    """Test the index page"""
    with TestClient(app=asgi.app) as client:
        response = client.get("/")
        assert response.status_code == HTTP_200_OK
        assert "Lorem ipsum" in response.text


def test_ping_pong() -> None:
    """Test the basic ping-pong endpoint"""
    with TestClient(app=asgi.app) as client:
        response = client.get("/ping")
        assert response.status_code == HTTP_200_OK
        assert response.json() == {"ping": "pong"}
