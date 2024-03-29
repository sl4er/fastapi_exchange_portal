from core.config import settings
import aiohttp


class ApiExchangeConnector:
    API_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={settings.EXCHANGE_KEY}"

    @staticmethod
    async def get_list_of_currencies():
        async with aiohttp.ClientSession() as session:
            async with session.get(ApiExchangeConnector.API_URL) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get("data")

    @staticmethod
    async def get_exchange_pair(first_valute: str, second_valute: str):
        api_url = f"{ApiExchangeConnector.API_URL}&base_currency={first_valute}&currencies={second_valute}"
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get("data").get(second_valute)
    
