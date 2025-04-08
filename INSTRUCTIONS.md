# Hướng dẫn khởi động Chatbot Đảo Trường Sa

## Cấu trúc dự án

Dự án gồm hai phần chính:
- **Backend (Flask/Python)** - Xử lý logic chatbot và API
- **Frontend (React)** - Giao diện người dùng

## Cách 1: Khởi động toàn bộ ứng dụng

Sử dụng Gunicorn để khởi động backend với các API endpoints:

```bash
# Tại thư mục gốc của dự án
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

Sau khi khởi động, API sẽ có sẵn tại:
- http://localhost:5000/api/chat (POST) - Gửi tin nhắn văn bản
- http://localhost:5000/api/voice (POST) - Gửi tin nhắn giọng nói
- http://localhost:5000/api/history (GET) - Lấy lịch sử trò chuyện
- http://localhost:5000/api/questions (GET) - Lấy câu hỏi gợi ý
- http://localhost:5000/api/reset (POST) - Đặt lại lịch sử

## Cách 2: Phát triển với frontend và backend tách biệt

### Khởi động Backend

```bash
cd backend
python start_backend.py
```

Backend sẽ chạy trên cổng 5000.

### Khởi động Frontend (phát triển)

```bash
cd frontend
npm install  # Chỉ chạy lần đầu tiên
npm start
```

Frontend sẽ chạy trên cổng 3000, và kết nối với backend thông qua proxy.

## Testing API

Bạn có thể test các API bằng cách sử dụng curl:

```bash
# Lấy câu hỏi gợi ý
curl http://localhost:5000/api/questions

# Gửi tin nhắn
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Vị trí của đảo Trường Sa ở đâu?"}'

# Lấy lịch sử
curl http://localhost:5000/api/history
```