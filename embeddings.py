
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class EmbeddingModel:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        return self.model.encode(texts, convert_to_numpy=True)

def rank_chunks(query, chunks, embedder):
    query_vec = embedder.embed([query])[0].reshape(1, -1)
    chunk_vecs = embedder.embed(chunks)
    similarities = cosine_similarity(query_vec, chunk_vecs)[0]
    ranked = sorted(zip(chunks, similarities), key=lambda x: x[1], reverse=True)
    return ranked
