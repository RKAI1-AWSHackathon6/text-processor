import pinecone

from core.config import settings

pinecone.init(api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENVIRONMENT)
index = pinecone.Index(settings.PINECONE_INDEX_NAME)

delete_response = index.delete(ids=None, delete_all=True)
print(delete_response)
