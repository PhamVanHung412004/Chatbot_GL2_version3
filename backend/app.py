import os
import json
from flask import Flask, render_template, request, jsonify, session, send_from_directory
from flask_cors import CORS
# from backend.data import get_answer, get_predefined_questions
from data import get_answer
import logging

app = Flask(__name__)
CORS(app)  # Cho phép cross-origin requests từ frontend
app.secret_key = os.environ.get("SESSION_SECRET", "spratlys_islands_secret_key")

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint to process chat messages and return responses."""
    data = request.json
    user_message = data.get('message', '')

    # Get session chat history or initialize if not exists
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    # Add user message to history
    if user_message:
        # Add user message to chat history
        session['chat_history'].append({
            'role': 'user',
            'content': user_message
        })
        # print( "use: " , user_message)
        # Get bot response
        bot_response = get_answer(user_message)
        print("answers : " , bot_response)
        # Add bot response to chat history
        session['chat_history'].append({
            'role': 'bot',
            'content': bot_response
        })
        
        # Save session
        session.modified = True
        
        # Không cần chuyển đổi lịch sử ở đây vì frontend chỉ cần response
        return jsonify({
            'response': bot_response
        })
    
    return jsonify({'error': 'No message provided'}), 400

@app.route('/api/history')
def history():
    """API endpoint to get chat history."""
    # Get chat history from session or initialize as empty list
    chat_history = session.get('chat_history', [])
    
    # Debug: Print the session data
    print("Session chat_history:", chat_history)
    
    # Convert session history format to frontend format
    frontend_history = []
    
    for item in chat_history:
        # Check data structure
        if isinstance(item, dict) and 'role' in item and 'content' in item:
            sender = 'user' if item['role'] == 'user' else 'bot'
            frontend_history.append({
                'text': item['content'],
                'sender': sender,
                'timestamp': '2025-04-06T10:00:00Z'  # Placeholder timestamp
            })
    
    # Debug: Print the frontend history
    print("Frontend history:", frontend_history)
    
    return jsonify({
        'history': frontend_history
    })

# @app.route('/api/questions')
# def questions():
#     """API endpoint to get predefined questions."""
#     return jsonify({
#         'questions': get_predefined_questions()
#     })

@app.route('/api/reset', methods=['POST'])
def reset():
    """API endpoint to reset the chat history."""
    # We don't clear the session history anymore, just return success
    # This allows the frontend to clear the current chat but keep history in sidebar
    return jsonify({'status': 'success'})

@app.route('/api/voice', methods=['POST'])
def voice():
    """API endpoint to handle voice input."""
    # In a real app, you would process audio and convert it to text
    # using a service like Google Speech-to-Text API
    data = request.json
    
    # Get the base64 audio data
    audio_data = data.get('audio', '')
    
    if audio_data:
        # In a real implementation, you would send the audio to a speech-to-text service
        # For this demo, we'll just return a default response
        text = "Đây là tin nhắn thoại" # Placeholder text since we don't have actual speech-to-text
        bot_response = get_answer(text)
        
        # Update session history
        if 'chat_history' not in session:
            session['chat_history'] = []
        
        session['chat_history'].append({
            'role': 'user',
            'content': text + " (voice message)"
        })
        
        session['chat_history'].append({
            'role': 'bot',
            'content': bot_response
        })
        
        session.modified = True
        
        return jsonify({
            'response': bot_response
        })
    
    return jsonify({'error': 'No audio data provided'}), 400

# Serve HTML template or static files from React build folder
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    # Cố gắng tìm frontend build
    frontend_build_path = os.path.join('frontend', 'build')
    
    if path != "" and os.path.exists(os.path.join(frontend_build_path, path)):
        return send_from_directory(frontend_build_path, path)
    else:
        # Check if index.html exists in the build folder
        if os.path.exists(os.path.join(frontend_build_path, 'index.html')):
            return send_from_directory(frontend_build_path, 'index.html')
        else:
            # Phục vụ trang HTML từ template
            templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
            if os.path.exists(os.path.join(templates_dir, 'index.html')):
                return send_from_directory(templates_dir, 'index.html')
            else:
                # Trả về thông báo API đang chạy nếu không có template hoặc frontend build
                return jsonify({
                    "status": "API Running",
                    "message": "Frontend is not built. API endpoints are available at /api/",
                    "endpoints": [
                        {"path": "/api/chat", "method": "POST", "description": "Send text message and get response"},
                        {"path": "/api/voice", "method": "POST", "description": "Send voice message and get response"},
                        {"path": "/api/history", "method": "GET", "description": "Get chat history"},
                        {"path": "/api/questions", "method": "GET", "description": "Get predefined questions"},
                        {"path": "/api/reset", "method": "POST", "description": "Reset chat history"}
                    ]
                })

logging.basicConfig(level=logging.DEBUG)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)