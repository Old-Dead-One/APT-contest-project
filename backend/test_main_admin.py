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
def test_get_and_create_chapters(db, client):
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
    chapter_id = 2
    update_chapter_data = {"name": "Updated Test Chapter", "location": "Updated Test Location"}
    update_response = client.put(f"/chapters/{chapter_id}", json=update_chapter_data)
    assert update_response.status_code == 200
    updated_get_response = client.get(f"/chapters/{chapter_id}")
    assert updated_get_response.status_code == 200
    updated_chapter_data = updated_get_response.json()
    assert {"chapter_id": 2, "name": "Updated Test Chapter", "location": "Updated Test Location"} in updated_chapter_data

# Test delete_chapter endpoint
def test_delete_chapter(db, client):
    chapter_id = 1
    delete_response = client.delete(f"/chapters/{chapter_id}")
    assert delete_response.status_code == 200
    get_response = client.get(f"/chapters/{chapter_id}")
    assert get_response.status_code == 200

# Test post & get event endpoints
def test_get_and_create_events(db, client):
    event_data = {"event_id": 1, "name": "Test Event", "course": "Test Course", "date": "2024-05-16", "chapter_id": 2}
    create_response = client.post("/events/", json=event_data)
    assert create_response.status_code == 200
    response = client.get("/events/")
    assert response.status_code == 200
    events = response.json()
    assert {"event_id": 1, "name": "Test Event", "course": "Test Course", "date": "2024-05-16", "chapter_id": 2} in events

# Test post event endpoints
def test_create_events(db, client):
    event_data = {"event_id": 2, "name": "Test Event2", "course": "Test Course2", "date": "2024-05-12", "chapter_id": 2}
    create_response = client.post("/events/", json=event_data)
    assert create_response.status_code == 200
    response = client.get("/events/")
    assert response.status_code == 200
    events = response.json()
    assert {"event_id": 2, "name": "Test Event2", "course": "Test Course2", "date": "2024-05-12", "chapter_id": 2} in events

# Test put event endpoint
def test_update_event(db, client):
    event_id = 1
    update_event_data = {"name": "Updated Test Event", "course": "Updated Test Course", "date": "2024-05-30", "chapter_id": 2}
    update_response = client.put(f"/events/{event_id}", json=update_event_data)
    assert update_response.status_code == 200
    updated_get_response = client.get(f"/events/{event_id}")
    assert updated_get_response.status_code == 200
    updated_event_data = updated_get_response.json()
    assert {"event_id": 1, "name": "Updated Test Event", "course": "Updated Test Course", "date": "2024-05-30", "chapter_id": 2} in updated_event_data

# Test delete event endpoint
def test_delete_event(db, client):
    event_id = 1
    delete_response = client.delete(f"/events/{event_id}")
    assert delete_response.status_code == 200
    get_response = client.get(f"/events/{event_id}")
    assert get_response.status_code == 200

# Test post & get contest endpoints
def test_get_and_create_contests(db, client):
    contest_data = {"contest_id": 1, "name": "Test Contest", "cost": 20.00, "event_id": 2}
    create_response = client.post("/contests/", json=contest_data)
    assert create_response.status_code == 200
    response = client.get(f"/contests/event/{2}")
    assert response.status_code == 200
    contests = response.json()
    assert {"contest_id": 1, "name": "Test Contest", "cost": 20.00, "event_id": 2} in contests

# Test post_contest endpoints
def test_create_contests(db, client):
    contest_data = {"contest_id": 2, "name": "Test Contest2", "cost": 21.00, "event_id": 2}
    create_response = client.post("/contests/", json=contest_data)
    assert create_response.status_code == 200
    response = client.get(f"/contests/event/{2}")
    assert response.status_code == 200
    contests = response.json()
    assert {"contest_id": 2, "name": "Test Contest2", "cost": 21.00, "event_id": 2} in contests

def test_update_contests(db, client):
    contest_id = 2
    event_id = 2
    update_contest_data = {"name": "Updated Test Contest2", "cost": 20, "event_id": 2}
    update_response = client.put(f"/contests/{contest_id}", json=update_contest_data)
    assert update_response.status_code == 200
    updated_get_response = client.get(f"/contests/event/{event_id}")
    assert updated_get_response.status_code == 200
    updated_contest_data = updated_get_response.json()
    assert {"contest_id": 2, "name": "Updated Test Contest2", "cost": 20, "event_id": 2} in updated_contest_data

# Test delete_contest endpoint
def test_delete_contest(db, client):
    contest_id = 1
    delete_response = client.delete(f"/contests/{contest_id}")
    assert delete_response.status_code == 200
    get_response = client.get(f"/contests/event/{contest_id}")
    assert get_response.status_code == 200

# Test post & get player
def test_get_and_create_player(db, client):
    player_data = {"player_id": 1, "division": 4, "first_name": "Bo",
                   "last_name": "Diggidy", "venmo_id": "@bodiggidy",
                   "email": "bodiggidy@gmial.com", "home_chapter_id": 2}
    create_response = client.post("/players/", json=player_data)
    assert create_response.status_code == 200
    response = client.get("/players/")
    assert response.status_code == 200
    events = response.json()
    assert {"player_id": 1, "division": 4, "first_name": "Bo",
                   "last_name": "Diggidy", "venmo_id": "@bodiggidy",
                   "email": "bodiggidy@gmial.com", "home_chapter_id": 2} in events
    
# Test post & get player
def test_create_player(db, client):
    player_data = {"player_id": 2, "division": 4, "first_name": "Beau",
                   "last_name": "Diggity", "venmo_id": "@bodiggity",
                   "email": "bodiggity@gmial.com", "home_chapter_id": 2}
    create_response = client.post("/players/", json=player_data)
    assert create_response.status_code == 200
    response = client.get("/players/")
    assert response.status_code == 200
    events = response.json()
    assert {"player_id": 2, "division": 4, "first_name": "Beau",
            "last_name": "Diggity", "venmo_id": "@bodiggity",
            "email": "bodiggity@gmial.com", "home_chapter_id": 2} in events
    
# Test delete player    
def test_delete_player(db, client):
    player_id = 1
    chapter_id = 2
    delete_response = client.delete(f"/players/{player_id}")
    assert delete_response.status_code == 200
    get_response = client.get(f"/players/chapter/{chapter_id}")
    assert get_response.status_code == 200