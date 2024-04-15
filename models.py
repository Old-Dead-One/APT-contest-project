from pydantic import BaseModel
from enum import Enum
from uuid import UUID

from chapters import APT_Chapters


class Chapter(BaseModel):
    Chapter = APT_Chapters

class Contests(Enum):
    SENIOR_NET = "Senior Net"
    OPEN_NET = "Open Net"
    SUPER_SKINS = "Super Skins"
    DIVISION_SKINS = "Division Skins"
    UNDEFINED1 = "Undefined 1"
    UNDEFINED2 = "Undefined 2"
    UNDEFINED3 = "Undefined 3"

class Players(BaseModel):
    player_id: UUID
    first_name: str
    last_name: str
    venmo_id: str
    email: str
    contests_entered: list[Contests]
    total_due: int

