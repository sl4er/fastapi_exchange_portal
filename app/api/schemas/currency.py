from enum import Enum
from pydantic import BaseModel, validator

from app.core.exceptions import SimilarCurrencyException


class CurrencyEnum(str, Enum):
    AUD = "AUD"
    BGN = "BGN"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CNY = "CNY"
    CZK = "CZK"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    HKD = "HKD"
    HRK = "HRK"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    ISK = "ISK"
    JPY = "JPY"
    KRW = "KRW"
    MXN = "MXN"
    MYR = "MYR"
    NOK = "NOK"
    NZD = "NZD"
    PHP = "PHP"
    PLN = "PLN"
    RON = "RON"
    RUB = "RUB"
    SEK = "SEK"
    SGD = "SGD"
    THB = "THB"
    TRY = "TRY"
    USD = "USD"
    ZAR = "ZAR"

    def __str__(self):
        return self.value


class Currency(BaseModel):
    first_valute: CurrencyEnum
    second_valute: CurrencyEnum
    volume: int = 1

    @validator("second_valute")
    def currency_must_be_different(cls, v, values):
        if v == values.get("first_valute"):
            raise SimilarCurrencyException
        return v
