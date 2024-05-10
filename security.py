from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import uuid
from passlib.context import CryptContext
from models import Player
import re

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def validate_password(password: str) -> bool:
    # Password must be at least 10 characters long and at most 65 characters long
    if len(password) < 10 or len(password) > 65:
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

# Generate password reset token
def generate_password_reset_token() -> str:
    return str(uuid.uuid4())

# Send password reset email
def send_password_reset_email(email: str, token: str):
    # Add email logic there must be some available library/template to use
    pass

# Reset password
def reset_password(email: str, new_password: str, expiration_minutes: int = 60, db: Session = None) -> None:
    if not validate_password(new_password):
        raise HTTPException(status_code=400, detail="Password does not meet requirements")

    player = db.query(Player).filter(Player.email == email).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")

    # Generate password reset token
    token = generate_password_reset_token()

    # Set password reset token and expiration time
    expiration_time = datetime.now() + timedelta(minutes=expiration_minutes)
    player.password_reset_token = token
    player.password_reset_token_expiration = expiration_time

    db.commit()
    # Send password reset email
    send_password_reset_email(email, token)
