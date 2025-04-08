import React, { useState, useEffect, useRef } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPaperPlane, faMicrophone, faStop } from '@fortawesome/free-solid-svg-icons';

const MessageInput = ({ onSendMessage }) => {
  const [message, setMessage] = useState('');
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState(null);
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);
  const textInputRef = useRef(null);

  const handleInputChange = (e) => {
    setMessage(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim()) {
      onSendMessage(message);
      setMessage('');
    }
  };

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorderRef.current = new MediaRecorder(stream);
      
      mediaRecorderRef.current.ondataavailable = (event) => {
        if (event.data.size > 0) {
          audioChunksRef.current.push(event.data);
        }
      };
      
      mediaRecorderRef.current.onstop = () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/wav' });
        setAudioBlob(audioBlob);
        audioChunksRef.current = [];
        
        // Send audio to backend
        const reader = new FileReader();
        reader.readAsDataURL(audioBlob);
        reader.onloadend = () => {
          const base64Audio = reader.result.split(',')[1];
          onSendMessage(base64Audio, true);
        };
        
        // Stop all tracks of the stream
        stream.getTracks().forEach(track => track.stop());
      };
      
      audioChunksRef.current = [];
      mediaRecorderRef.current.start();
      setIsRecording(true);
    } catch (error) {
      console.error('Error accessing microphone:', error);
      alert('Không thể truy cập microphone. Vui lòng kiểm tra quyền truy cập.');
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  // Focus the text input on component mount
  useEffect(() => {
    textInputRef.current?.focus();
  }, []);

  return (
    <div className="message-input-container">
      <button
        className={`mic-button ${isRecording ? 'recording' : ''}`}
        onClick={isRecording ? stopRecording : startRecording}
        title={isRecording ? 'Dừng ghi âm' : 'Bắt đầu ghi âm'}
      >
        <FontAwesomeIcon icon={isRecording ? faStop : faMicrophone} />
      </button>
      
      <form onSubmit={handleSubmit} className="message-form">
        <input
          type="text"
          ref={textInputRef}
          className="message-input"
          value={message}
          onChange={handleInputChange}
          onKeyDown={handleKeyDown}
          placeholder="Nhập câu hỏi về Đảo Trường Sa..."
          disabled={isRecording}
        />
        <button 
          type="submit" 
          className="send-button" 
          disabled={!message.trim() || isRecording}
        >
          <FontAwesomeIcon icon={faPaperPlane} />
        </button>
      </form>
    </div>
  );
};

export default MessageInput;