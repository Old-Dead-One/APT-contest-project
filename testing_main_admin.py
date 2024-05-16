import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, create_engine
from sqlmodel.pool import StaticPool
from main_admin import app

# Create a test database in memory
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool)

# Create a fixture for the database session
@pytest.fixture(scope="function")
def db():
    with Session(engine) as session:
        yield session

# Create a fixture for the test client
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client

# Test get_chapters endpoint
def test_get_chapters(db, client):
    chapter_data = {"chapter_id": 1, "name": "Test Chapter", "location": "Test Location"}
    create_response = client.post("/chapters/", json=chapter_data)
    assert create_response.status_code == 200
    response = client.get("/chapters/")
    assert response.status_code == 200
    chapters = response.json()
    assert {"chapter_id": 1, "name": "Test Chapter", "location": "Test Location"} in chapters

# Test create_chapter endpoint
def test_create_chapter(db, client):
    chapter_data = {"chapter_id": 2, "name": "Test Chapter2", "location": "Test Location2"}
    create_response = client.post("/chapters/", json=chapter_data)
    assert create_response.status_code == 200
    response = client.get("/chapters/")
    assert response.status_code == 200
    chapters = response.json()
    assert {"chapter_id": 2, "name": "Test Chapter2", "location": "Test Location2"} in chapters

# Test update_chapter endpoint
def test_update_chapter(db, client):
    # Retrieve chapter
    chapter_id = 1
    get_response = client.get(f"/chapters/{chapter_id}")
    assert get_response.status_code == 200
    chapter_id = get_response.json()
    # Update chapter
    update_chapter_data = {"name": "Updated Test Chapter", "location": "Updated Test Location"}
    update_response = client.put(f"/chapter/{chapter_id}", json=update_chapter_data)
    assert update_response.status_code == 200
    # Retrieve updated chapter
    updated_get_response = client.get(f"/chapters/{chapter_id}")
    assert updated_get_response.status_code == 200
    chapter_id = get_response.json()
    # Check updated chapter data
    assert update_chapter_data["name"] == "Updated Test Chapter"
    assert update_chapter_data["location"] == "Updated Test Location"