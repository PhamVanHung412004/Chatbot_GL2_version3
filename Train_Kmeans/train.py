from package import np
from package import pd
from package import Read_File
from package import Kmeans
from package import Embedding_To_Numpy
from package import Path
from package import joblib
import faiss


def main():
    # Read file csv
    file_path = Path(__file__).parent.parent

    data = Read_File(file_path / "backend"/ "dataset_tmp.csv").run()
    data_embedding = Embedding_To_Numpy(data["embedding"]).convert_to_numpy()
    d = 384
    index = faiss.IndexFlatL2(d)  # Tạo index kiểu L2

    index.add(data_embedding)
    faiss.write_index(index, str(file_path / "backend" / "semantic_search" / "vector_tmp.faiss"))

main()  