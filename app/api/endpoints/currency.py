from fastapi import APIRouter, Depends

from app.api.schemas.currency import Currency, CurrencyOut
from app.core.security import get_current_user
from app.core.exceptions import EmptyCurrencyListException, ExchangeCurrencyListException
from app.utils.external_api import ApiExchangeConnector as exchange_connector


currency_router = APIRouter(
    prefix="/currency",
    tags=["currency"]
)

@currency_router.post("/exchange", status_code=200, response_model=CurrencyOut)
async def get_currency_exchange(currency: Currency, token:str = Depends(get_current_user)):
    course = await exchange_connector.get_exchange_pair(currency.first_valute, currency.second_valute)
    
    if course:
        result = currency.volume * course
        return CurrencyOut(**currency.model_dump(), result=result)
    
    raise ExchangeCurrencyListException

@currency_router.get("/list", status_code=200)
async def get_currency_list(token:str = Depends(get_current_user)) -> list[str]:
    valutes = await exchange_connector.get_list_of_currencies()
    
    if valutes:
        return list(valutes.keys())

    raise EmptyCurrencyListException