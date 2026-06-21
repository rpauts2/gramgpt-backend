from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import jwt
import hashlib

from app.config import settings
from app.database import get_db
from app.models.user import User

router = APIRouter()
security = HTTPBearer()

class TelegramAuth(BaseModel):
    init_data: str

class TokenResponse(BaseModel):
    token: str
    user_id: int
    username: str

def create_token(user_id: int) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

@router.post("/telegram", response_model=TokenResponse)
async def auth_telegram(data: TelegramAuth, db: AsyncSession = Depends(get_db)):
    try:
        from telegram import Update
        validated = tg.WebApp.initDataUnsafe
        user_id = validated.user.id
        username = validated.user.username or validated.user.first_name
    except Exception:
        user_id = int(hashlib.md5(data.init_data.encode()).hexdigest()[:8], 16) % 100000
        username = f"user_{user_id}"

    result = await db.execute(select(User).where(User.telegram_id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        user = User(telegram_id=user_id, username=username, created_at=datetime.utcnow())
        db.add(user)
        await db.commit()

    token = create_token(user_id)
    return TokenResponse(token=token, user_id=user_id, username=username)

@router.get("/me")
async def get_me(token: str = Depends(security), db: AsyncSession = Depends(get_db)):
    try:
        payload = jwt.decode(token.credentials, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = int(payload["sub"])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    result = await db.execute(select(User).where(User.telegram_id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"user_id": user.telegram_id, "username": user.username, "created_at": str(user.created_at)}
