from typing import List
from schemas.base import BaseResponse, BaseToken, BaseRequest


class ClassifyRequest(BaseRequest):
    title: str
    description: str
    keywords: str


class ClassifyResponse(BaseResponse):
    data: List[BaseToken]
