from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from organisation_utils.logging_config import logger_factory
from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_fixed,
)

from models import EmbedRequest, EmbedResponse
from services import generate_embeddings, load_model

logger = logger_factory.get_logger("main_logger")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.embed_model = load_model()
    yield


app = FastAPI(title="Embedder Service", lifespan=lifespan)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/embed", response_model=EmbedResponse)
async def embed(request: EmbedRequest):
    model = app.state.embed_model
    logger.info("Model loaded")

    try:
        async for attempt in AsyncRetrying(
            stop=stop_after_attempt(3),
            wait=wait_fixed(1),
            retry=retry_if_exception_type(Exception),
        ):
            with attempt:
                logger.info("Generating embeddings...")
                embeddings = await generate_embeddings(
                    model, request.chunks, batch_size=32
                )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to produce embeddings: {e}"
        )
    return EmbedResponse(embeddings=embeddings)
