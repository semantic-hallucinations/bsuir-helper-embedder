from typing import List

from pydantic import BaseModel


class EmbedRequest(BaseModel):
    chunks: List[str]


class EmbedResponse(BaseModel):
    embeddings: List[List[float]]
