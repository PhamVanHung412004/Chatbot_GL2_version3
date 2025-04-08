#!/bin/bash
# Script to start the complete Chatbot Đảo Trường Sa application

echo "===== Khởi động Chatbot Đảo Trường Sa ====="
echo "Chạy ứng dụng hoàn chỉnh với Gunicorn"
echo "Ứng dụng sẽ có sẵn tại: http://localhost:5000"
echo "API endpoints sẽ có sẵn tại: http://localhost:5000/api/"
echo "============================================"

# Get the current directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Start the application with Gunicorn
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app