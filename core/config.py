from typing import List, Optional, Dict, Any
from pydantic import validator, PostgresDsn, BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Text Processor"
    API_V1_STR: str = "/api/v1/text_processor"

    POSTGRES_SERVER: str = "10.101.14.21:5432"
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'postgres'
    POSTGRES_DB: str = 'app'
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI")
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get('POSTGRES_USER'),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    # CLASSIFY_TOP_N: int = 5
    CLASSIFY_MIN_OCCURRENCE: int = 1
    EMBEDDING_SIZE: int = 1536
    EMBEDDING_SCORE_THRESHOLD: float = 0.85

    PINECONE_API_KEY: str = "7cf761c7-53d5-445b-8a8c-d8a216f14043"
    PINECONE_ENVIRONMENT: str = "us-west1-gcp-free"
    PINECONE_INDEX_NAME: str = "text-processor"
    PINECONE_INDEX_METRIC: str = "cosine"

    RETRY_OPENAI_API: int = 3

    OPENAI_API_KEYS: List[str] = [
        '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',
        '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',
        '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',
        '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',
        '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',
        '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'
    ]


settings = Settings()
