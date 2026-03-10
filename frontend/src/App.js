import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [currentQuote, setCurrentQuote] = useState(null);
  const [quotes, setQuotes] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchQuotes();
  }, []);

  const fetchQuotes = async () => {
    try {
      const response = await axios.get(`${API_URL}/quotes`);
      setQuotes(response.data);
    } catch (error) {
      console.error('Error fetching quotes:', error);
    }
  };

  const generateQuote = async () => {
    setLoading(true);
    try {
      const response = await axios.post(`${API_URL}/generate`);
      setCurrentQuote(response.data);
      fetchQuotes();
    } catch (error) {
      console.error('Error generating quote:', error);
      alert('Failed to generate quote. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const deleteQuote = async (id) => {
    try {
      await axios.delete(`${API_URL}/quote/${id}`);
      fetchQuotes();
      if (currentQuote && currentQuote.id === id) {
        setCurrentQuote(null);
      }
    } catch (error) {
      console.error('Error deleting quote:', error);
    }
  };

  return (
    <div className="app">
      <div className="container">
        <h1>AI Quote Generator</h1>
        
        <button 
          className="generate-btn" 
          onClick={generateQuote}
          disabled={loading}
        >
          {loading ? 'Generating...' : 'Generate Quote'}
        </button>

        {currentQuote && (
          <div className="current-quote">
            <p>"{currentQuote.text}"</p>
          </div>
        )}

        <div className="quotes-list">
          <h2>Saved Quotes</h2>
          {quotes.length === 0 ? (
            <p className="no-quotes">No quotes saved yet. Generate one!</p>
          ) : (
            quotes.map((quote) => (
              <div key={quote.id} className="quote-item">
                <p>"{quote.text}"</p>
                <button 
                  className="delete-btn"
                  onClick={() => deleteQuote(quote.id)}
                >
                  Delete
                </button>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
