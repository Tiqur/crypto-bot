from binance.client import Client
from datetime import datetime, timezone
from scripts.database import *
from models.ohlcv import *
import math 
import os
DAY_SEC = 86400


def download_historical_data(client, token, interval, time_start, time_end):
    database = DatabaseInit()
    print(f"Downloading {token} historical data...")
    

    # Download chunks of data rather than all at once
    while time_start < time_end:
        start = time_start
        end = time_start + DAY_SEC
        days_left = math.floor((time_end - start) / DAY_SEC)
        date_start = datetime.fromtimestamp(start, timezone.utc)
        date_end = datetime.fromtimestamp(end, timezone.utc)

        # Get data from binance api
        print(f"{date_start.strftime('%b %d %Y %H:%M:%S')} -> {date_end.strftime('%b %d %Y %H:%M:%S')}")
        historical_data = client.get_historical_klines(token, interval, str(start), str(end))

        # Extract OHLVC from data
        for data in historical_data:
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
            ] = data

            # Insert data to db
            OhlcvModel(
                token = token,
                interval = 1,
                open_time = open_time,
                open = open,
                high = high,
                low = low,
                close = close,
                volume = volume,
                close_time = close_time,
                num_of_trades = num_of_trades,
            ).save()
            
        time_start += DAY_SEC



    
