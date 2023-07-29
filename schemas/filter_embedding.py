from schemas.base import BaseRequest, BaseResponse


class FilterEmbeddingRequest(BaseRequest):
    title: str
    description: str


class FilterEmbeddingResponse(BaseResponse):
    data: bool
