from binance.client import Client
from datetime import datetime, timezone
import math
import os
DAY_SEC = 86400


def download_historical_data(client, token, interval, time_start, time_end):
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

        # Insert data to db
        time_start += DAY_SEC



    
