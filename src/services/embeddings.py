import asyncio
from typing import List

from sentence_transformers import SentenceTransformer


def _encode_batch(model: SentenceTransformer, texts: List[str], batch_size: int):
    embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        embs = model.encode(batch, convert_to_numpy=True, normalize_embeddings=True)
        embeddings.extend(embs.tolist())
    return embeddings


async def generate_embeddings(
    model: SentenceTransformer, chunks: List[str], batch_size: int = 32
) -> List[List[float]]:
    return await asyncio.to_thread(_encode_batch, model, chunks, batch_size)
