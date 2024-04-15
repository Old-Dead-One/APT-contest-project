from fastapi import FastAPI
import uuid4

from models.contests import Contests
from models.players import Players

app = FastAPI()

contests: dict[uuid.UUID, Contests] = {}
players: dict[uuid.UUID, Players] = {}

# Contests endpoints
@app.get("contests/")
async def get_contests():
    return contests

@app.post("/contests/")
async def create_contest(contest: Contests):
    contests.append(contest)
    return contest

@app.put("/contests/{contest_id}")
async def update_contest(contest_id: int, contest: Contests):
    contests[contest_id] = contest
    return contest

@app.delete("/contests/{contest_id}")
async def delete_contest(contest_id: int):
    contests.pop(contest_id)
    return {"message": "Contest deleted successfully"}

# Players endpoints
@app.get("/players/")
async def get_players():
    return players

@app.post("/players/")
async def create_player(player: Players):
    players.append(player)
    return player

@app.put("/players/{player_id}")
async def update_player(player_id: int, player: Players):
    players[player_id] = player
    return player

@app.delete("/players/{player_id}")
async def delete_player(player_id: int):
    players.pop(player_id)
    return {"message": "Player deleted successfully"}
