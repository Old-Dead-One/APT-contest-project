from sqlmodel import SQLModel, Field, Relationship
from datetime import date


class Chapter(SQLModel, table=True):
    chapter_id: int = Field(primary_key=True)
    name: str
    location: str
    players: list["Player"] = Relationship(back_populates="chapter")
    events: list["Event"] = Relationship(back_populates="chapter")

class Event(SQLModel, table=True):
    event_id: int = Field(primary_key=True)
    name: str
    course: str
    date: date
    chapter_id: int = Field(foreign_key="chapter.chapter_id")
    chapter: Chapter = Relationship(back_populates="events")
    players: list["PlayerEventLink"] = Relationship(back_populates="event")

class PlayerEventLink(SQLModel, table=True):
    player_id: int = Field(foreign_key="player.player_id", primary_key=True)
    event_id: int = Field(foreign_key="event.event_id", primary_key=True) 

class Player(SQLModel, table=True):
    player_id: int = Field(primary_key=True)
    division: int
    first_name: str
    last_name: str
    venmo_id: str
    email: str
    home_chapter_id:int = Field(foreign_key="chapter.chapter_id")
    chapter: Chapter = Relationship(back_populates="players")
    events: list["PlayerEventLink"] = Relationship(back_populates="player")

class Contest(SQLModel, table=True):
    contest_id: int = Field(primary_key=True)
    name: str 
    cost: float
    event_id: int = Field(foreign_key="event.event_id")
    event: Event = Relationship(back_populates="contests")

class PlayerCart(SQLModel, table=True):
    player_id: int = Field(foreign_key="player.player_id", primary_key=True)
    chapter_id: int = Field(foreign_key="chapter.chapter_id", primary_key=True)
    event_id: int = Field(foreign_key="event.event_id", primary_key=True)
    contest_id: int = Field(foreign_key="contest.contest_id", primary_key=True)
