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

def test_create_user(client):
    user_data = {
        "username": "testuser1",
        "email": "testuser1@example.com",
        "full_name": "Test User1",
        "password": "password123"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    assert response.json()["username"] == user_data["username"]
    assert response.json()["email"] == user_data["email"]
    assert response.json()["full_name"] == user_data["full_name"]

def test_get_user(client):
    db = Session(bind=engine)
    user_data = {
        "username": "testuser2",
        "email": "testuser2@example.com",
        "full_name": "Test User2",
        "password": "password123"
    }
    user = models.User(**user_data)
    db.add(user)
    db.commit()

    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200
    assert response.json()["username"] == user_data["username"]
    assert response.json()["email"] == user_data["email"]
    assert response.json()["full_name"] == user_data["full_name"]

def test_update_user(client):
    db = Session(bind=engine)
    user_data = {
        "username": "testuser3",
        "email": "testuser3@example.com",
        "full_name": "Test User3",
        "password": "password123"
    }
    user = models.User(**user_data)
    db.add(user)
    db.commit()

    new_user_data = {
        "username": "updatedtestuser3",
        "email": "updatedtestuser3@example.com",
        "full_name": "Updated Test User3",
        "password": "password456"
    }
    response = client.put(f"/users/{user.id}", json=new_user_data)
    assert response.status_code == 200
    assert response.json()["username"] == new_user_data["username"]
    assert response.json()["email"] == new_user_data["email"]
    assert response.json()["full_name"] == new_user_data["full_name"]

def test_delete_user(client: TestClient):
    user = {"email": "testuser@example.com", "password": "testpassword", "full_name": "Test User"}
    response = client.post("/users/", json=user)
    assert response.status_code == 201
    created_user = response.json()

    response = client.delete(f"/users/{created_user['id']}/")
    assert response.status_code == 200

    response = client.get(f"/users/{created_user['id']}/")
    assert response.status_code == 404

