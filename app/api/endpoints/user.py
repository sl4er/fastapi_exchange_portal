from fastapi import APIRouter, Depends
from app.api.schemas.user import User, UserOut
from app.core.security import create_token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.hash import Hash
from app.db.database import get_async_db_session
from app.core.exceptions import (
    InvalidLoginException,
    InvalidPasswordException,
)
from app.repositories.exchange_repo import ExchangeRepository, SqlAlchemyExchangeRepository

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

async def get_exchange_repository(session: AsyncSession = Depends(get_async_db_session)) -> ExchangeRepository:
    return SqlAlchemyExchangeRepository(session)


@auth_router.post("/register", response_model=UserOut)
async def create_user(reg_user: User, repo: ExchangeRepository = Depends(get_exchange_repository)):
    return await repo.create_user(reg_user)


@auth_router.post("/login")
async def get_token(request: OAuth2PasswordRequestForm = Depends(), repo: ExchangeRepository = Depends(get_exchange_repository)):
    user = await repo.get_user_by_name(request.username)
    
    if not user:
        raise InvalidLoginException
    if not await Hash.verify(user.password, request.password):
        raise InvalidPasswordException
    
    access_token = await create_token(data={"sub": user.name})
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_name" : user.name
    }

