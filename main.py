from binance.client import Client
from dotenv import load_dotenv
from scripts import download_historical_data as dhd
import time
import os
DAY_SEC = 86400

# Coins to watch
watchlist = ['DOGEUSDT', 'BTCUSDT', 'ETHUSDT']
time_interval = Client.KLINE_INTERVAL_1MINUTE
time_duration = "1 day ago UTC"

# Load env variables
load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

# Initialize binance
client = Client(api_key, api_secret)

# Get data for each token
current_time = time.time()
for token in watchlist:
    dhd.download_historical_data(client, token, time_interval, current_time - DAY_SEC * 5, current_time)

