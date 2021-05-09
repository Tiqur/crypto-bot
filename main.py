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
for token in watchlist:
    
    print(f"Downloading {token} historical data...")
    historical_data = client.get_historical_klines(token, time_interval, time_duration)

    # Extract OHLVC from data
    for ohlcv in historical_data:
        [
            open_time,
            open,
            high,
            low,
            close,
            volume,
            close_time,
            quote_asset_volume,
            num_of_trades,
            taker_buy_base_asset_volume,
            taker_buy_base_quote_asset_volume,
            ignore
        ] = ohlcv
        
        


current_time = time.time()
dhd.download_historical_data(client, 'DOGEUSDT', time_interval, current_time - DAY_SEC * 20, current_time)

