from os import getenv
import aiohttp
import httpx
import requests
from fastapi import HTTPException

APIKEY = getenv('API_KEY')

## sicrona
def sync_convert(from_currency: str, to_currency: str, price: float):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={APIKEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if "Realtime Currency Exchange Rate" not in data:
            raise HTTPException(status_code=400, detail="Realtime Currency Exchange Rate")

        exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        return {to_currency: price * exchange_rate}

    except Exception as e:
        raise HTTPException(status_code=400, detail="Something went wrong")



##Asicrona
async def async_convert(from_currency: str, to_currency: str, price: float):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={APIKEY}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        data = response.json()

        if "Realtime Currency Exchange Rate" not in data:
            raise HTTPException(status_code=400, detail="Realtime Currency Exchange Rate")

        exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        return {to_currency: price * exchange_rate}

    except Exception as e:
        raise HTTPException(status_code=400, detail="Something went wrong")