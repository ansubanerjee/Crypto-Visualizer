import requests as rq
import pandas as pd
from datetime import datetime

COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"

def get_current_price(coin, currency="usd"):
    url = f"{COINGECKO_BASE_URL}/simple/price"
    params = {
        'ids': coin,
        'vs_currencies': currency
    }
    try:
        response = rq.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data[coin][currency]
    except Exception as e:
        print("Error fetching current price:", e)
        return None

def get_historical_data(coin, currency="usd", days=30):
    url = f"{COINGECKO_BASE_URL}/coins/{coin}/market_chart"
    params = {
        'vs_currency': currency,
        'days': days,
        'interval': 'daily'
    }
    try:
        response = rq.get(url, params=params)
        response.raise_for_status()
        prices = response.json()['prices']
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df[['date', 'price']]
    except Exception as e:
        print("Error fetching historical data:", e)
        return pd.DataFrame()
