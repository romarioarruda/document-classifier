from uuid import UUID
from typing import Dict
from pydantic import BaseModel, Field


class ModelEntity(BaseModel):
    id: UUID
    classification: str = Field(min_length=3, max_length=30)
    classification_raw: str = Field(min_length=3, max_length=30)
    text: str = Field(min_length=10, max_length=10000)


class ModelFieldsEntity(BaseModel):
    id: UUID
    modelId: UUID
    fields: Dict
