import asyncio
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from app.core.config import settings
from app.core.exceptions import InvalidLoginException, JWTTokenErrorException, JWTTokenExpiredException, JWTUserValidationException
from app.db.database import get_async_db_session
from app.db.models import DbUser
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def create_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = await asyncio.to_thread(jwt.encode, to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_async_db_session)):
    try:
        payload = await asyncio.to_thread(jwt.decode, token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise JWTUserValidationException

    except jwt.ExpiredSignatureError:
        raise JWTTokenExpiredException
    except jwt.InvalidTokenError:
        raise JWTTokenErrorException
    
    user = await db.execute(select(DbUser).filter(DbUser.name == username))
    user = user.scalar_one_or_none()
    
    if user is None:
        raise InvalidLoginException
    
    return user   
    