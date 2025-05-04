import os

from sentence_transformers import SentenceTransformer


def load_model() -> SentenceTransformer:
    device = os.getenv("EMBEDDER_DEVICE", default="cpu")
    model_name = os.getenv("EMBEDDER_MODEL", default="BAAI/bge-m3")
    model = SentenceTransformer(model_name, device=device)

    if model.device.type == "cuda":
        model.half()
    model.eval()
    return model
