from peewee import * 
from scripts.database import *


# ohlcv table
class OhlvcModel(Model):
    token = TextField()
    interval = SmallIntegerField()
    open_time = BigIntegerField()
    open = DecimalField()
    high = DecimalField()
    low = DecimalField()
    close = DecimalField()
    volume = DecimalField()
    close_time = BigIntegerField()
    num_of_trades = BigIntegerField()

    class Meta:
        database  = DatabaseInit().database



