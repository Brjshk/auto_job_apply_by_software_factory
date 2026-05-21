from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.auth import create_user, authenticate_user

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    password: str

@router.post('/api/register')
async def register(user: UserCreate):
    return create_user(user.username, user.password)

class UserLogin(BaseModel):
    username: str
    password: str

@router.post('/api/login')
async def login(user: UserLogin):
    token = authenticate_user(user.username, user.password)
    if not token:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"token": token}