# Frontend cho Chatbot Đảo Trường Sa

## Mô tả

Frontend cho chatbot Đảo Trường Sa được xây dựng bằng React, cung cấp giao diện người dùng tương tác để giao tiếp với chatbot về thông tin Đảo Trường Sa.

## Cấu trúc

- `src/App.js`: Component chính điều phối toàn bộ ứng dụng
- `src/components/`: Thư mục chứa các component
  - `ChatPanel.js`: Hiển thị tin nhắn trò chuyện
  - `HistoryPanel.js`: Hiển thị lịch sử trò chuyện
  - `MessageInput.js`: Nhập tin nhắn văn bản và ghi âm giọng nói
- `src/App.css`: Stylesheet chính cho ứng dụng

## Tính năng

- Giao diện trò chuyện trực quan
- Hỗ trợ nhập tin nhắn văn bản
- Hỗ trợ ghi âm và gửi tin nhắn giọng nói
- Hiển thị lịch sử trò chuyện
- Các câu hỏi gợi ý để bắt đầu cuộc trò chuyện
- Nút đặt lại cuộc trò chuyện
- Responsive design cho các thiết bị di động

## Khởi động Frontend (Development)

```bash
npm install  # Chỉ cần chạy lần đầu
npm start
```

Frontend sẽ chạy trên cổng 3000, và kết nối với backend thông qua proxy.

## Build Frontend cho Production

```bash
npm run build
```

Thư mục `build` sẽ chứa các tệp tĩnh có thể được phục vụ bởi backend Flask.