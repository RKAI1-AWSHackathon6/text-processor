from fastapi import APIRouter, HTTPException

from schemas.sentiment_summary import SentimentSummaryRequest, SentimentSummaryResponse
from tasks.sentiment_semantic import sentiment_summary_er

router = APIRouter()


@router.post("", response_model=SentimentSummaryResponse)
async def sentiment_summary(request: SentimentSummaryRequest):
    res = sentiment_summary_er.get_sentiment_and_summary(request.content)
    if res is None:
        raise HTTPException(status_code=400, detail="Cannot get sentiment and summary")
    return SentimentSummaryResponse(
        code=0,
        message='success',
        data=res
    )
