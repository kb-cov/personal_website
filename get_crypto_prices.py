import requests

endpoint_list = [
    "https://api.coinbase.com/v2/prices/BTC-USD/spot",
    "https://api.coinbase.com/v2/prices/BTC-GBP/spot",
    "https://api.coinbase.com/v2/prices/ETH-GBP/spot",
    "https://api.coinbase.com/v2/prices/ADA-GBP/spot",
    "https://api.coinbase.com/v2/prices/DOGE-GBP/spot",
    "https://api.coinbase.com/v2/prices/XLM-GBP/spot",
    "https://api.coinbase.com/v2/prices/NEAR-GBP/spot",
    "https://api.coinbase.com/v2/prices/TRX-GBP/spot",
    "https://api.coinbase.com/v2/prices/SHIB-GBP/spot",
]

def get_crypto_data(endpoint_list):
    """
    Fetches cryptocurrency prices from the Coinbase API and prints them.
    The prices are formatted based on the currency type.
    """
    crypto_listings = []
    for endpoint in endpoint_list:
        response = requests.get(endpoint)
        data = response.json()
        crypto_listings.append(data)
    return crypto_listings
