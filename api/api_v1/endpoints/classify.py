from fastapi import APIRouter

from schemas.classify import ClassifyRequest, ClassifyResponse, BaseToken
from tasks.classify import classifier

router = APIRouter()


@router.post("", response_model=ClassifyResponse)
async def classify(classify_request: ClassifyRequest):
    content = '. '.join([classify_request.title, classify_request.description, classify_request.keywords])
    result = classifier.classify(text_content=content)
    return ClassifyResponse(
        code=0,
        message='success',
        data=result
    )
