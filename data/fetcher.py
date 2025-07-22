import requests
from config import settings

def fetch_crypto_data(crypto='bitcoin', period='30d'):
    url = f"{settings.DATA_SOURCE}/coins/{crypto}/market_chart"
    params = {'vs_currency': 'usd', 'days': period}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
