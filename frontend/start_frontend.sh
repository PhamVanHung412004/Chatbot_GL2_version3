#!/bin/bash
echo "===== Khởi động Frontend Chatbot Đảo Trường Sa ====="
echo "Frontend sẽ chạy trên cổng 3000"
echo "Đảm bảo rằng backend đang chạy trên cổng 5000"
echo "==================================================="
cd "$(dirname "$0")"
npm start