from binance.client import Client
from dotenv import load_dotenv
import os


# Load env variables
load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

# Initialize binance
client = Client(api_key, api_secret)

