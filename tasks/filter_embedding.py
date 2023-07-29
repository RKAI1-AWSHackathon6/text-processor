import pinecone
import uuid
from core.config import settings
from tasks.chatgpt_api import api_chat_gpt


class FilterEmbedding:
    def __init__(self):
        pinecone.init(api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENVIRONMENT)
        self.index = pinecone.Index(settings.PINECONE_INDEX_NAME)

    def check_embedding_in_index(self, content) -> bool:
        embedding = None
        is_done = False
        for _ in range(settings.RETRY_OPENAI_API):
            for i in range(len(settings.OPENAI_API_KEYS)):
                embedding = api_chat_gpt.get_embedding(content, settings.OPENAI_API_KEYS[i])
                if embedding is not None:
                    is_done = True
                    break
            if is_done:
                break

        if embedding is None:
            return False
        result = self.index.query(vector=embedding, top_k=1, include_values=False)['matches']
        if len(result) == 0 or result[0]['score'] <= settings.EMBEDDING_SCORE_THRESHOLD:
            self.index.upsert([
                (str(uuid.uuid4()), embedding)
            ])
            return True
        return False


filter_embeder = FilterEmbedding()

if __name__ == '__main__':
    pinecone.init(api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENVIRONMENT)
    pinecone.create_index(name=settings.PINECONE_INDEX_NAME,
                          dimension=settings.EMBEDDING_SIZE,
                          metric=settings.PINECONE_INDEX_METRIC)
    print(pinecone.list_indexes())

    # filter_embeder.check_embedding_in_index('This is a test')
