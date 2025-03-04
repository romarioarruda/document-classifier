import os
from motor.motor_asyncio import AsyncIOMotorClient


class MongoDB:
    _instance = None
    _connection: AsyncIOMotorClient = None
    _db_uri = os.getenv("MONGODB_URI")

    def __new__(self):
        if self._instance is None:
            self._connection = self.create_connection(self)
            self._instance = super().__new__(self)

        return self._instance
    

    def create_connection(self):
        if self._db_uri is None:
            raise Exception("MONGODB_URI must be filled in env variables")
        
        return AsyncIOMotorClient(self._db_uri, minpoolsize=10)


    def close_connection(self):
        if self._connection is None:
            return

        self._connection.close()
        self._connection = None
        print('MongoDB connection closed successfully!')


    def get_connection(self):
        return self._connection