import json
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
from pathlib import Path

class read_file_json:
    def __init__(self, path : str = None) -> None:
        '''
        path : đường dẫn của file .txt
        '''
        self.__path = path

    def get_data(self) -> dict:
        with open(self.__path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
def main():
    file_path = Path(__file__).parent.parent / "truong_sa_qa_deduplicated.json"
    # print(file_path)
    model = SentenceTransformer("all-MiniLM-L6-v2")  

    data = read_file_json(file_path).get_data()
    vector_data_answers = [ key for key , value in data.items()]

    
    embeddings = np.array([model.encode(doc).tolist() for doc in vector_data_answers])  # Chuyển thành list để lưu vào CSV
    df = pd.DataFrame({
        "chunk_id": range(1, len(vector_data_answers) + 1),
        "text": vector_data_answers,
        "embedding": [json.dumps(emb.tolist()) for emb in embeddings],  # Chuyển embedding thành JSON để lưu vào CSV
    })

    df.to_csv("/home/phamvanhung/project/Chatbot_GL2_version3/backend/dataset_tmp.csv", index=False, encoding="utf-8")

main()
