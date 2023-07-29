from fastapi import APIRouter

from api.api_v1.endpoints import classify
from api.api_v1.endpoints import filter_embedding
from api.api_v1.endpoints import sentiment_summary

api_router = APIRouter()
api_router.include_router(classify.router, prefix="/classify", tags=["Classify"])
api_router.include_router(filter_embedding.router, prefix="/filter_embedding", tags=["Filter by embedding"])
api_router.include_router(sentiment_summary.router, prefix="/sentiment_summary", tags=["Sentiment and summary"])
