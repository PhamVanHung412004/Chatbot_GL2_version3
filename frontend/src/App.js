import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import ChatPanel from './components/ChatPanel';
import HistoryPanel from './components/HistoryPanel';
import MessageInput from './components/MessageInput';

function App() {
  const [messages, setMessages] = useState([]);
  const [history, setHistory] = useState([]);
  const [predefinedQuestions, setPredefinedQuestions] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    // Fetch predefined questions on component mount
    fetchPredefinedQuestions();
    
    // Fetch chat history on component mount
    fetchHistory();
  }, []);

  const fetchPredefinedQuestions = async () => {
    try {
      const response = await axios.get('/api/questions');
      setPredefinedQuestions(response.data.questions);
    } catch (error) {
      console.error('Error fetching predefined questions:', error);
    }
  };

  const fetchHistory = async () => {
    try {
      const response = await axios.get('/api/history');
      setHistory(response.data.history);
      setMessages(response.data.history);
    } catch (error) {
      console.error('Error fetching history:', error);
    }
  };

  const handleSendMessage = async (message, isVoice = false) => {
    if (!message.trim()) return;

    const newMessage = { text: message, sender: 'user' };
    setMessages(prevMessages => [...prevMessages, newMessage]);
    setIsLoading(true);

    try {
      let endpoint = '/api/chat';
      let data = { message };
      
      if (isVoice) {
        endpoint = '/api/voice';
        data = { audio: message }; // In voice mode, message contains the audio data
      }

      const response = await axios.post(endpoint, data);
      
      setIsLoading(false);
      setMessages(prevMessages => [
        ...prevMessages,
        { text: response.data.response, sender: 'bot' }
      ]);
      
      // Update history after sending a message
      fetchHistory();
    } catch (error) {
      console.error('Error sending message:', error);
      setIsLoading(false);
      setMessages(prevMessages => [
        ...prevMessages,
        { 
          text: 'Xin lỗi, có lỗi xảy ra khi xử lý tin nhắn của bạn.', 
          sender: 'bot' 
        }
      ]);
    }
  };

  const handleResetChat = async () => {
    try {
      await axios.post('/api/reset');
      setMessages([]);
      setHistory([]);
    } catch (error) {
      console.error('Error resetting chat:', error);
    }
  };

  const handleSelectQuestion = (question) => {
    // If question is an object with text property, use that
    if (question && typeof question === 'object' && question.text) {
      handleSendMessage(question.text);
    } else {
      // Otherwise use the question directly
      handleSendMessage(question);
    }
  };

  return (
    <div className="app-container">
      <div className="sidebar">
        <div className="logo-container">
          <h1>Đảo Trường Sa</h1>
        </div>
        <HistoryPanel 
          history={history} 
          onSelectQuestion={handleSendMessage} 
          onReset={handleResetChat} 
        />
        <div className="predefined-questions">
          <h3>Câu hỏi gợi ý</h3>
          <ul>
            {predefinedQuestions.map((question, index) => (
              <li 
                key={question.id || index} 
                onClick={() => handleSelectQuestion(question)}
              >
                {question.text || question}
              </li>
            ))}
          </ul>
        </div>
      </div>
      
      <div className="main-panel">
        <ChatPanel 
          messages={messages} 
          isLoading={isLoading} 
        />
        <MessageInput 
          onSendMessage={handleSendMessage} 
        />
      </div>
    </div>
  );
}

export default App;