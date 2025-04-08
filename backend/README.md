# Backend cho Chatbot Đảo Trường Sa

## Mô tả

Backend cho chatbot Đảo Trường Sa được xây dựng bằng Flask (Python), cung cấp các API endpoints để xử lý tin nhắn văn bản, tin nhắn giọng nói, lịch sử trò chuyện và các câu hỏi gợi ý.

## Cấu trúc

- `app.py`: Flask application chính và các API routes
- `data.py`: Dữ liệu và logic xử lý câu hỏi/trả lời về Đảo Trường Sa
- `main.py`: Entry point cho backend
- `start_backend.py`: Script để khởi động backend riêng biệt

## API Endpoints

| Endpoint | Method | Description | Request Body | Response |
|----------|--------|-------------|--------------|----------|
| `/api/chat` | POST | Xử lý tin nhắn văn bản | `{"message": "text"}` | `{"response": "bot answer"}` |
| `/api/voice` | POST | Xử lý tin nhắn giọng nói | `{"audio": "base64_audio_data"}` | `{"response": "bot answer"}` |
| `/api/history` | GET | Lấy lịch sử trò chuyện | - | `{"history": [{message objects}]}` |
| `/api/questions` | GET | Lấy câu hỏi gợi ý | - | `{"questions": [{question objects}]}` |
| `/api/reset` | POST | Đặt lại lịch sử | - | `{"status": "success"}` |

## Khởi động Backend

```bash
python start_backend.py
```

hoặc 

```bash
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

## Lưu ý phát triển

- Dữ liệu chatbot được lưu trữ trong `data.py`
- Lịch sử trò chuyện được lưu trong Flask session
- CORS đã được bật để cho phép kết nối từ frontend