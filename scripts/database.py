from peewee import * 


class DatabaseInit():
    def __init__(self):
        self.database = SqliteDatabase('data.db')

    def connect(self):
        self.database.connect()

    def create_tables(self, OhlvcModel):
        self.database.create_tables([OhlvcModel])



