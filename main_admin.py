from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select
from database import get_db
from models import Chapter, Event, Contest, Player

app = FastAPI()

# Chapter CRUD operations

@app.get("/chapters/", response_model=list[Chapter])
async def get_chapters(db: Session = Depends(get_db)) -> list[Chapter]:
    return db.exec(select(Chapter.chapter_id, Chapter.name, Chapter.location)).all()

@app.get("/chapters/{chapter_id}", response_model=list[Chapter])
async def get_chapter_by_id(chapter_id: int, db: Session = Depends(get_db)) -> list[Chapter]:
    chapter = db.exec(select(Chapter).where(Chapter.chapter_id == chapter_id)).all()
    return chapter

@app.post("/chapters/", response_model=Chapter)
async def create_chapter(chapter: Chapter, db: Session = Depends(get_db)) -> Chapter:
    existing_chapter = db.exec(select(Chapter).where(Chapter.name == chapter.name)).first()
    if existing_chapter:
        raise HTTPException(status_code=400, detail="Chapter already exists")
    db.add(chapter)
    db.commit()
    return chapter

@app.put("/chapters/{chapter_id}", response_model=Chapter)
async def update_chapter(chapter_id: int, chapter: Chapter, db: Session = Depends(get_db)) -> Chapter:
    db_chapter = db.get(Chapter, chapter_id)
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    db_chapter.name = chapter.name
    db_chapter.location = chapter.location
    db.commit()
    return db_chapter

@app.delete("/chapters/{chapter_id}")
async def delete_chapter(chapter_id: int, db: Session = Depends(get_db)) -> None:
    db_chapter = db.get(Chapter, chapter_id)
    if db_chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    db.delete(db_chapter)
    db.commit()

# Event CRUD operations

@app.get("/events/", response_model=list[Event])
async def get_events(db: Session = Depends(get_db)) -> list[Event]:
    return db.exec(select(Event)).all()

@app.get("/events/{event_id}", response_model=list[Event])
async def get_events_by_event_id(event_id: int, db: Session = Depends(get_db)) -> list[Event]:
    events = db.exec(select(Event).where(Event.event_id == event_id)).all()
    return events

# Get events by chapter
@app.get("/events/chapter/{chapter_id}", response_model=list[Event])
async def get_events_by_chapter(chapter_id: int, db: Session = Depends(get_db)) -> list[Event]:
    events = db.exec(select(Event).where(Event.chapter_id == chapter_id)).all()
    return events

@app.post("/events/", response_model=Event)
async def create_event(event: Event, db: Session = Depends(get_db)) -> Event:
    existing_event = db.exec(select(Event).where(Event.name == event.name)).first()
    if existing_event:
        raise HTTPException(status_code=400, detail="Event already exists")
    db.add(event)
    db.commit()
    return event

@app.put("/events/{event_id}", response_model=Event)
async def update_event(event_id: int, event: Event, db: Session = Depends(get_db)) -> Event:
    db_event = db.get(Event, event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    db_event.name = event.name
    db_event.course = event.course
    db_event.date = event.date
    db.commit()
    return db_event

@app.delete("/events/{event_id}")
async def delete_event(event_id: int, db: Session = Depends(get_db)) -> None:
    db_event = db.get(Event, event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()

# Contest CRUD operations

# Get contest by events
@app.get("/contests/event/{event_id}", response_model=list[Contest])
async def get_contests_by_event(event_id: int, db: Session = Depends(get_db)) -> list[Contest]:
    contests = db.exec(select(Contest).where(Contest.event_id == event_id)).all()
    return contests

@app.post("/contests/", response_model=Contest)
async def create_contest(contest: Contest, db: Session = Depends(get_db)) -> Contest:
    existing_contest = db.exec(select(Contest).where(Contest.name == contest.name)).first()
    if existing_contest:
        raise HTTPException(status_code=400, detail="Contest already exists")
    db.add(contest)
    db.commit()
    return contest

@app.put("/contests/{contest_id}", response_model=Contest)
async def update_contest(contest_id: int, contest: Contest, db: Session = Depends(get_db)) -> Contest:
    db_contest = db.get(Contest, contest_id)
    if db_contest is None:
        raise HTTPException(status_code=404, detail="Contest not found")
    db_contest.name = contest.name
    db_contest.cost = contest.cost
    db.commit()
    return db_contest

@app.delete("/contests/{contest_id}", response_model=None)
async def delete_contest(contest_id: int, db: Session = Depends(get_db)) -> None:
    db_contest = db.get(Contest, contest_id)
    if db_contest is None:
        raise HTTPException(status_code=404, detail="Contest not found")
    db.delete(db_contest)
    db.commit()

# Player CRUD operations

@app.get("/players/", response_model=list[Player])
async def get_players(db: Session = Depends(get_db)) -> list[Player]:
    return db.exec(select(Player)).all()

# Get players by chapter
@app.get("/players/chapter/{chapter_id}", response_model=list[Player])
async def get_players_by_chapter(chapter_id: int, db: Session = Depends(get_db)) -> list[Player]:
    players = db.exec(select(Player).where(Player.home_chapter_id == chapter_id)).all()
    if not players:
        raise HTTPException(status_code=404, detail="No chapter with that player found")
    return players

@app.post("/players/", response_model=Player)
async def create_player(player: Player, db: Session = Depends(get_db)) -> Player:
    existing_player = db.exec(select(Player).where(Player.email == player.email)).first()
    if existing_player:
        raise HTTPException(status_code=400, detail="Player already exists")
    db.add(player)
    db.commit()
    return player

@app.put("/players/{player_id}", response_model=Player)
async def update_player(player_id: int, player: Player, db: Session = Depends(get_db)) -> Player:
    db_player = db.get(Player, player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    db_player.first_name = player.first_name
    db_player.last_name = player.last_name
    db_player.venmo_id = player.venmo_id
    db_player.email = player.email
    db.commit()
    return db_player

@app.delete("/players/{player_id}")
async def delete_player(player_id: int, db: Session = Depends(get_db)) -> None:
    db_player = db.get(Player, player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    db.delete(db_player)
    db.commit()