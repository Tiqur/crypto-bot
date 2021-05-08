from datetime import datetime
import os

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
DAY_MS = 8.64E+7

def download_historica_data(token, time_start, time_end):
    time_diff = time_end - time_start
    days = time_diff / DAY_MS

    # Download chunks of data rather than all at once
    while days > 0:
        start = days * DAY_MS
        end = (days * DAY_MS) + DAY_MS

        # Get data from binance api
        print(f"Downloading {token} historical data, {end / DAY_MS} -> {start / DAY_MS}...")
        historical_data = client.get_historical_klines(token, time_interval, time_duration)
        print(historical_data)

        # Insert data to db
        days -= 1



    
