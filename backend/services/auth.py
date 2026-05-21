from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(username: str, password: str):
    hashed_password = pwd_context.hash(password)
    user = User(username=username, password=hashed_password)
    # Add user to the database (session.add(user), session.commit() etc.)
    return {"message": "User registered successfully."}

def authenticate_user(username: str, password: str):
    # Fetch user from the database and verify password
    return "some_jwt_token"  # Return a JWT token