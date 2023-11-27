from sentence_transformers import SentenceTransformer
from config import *

class Embedder:
    __embedder = None

    def __init__(self):
        self.__embedder = SentenceTransformer(EMBEDDING_MODEL)

    def encode(self, msg: str):
        return self.__embedder.encode([msg], show_progress_bar=True, normalize_embeddings=True)
    
    def encode(self, msgs: list):
        return self.__embedder.encode(msgs, show_progress_bar=True, normalize_embeddings=True)