from binance.client import Client
from dotenv import load_dotenv
from scripts.download_historical_data import *
from scripts.database import *
from models.ohlcv import *
import time
import os
DAY_SEC = 86400

# Database stuff
db = DatabaseInit()
db.connect()
db.create_tables(OhlcvModel)

# Coins to watch
watchlist = ['DOGEUSDT', 'BTCUSDT', 'ETHUSDT']
time_interval = Client.KLINE_INTERVAL_1MINUTE
days_to_download = 3

# Load env variables
load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

# Initialize binance
client = Client(api_key, api_secret)


# Get data for each token
current_time = time.time()
time_start = current_time - days_to_download * DAY_SEC
for token in watchlist:

    # Get max and min time intervals from database ( This will determine if the downloads can be optimized )
    # This will work assuming the records don't have gaps ( If this becomes a problem, will iterate. But would rather not for the sake of performance )
    min = OhlcvModel.select(fn.MIN(OhlcvModel.open_time)).where(OhlcvModel.token == token).scalar()
    max = OhlcvModel.select(fn.MAX(OhlcvModel.open_time)).where(OhlcvModel.token == token).scalar()

    # Times to download
    timeframes = []

    # If records exist for this specific token
    if min and max:
        min /= 1000
        max /= 1000

        # Download data prior to current records
        if min > time_start:
            timeframes.append((time_start, min))

        # Download data from last record to current time
        if max < current_time:  # This will most likely always be true
            timeframes.append((max, current_time))

    else: # Else, download all records in timeframe
        timeframes.append((time_start, current_time))

    # Download
    for timeframe in timeframes:
        download_historical_data(client, token, time_interval, timeframe[0], timeframe[1])

    #download_historical_data(client, token, time_interval, current_time - 86400 * 1, current_time)

query = OhlcvModel.select().where(OhlcvModel.token == 'DOGEUSDT').order_by(OhlcvModel.open_time)
min = OhlcvModel.select(fn.MIN(OhlcvModel.open_time)).where(OhlcvModel.token == token).scalar()
max = OhlcvModel.select(fn.MAX(OhlcvModel.close_time)).where(OhlcvModel.token == token).scalar()
print(len(query))
print((max - min) / 60000)
