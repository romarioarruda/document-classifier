from typing import Dict, List, Optional
from motor.motor_asyncio import AsyncIOMotorDatabase


class MongoBaseRepository:
    def __init__(self, db: AsyncIOMotorDatabase, collection_name: str):
        self.collection = db.get_collection(collection_name)


    async def create(self, data: Dict):
        """Insert a new document and return the ID"""
        result = await self.collection.insert_one(data)
        return result.inserted_id


    async def get_by_id(self, document_id: str) -> Optional[Dict]:
        """Search a document by ID"""
        return await self.collection.find_one({"_id": document_id})


    async def get_all(self, filter_query: Dict = None) -> List[Dict]:
        """Search for documents based on filter query"""
        filter_query = filter_query or {}
        cursor = self.collection.find(filter_query)
        return [document async for document in cursor]


    async def update(self, document_id: str, update_data: Dict) -> Optional[Dict]:
        """Update a document and return the updated values"""
        result = await self.collection.find_one_and_update(
            {"_id": document_id},
            {"$set": update_data},
            return_document=True
        )
        return result


    async def delete(self, document_id: str) -> bool:
        """Delete document by ID"""
        result = await self.collection.delete_one({"_id": document_id})
        return result.deleted_count > 0

