import os
import json
import speech_recognition as sr
from pathlib import Path
from semantic_search import Sematic_search
from sentence_transformers import SentenceTransformer
from gen import Answer_Question_From_Documents
from langdetect import detect, LangDetectException
from deep_translator import GoogleTranslator
from read_file import Read_File_CSV
from gtts import gTTS

# Lấy thư mục gốc của file hiện tại (tức là backend/)
BASE_DIR = Path(__file__).resolve().parent

def load_model() -> SentenceTransformer:
    return SentenceTransformer(str(BASE_DIR / "model" / "all-MiniLM-L6-v2"))

def get_answer(use_query):
    try:
        # Tìm kiếm semantic
        list_index = Sematic_search(load_model(), use_query, 3).run()
        vector_tmp = list_index[0]
        vector = [int(i) for i in vector_tmp]

        # Đọc dữ liệu từ dataset.csv (dùng Path)
        dataset_path = BASE_DIR / "dataset.csv"
        datas = Read_File_CSV(str(dataset_path)).run()

        # Lấy các đoạn văn bản liên quan
        list_context = [datas["text"][i] for i in vector]
        
        # Tạo câu trả lời
        answer = Answer_Question_From_Documents(use_query, list_context).run()

        # Dịch nếu không phải tiếng Việt
        if detect(answer) != 'vi':
            answer = GoogleTranslator(source='auto', target='vi').translate(answer)

        return answer

    except ZeroDivisionError as e:
        title = str(e)
        if detect(title) != 'vi':
            title = GoogleTranslator(source='auto', target='vi').translate(title)
     
        return f"Lỗi: {title}"
