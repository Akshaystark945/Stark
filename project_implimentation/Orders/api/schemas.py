# file orders/api/schemas.py

from enum import Enum
from typing import List, list, Optional
from uuid import UUID
from pydantic import conint, conlisst, basemodel, field, field_validator
from datetime import datetime

class Size(Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'

class status(Enum):
    created = 'created'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatch = 'dispatch'
    delivered = 'delivered'

class OrderItemSchema(basemodel):
    product: str
    size: Size
    # optional type given as int, fields first argument specifies 1
    # Second argument greater than or equal
    # third argument strictly integer 1, no string or float 
    Quantity: Optional[int]= field(1, ge=1, strict=True)
    # additional validator in order to restrain from using the null value
    @field_validator('quantity')
    def quantity_non_nullable(cls, value):
        if value is None:
            raise ValueError('quantity may not be none')
        return value

class CreateOrderSchema(basemodel):
    order: List[OrderItemSchema] = field(..., min_items=1)

class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: status

class GetOrdersSchema(basemodel):
    orders: List[GetOrderSchema]