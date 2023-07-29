from typing import List, Union
from schemas.base import BaseRequest, BaseResponse, BaseModel


class SentimentSummaryRequest(BaseRequest):
    content: str


class SentimentSummaryCode(BaseModel):
    type: int
    summary: Union[str, None] = None
    explain: Union[str, None] = None
    message: str


class SentimentSummaryResponse(BaseResponse):
    data: SentimentSummaryCode
