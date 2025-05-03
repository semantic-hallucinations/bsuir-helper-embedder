import os

from sentence_transformers import SentenceTransformer


def load_model() -> SentenceTransformer:
    device = os.getenv("EMBEDDER_DEVICE", None)
    model = SentenceTransformer("BAAI/bge-m3", device=device)

    if model.device.type == "cuda":
        model.half()
    model.eval()
    return model
