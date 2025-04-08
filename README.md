# Chatbot Đảo Trường Sa

![Trường Sa Islands](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Spratly_Is_since_NalGeoMag.svg/300px-Spratly_Is_since_NalGeoMag.svg.png)

## Giới thiệu

Đây là ứng dụng chatbot cung cấp thông tin giáo dục về Quần đảo Trường Sa (Spratly Islands). Ứng dụng được xây dựng với kiến trúc tách biệt giữa frontend và backend để dễ dàng phát triển và mở rộng.

## Tính năng

- 💬 Chat văn bản với chatbot
- 🎤 Ghi âm và gửi tin nhắn giọng nói
- 📝 Xem lịch sử trò chuyện
- ❓ Câu hỏi gợi ý để bắt đầu
- 🔄 Đặt lại cuộc trò chuyện
- 📱 Thiết kế responsive cho các thiết bị

## Cách sử dụng

### Khởi động ứng dụng

```bash
# Phương pháp 1: Khởi động toàn bộ ứng dụng (production)
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app

# Phương pháp 2: Khởi động riêng backend và frontend (development)
# Terminal 1 - Backend
cd backend
python start_backend.py

# Terminal 2 - Frontend
cd frontend
npm start
```

Xem hướng dẫn chi tiết tại [tài liệu hướng dẫn](docs/INSTRUCTIONS.md).

## Kiến trúc hệ thống

### Backend (Flask/Python)
- Xử lý logic chatbot và cung cấp API RESTful
- Lưu trữ dữ liệu trong session
- Có sẵn các API endpoints cho chat, voice, history, questions, và reset

### Frontend (React)
- Giao diện người dùng tương tác, xây dựng với React
- Kết nối với backend thông qua API
- Có thể chạy tách biệt trong quá trình phát triển (cổng 3000)

## API Documentation

| Endpoint | Method | Description | Request Body | Response |
|----------|--------|-------------|--------------|----------|
| `/api/chat` | POST | Gửi tin nhắn văn bản | `{"message": "text"}` | `{"response": "bot answer"}` |
| `/api/voice` | POST | Gửi tin nhắn giọng nói | `{"audio": "base64_audio_data"}` | `{"response": "bot answer"}` |
| `/api/history` | GET | Lấy lịch sử trò chuyện | - | `{"history": [{message objects}]}` |
| `/api/questions` | GET | Lấy câu hỏi gợi ý | - | `{"questions": [{question objects}]}` |
| `/api/reset` | POST | Đặt lại lịch sử | - | `{"status": "success"}` |

## Tài liệu bổ sung

Xem thêm:
- [Tài liệu hướng dẫn](docs/INSTRUCTIONS.md)
- [Tài liệu chi tiết](docs/README.md)