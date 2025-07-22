from data.fetcher import fetch_crypto_data

def test_fetch_crypto_data():
    data = fetch_crypto_data('bitcoin', '1')
    assert 'prices' in data
