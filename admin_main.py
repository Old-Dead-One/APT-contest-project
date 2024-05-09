from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select

from database import get_db
from models import Chapter, Event, Contest, Player, SQLModel

app = FastAPI()


# Chapter CRUD opperations

# Get all chapters
@app.get("/chapters/", response_model=list[Chapter])
async def get_chapters(db: Session = Depends(get_db)) -> list[Chapter]:
    return list(db.exec(select(Chapter)).all())

# Create a new chapter
@app.post("/chapters", response_model=Chapter)
async def create_chapter(chapter: Chapter, db: Session = Depends(get_db)) -> Chapter:
    existing_chapter = db.exec(select(Chapter).where(Chapter.name == chapter.name)).first()
    if existing_chapter:
        raise HTTPException(status_code=400, detail="Chapter already exists")
    db.add(chapter)
    db.commit()
    return chapter

# Update an existing chapter
@app.put("/chapters/{chapter_id}", response_model=Chapter)
async def update_chapter(chapter_id: int, chapter: Chapter, db: Session = Depends(get_db)) -> Chapter:
    db_chapter = db.get(Chapter, chapter_id)
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    db_chapter.name = chapter.name
    db_chapter.location = chapter.location
    db.commit()
    return db_chapter

# Delete a chapter
@app.delete("/chapters/{chapter_id}", response_model=None)
async def delete_chapter(chapter_id: int, db: Session = Depends(get_db)) -> None:
    db_chapter = db.get(Chapter, chapter_id)
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    db.delete(db_chapter)
    db.commit()

# CRUD opperations

# Get all events
@app.get("/events/")
async def get_events(db: Session = Depends(get_db)) -> list[Event]:
    return db.exec(select(Event)).all()

# Get events by chapter
@app.get("/events/")
async def get_events_by_chapter(chapter_id: int, db: Session = Depends(get_db)) -> list[Event]:
    events = db.exec(select(Event).where(Event.chapter_id == chapter_id)).all()
    return events

# Create an event
@app.post("/events", response_model=Event)
async def create_event(event: Event, db: Session = Depends(get_db)) -> Event:
    existing_event = db.exec(select(Event).where(Event.name == event.name)).first()
    if existing_event:
        raise HTTPException(status_code=400, detail="Event already exists")
    db.add(event)
    db.commit()
    return event

# Delete an event
@app.delete("/events/{event_id}", response_model=None)
async def delete_event(event_id: int, db: Session = Depends(get_db)) -> None:
    db_event = db.get(Event, event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()


@app.get("/contests/")
async def get_contests(db: Session = Depends(get_db)) -> list[Contest]:
    return db.exec(select(Contest)).all()

@app.get("/players/")
async def get_players(db: Session = Depends(get_db)) -> list[Player]:
    return db.exec(select(Player)).all()

