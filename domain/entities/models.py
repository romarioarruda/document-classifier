from typing import List
from pydantic import BaseModel, Field

from domain.dtos.field_pattern import FieldPatternDTO


class ModelsEntity(BaseModel):
    id: str = Field(alias='_id')
    classification: str = Field(..., min_length=3, max_length=30)
    classification_raw: str = Field(..., min_length=3, max_length=30, alias='classificationRaw')
    text: str = Field(..., min_length=10, max_length=10000)


class ModelFieldsEntity(BaseModel):
    id: str = Field(alias='_id')
    model_id: str = Field(..., min_length=20, max_length=128, alias='modelId')
    fields_and_patterns: List[FieldPatternDTO] = Field(..., alias='fieldsAndPatterns')
