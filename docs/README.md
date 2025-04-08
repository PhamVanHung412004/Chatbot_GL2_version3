# Chatbot Đảo Trường Sa - Tài liệu hướng dẫn

## Giới thiệu

Đây là ứng dụng chatbot tương tác cung cấp thông tin giáo dục về Quần đảo Trường Sa (Đảo Trường Sa), được xây dựng với kiến trúc tách biệt giữa frontend và backend để dễ dàng phát triển và mở rộng.

## Kiến trúc hệ thống

### Backend (Flask/Python)
- Xử lý logic chatbot và cung cấp API RESTful
- Lưu trữ dữ liệu trong session
- Có sẵn các API endpoints cho chat, voice, history, questions, và reset

### Frontend (React)
- Giao diện người dùng tương tác, xây dựng với React
- Kết nối với backend thông qua API
- Có thể chạy tách biệt trong quá trình phát triển (cổng 3000)

## Cách khởi động ứng dụng

### Khởi động backend

```bash
cd backend
python start_backend.py
```

### Khởi động frontend (phát triển)

```bash
cd frontend
npm install  # Chỉ chạy lần đầu
npm start
```

### Khởi động toàn bộ ứng dụng (production)

```bash
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

## API Documentation

| Endpoint | Method | Description | Request Body | Response |
|----------|--------|-------------|--------------|----------|
| `/api/chat` | POST | Gửi tin nhắn văn bản | `{"message": "text"}` | `{"response": "bot answer"}` |
| `/api/voice` | POST | Gửi tin nhắn giọng nói | `{"audio": "base64_audio_data"}` | `{"response": "bot answer"}` |
| `/api/history` | GET | Lấy lịch sử trò chuyện | - | `{"history": [{message objects}]}` |
| `/api/questions` | GET | Lấy câu hỏi gợi ý | - | `{"questions": [{question objects}]}` |
| `/api/reset` | POST | Đặt lại lịch sử | - | `{"status": "success"}` |

## Cấu trúc thư mục

```
├── backend/
│   ├── app.py          # Flask application và API routes
│   ├── data.py         # Dữ liệu chatbot và logic xử lý
│   ├── main.py         # Entry point cho backend
│   └── start_backend.py # Script khởi động riêng backend
├── frontend/
│   ├── public/         # Static assets
│   ├── src/            # React source code
│   │   ├── components/ # React components
│   │   ├── App.js      # Main React component
│   │   └── index.js    # React entry point
│   ├── package.json    # Dependencies và cấu hình
│   └── README.md       # Hướng dẫn frontend
├── docs/               # Tài liệu
├── main.py             # Entry point cho toàn bộ ứng dụng
└── README.md           # Tài liệu chính
```

## Tính năng

- 💬 Chat văn bản với chatbot
- 🎤 Ghi âm và gửi tin nhắn giọng nói
- 📝 Xem lịch sử trò chuyện
- ❓ Câu hỏi gợi ý để bắt đầu
- 🔄 Đặt lại cuộc trò chuyện
- 📱 Thiết kế responsive cho các thiết bị