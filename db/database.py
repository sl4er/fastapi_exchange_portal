from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from core.config import settings


engine = create_async_engine(url=settings.DATABASE_URL)

Base = declarative_base()
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_db_session():
    async with async_session() as session:
        yield session


async def create_tables(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
class Base(DeclarativeBase):
    pass