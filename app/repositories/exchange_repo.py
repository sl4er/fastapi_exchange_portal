from abc import ABC, abstractmethod
from sqlalchemy.exc import IntegrityError

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.user import User
from app.core.exceptions import RegistrationException
from app.core.hash import Hash
from app.db.models import DbUser


class ExchangeRepository(ABC):
    @abstractmethod
    async def create_user(self) -> DbUser:
        pass
    
    @abstractmethod
    async def get_user_by_name(self) -> DbUser:
        pass


class SqlAlchemyExchangeRepository(ExchangeRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, reg_user: User) -> DbUser:
        new_user = DbUser(
            name=reg_user.name,
            password=await Hash.bcrypt(reg_user.password),
            email=reg_user.email,
        )

        try:
            self.session.add(new_user)
            await self.session.commit()
            await self.session.refresh(new_user)
        except IntegrityError:
            await self.session.rollback()
            raise RegistrationException

        return new_user


    async def get_user_by_name(self, username) -> DbUser | None:
        user = await self.session.execute(select(DbUser).filter(DbUser.name == username))
        user = user.scalar_one_or_none()
        return user
