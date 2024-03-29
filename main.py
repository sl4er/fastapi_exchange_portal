from contextlib import asynccontextmanager
from fastapi import FastAPI


from app.api.endpoints import currency, user
from db.database import create_tables, engine


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await create_tables(engine)
#     yield


app = FastAPI()#lifespan=lifespan
app.include_router(user.auth_router)
app.include_router(currency.currency_router)
