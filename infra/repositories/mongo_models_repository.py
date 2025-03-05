from typing import Dict
from motor.motor_asyncio import AsyncIOMotorDatabase

from infra.repositories.mongo_base_repository import MongoBaseRepository


class MongoModelsRepository(MongoBaseRepository):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db, "models")


    async def get_all(self, filter_query: Dict = None):
        return await self.get_all(filter_query)

