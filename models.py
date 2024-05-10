from sqlmodel import SQLModel, Field, Relationship
from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
    date: datetime
    chapter_id: int = Field(foreign_key="Chapter.chapter_id")
    chapter: Chapter = Relationship(back_populates="events")
    player: list["Player"] = Relationship(back_populates="events", link_model="PlayerEventLink")

class PlayerEventLink(SQLModel, table=True):
    player_id: int = Field(foreign_key="player_id", primary_key=True)
    event_id: int = Field(foreign_key="event_id", primary_key=True) 

class Player(SQLModel, table=True):
    player_id: int = Field(primary_key=True)
    division: int
    is_admin: bool = Field(default=False)
    first_name: str
    last_name: str
    venmo_id: str
    email: str
    password: str  # Add password field
    home_chapter_id: int = Field(foreign_key="Chapter.chapter_id")
    chapter: Chapter = Relationship(back_populates="player")
    events: list[Event] = Relationship(back_populates="players", link_model="PlayerEventLink")

    # Add a method to hash the password
    def hash_password(self):
        self.password = pwd_context.hash(self.password)
