from typing import List, Optional

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class ProductModel(BaseModel):
    id: int
    name: str
    price: int
    category: int

class ProductGrapheneModel(PydanticObjectType):
    class Meta:
        model = ProductModel

class ProductGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = ProductModel
        exclude_fields = ('id')
