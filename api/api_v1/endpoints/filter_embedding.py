from fastapi import APIRouter

from schemas.filter_embedding import FilterEmbeddingRequest, FilterEmbeddingResponse
from tasks.filter_embedding import filter_embeder

router = APIRouter()


@router.post("", response_model=FilterEmbeddingResponse)
async def filter_embedding(req: FilterEmbeddingRequest):
    content = req.title + ". " + req.description
    resp = filter_embeder.check_embedding_in_index(content)
    return FilterEmbeddingResponse(code=200, message="success", data=resp)
