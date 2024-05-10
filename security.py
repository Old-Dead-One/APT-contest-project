from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import uuid
from passlib.context import CryptContext
from models import Player
import re

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def validate_password(password: str) -> bool:
    # Password must be at least 10 characters long
    if len(password) < 10:
        return False
    
    # Password must contain at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    
    # Password must contain at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    
    # Password must contain at least one digit
    if not re.search(r"\d", password):
        return False
    
    # Password must contain at least one common special character
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;\"'<>,.?/\\]", password):
        return False
    
    return True

def generate_password_reset_token() -> str:
    return str(uuid.uuid4())

def send_password_reset_email(email: str, token: str):
    # Logic to send an email containing the password reset link with the token
    pass

def reset_password(email: str, new_password: str, token: str, db: Session = None) -> None:
    if not validate_password(new_password):
        raise HTTPException(status_code=400, detail="Password does not meet requirements")

    player = db.query(Player).filter(Player.email == email, Player.password_reset_token == token).first()
    if not player or player.password_reset_token_expiration < datetime.now():
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    player.password = new_password
    player.password_reset_token = None
    player.password_reset_token_expiration = None
    player.hash_password()  # Hash the new password
    db.commit()

