import numpy as np
from pathlib import Path
import faiss
from sentence_transformers import SentenceTransformer
from Input import Init_Input

# Đường dẫn đến thư mục chứa file vector_database.faiss
BASE_DIR = Path(__file__).resolve().parent
VECTOR_PATH = BASE_DIR / "vector_tmp.faiss"

def read_model() -> dict:
    # Đọc file FAISS từ đường dẫn đã chuẩn hóa bằng pathlib
    index = faiss.read_index(str(VECTOR_PATH))
    return index

class Sematic_search(Init_Input):
    def __init__(self, model: SentenceTransformer, use_query: str, top_k: int) -> None:
        super().__init__(use_query, top_k)
        self.model = model

    def run(self) -> list:
        index = read_model()
        query_embedding = self.model.encode([self.use_query])[0]
        query_embedding = np.array(query_embedding, dtype="float32").reshape(1, -1)
        D, I = index.search(query_embedding, self.top_k)
        return I
