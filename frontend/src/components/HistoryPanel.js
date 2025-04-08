import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrash } from '@fortawesome/free-solid-svg-icons';

const HistoryPanel = ({ history, onSelectQuestion, onReset }) => {
  // Group history items by date
  const groupedHistory = history.reduce((groups, item) => {
    const date = new Date(item.timestamp).toLocaleDateString();
    if (!groups[date]) {
      groups[date] = [];
    }
    groups[date].push(item);
    return groups;
  }, {});

  return (
    <div className="history-panel">
      <div className="history-header">
        <h3>Lịch sử trò chuyện</h3>
        <button 
          className="reset-button" 
          onClick={onReset}
          title="Xóa lịch sử"
        >
          <FontAwesomeIcon icon={faTrash} />
        </button>
      </div>
      
      <div className="history-list">
        {Object.keys(groupedHistory).length > 0 ? (
          Object.entries(groupedHistory).map(([date, items]) => (
            <div key={date} className="history-date-group">
              <div className="history-date">{date}</div>
              {items.map((item, index) => (
                <div 
                  key={index} 
                  className="history-item"
                  onClick={() => onSelectQuestion(item.text)}
                >
                  {item.text.length > 30 
                    ? `${item.text.substring(0, 30)}...` 
                    : item.text}
                </div>
              ))}
            </div>
          ))
        ) : (
          <div className="empty-history">Không có lịch sử trò chuyện</div>
        )}
      </div>
    </div>
  );
};

export default HistoryPanel;