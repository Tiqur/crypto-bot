from binance.client import Client
from dotenv import load_dotenv
from scripts.download_historical_data import *
from scripts.database import *
from models.ohlvc import *
import time
import os

# Database stuff
db = DatabaseInit()
db.connect()
db.create_tables(OhlvcModel)

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
    download_historical_data(client, token, time_interval, current_time - 86400 * 5, current_time)

