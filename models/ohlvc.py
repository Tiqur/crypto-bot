# Initialize sqlite database
ohlcv_db = SqliteDatabase('data.db')

# ohlcv table
class OHLVC(Model):
    token: TextField()
    interval: SmallIntegerField()
    open_time: BigIntegerField()
    open: DecimalField()
    high: DecimalField()
    low: DecimalField()
    close: DecimalField()
    volume: BigIntegerField()
    close_time: BigIntegerField()
    num_of_trades: BigIntegerField()
    taker_buy_base_asset_volume: BigIntegerField()
    taker_buy_base_quote_asset_volume: BigIntegerField()

    class Meta:
        database = ohlcv_db



