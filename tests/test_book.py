from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.database import Base, engine
from app.main import app
from app import models

import pytest
import json
import random


@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as client:
        yield client
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


def test_create_book(client):
    book_data = {
        "title": "Test Book 1",
        "author": "Test Author 1",
        "description": "Test Description 1",
        "published_year": 2021
    }
    response = client.post("/books/", json=book_data)
    assert response.status_code == 201
    assert response.json()["title"] == book_data["title"]
    assert response.json()["author"] == book_data["author"]
    assert response.json()["description"] == book_data["description"]
    assert response.json()["published_year"] == book_data["published_year"]


def test_get_book(client):
    db = Session(bind=engine)
    book_data = {
        "title": "Test Book 2",
        "author": "Test Author 2",
        "description": "Test Description 2",
        "published_year": 2020
    }
    book = models.Book(**book_data)
    db.add(book)
    db.commit()

    response = client.get(f"/books/{book.id}")
    assert response.status_code == 200
    assert response.json()["title"] == book_data["title"]
    assert response.json()["author"] == book_data["author"]
    assert response.json()["description"] == book_data["description"]
    assert response.json()["published_year"] == book_data["published_year"]


def test_update_book(client):
    db = Session(bind=engine)
    book_data = {
        "title": "Test Book 3",
        "author": "Test Author 3",
        "description": "Test Description 3",
        "published_year": 2019
    }
    book = models.Book(**book_data)
    db.add(book)
    db.commit()

    new_book_data = {
        "title": "Updated Test Book 3",
        "author": "Updated Test Author 3",
        "description": "Updated Test Description 3",
        "published_year": 2018
    }
    response = client.put(f"/books/{book.id}", json=new_book_data)
    assert response.status_code == 200
    assert response.json()["title"] == new_book_data["title"]
    assert response.json()["author"] == new_book_data["author"]
    assert response.json()["description"] == new_book_data["description"]
    assert response.json()["published_year"] == new_book_data["published_year"]


def test_delete_book(client):
    # Создаем новую книгу
    book_data = {
        "title": "Test Book 4",
        "author": "Test Author 4",
        "description": "Test Description 4",
        "published_year": 2018
    }
    response = client.post("/books/", json=book_data)
    assert response.status_code == 201
    created_book = response.json()

    # Удаляем созданную книгу
    response = client.delete(f"/books/{created_book['id']}/")
    assert response.status_code == 200
