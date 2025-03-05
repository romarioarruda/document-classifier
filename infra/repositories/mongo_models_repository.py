from typing import Dict, List
from motor.motor_asyncio import AsyncIOMotorDatabase

from domain.entities.models import ModelsEntity
from infra.repositories.mongo_base_repository import MongoBaseRepository


class MongoModelsRepository(MongoBaseRepository):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db, "models")


    async def list_all(self, filter_query: Dict = None) -> List[ModelsEntity]:
        return await self.get_all(filter_query)

