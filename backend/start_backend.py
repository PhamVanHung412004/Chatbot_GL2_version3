#!/usr/bin/env python3
"""
Script to start the backend server for Chatbot Đảo Trường Sa
"""
import os
import sys

print("="*50)
print("Khởi động Backend Chatbot Đảo Trường Sa")
print("Backend sẽ chạy trên cổng 5000")
print("API endpoints sẽ có sẵn tại: http://localhost:5000/api/")
print("="*50)

# Change to the current directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Import and run the Flask application
from app import app
app.run(host="0.0.0.0", port=5000, debug=True)
app.chat()