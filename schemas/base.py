from typing import Optional
from pydantic import BaseModel


class BaseToken(BaseModel):
    symbol: str
    name: str
    id: int
    icon: str
    rank: Optional[int]


class BaseRequest(BaseModel):
    pass


class BaseResponse(BaseModel):
    code: int
    message: str
