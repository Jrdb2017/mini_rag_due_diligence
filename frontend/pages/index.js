import { useState } from 'react';

export default function Home() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/ask`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question }),
    });

    const data = await res.json();
    setAnswer(data.answer);
  };

  return (
    <main style={{ padding: '2rem' }}>
      <h1>Mini RAG Due Diligence Q&A</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask your question..."
          style={{ width: '300px', marginRight: '1rem' }}
        />
        <button type="submit">Ask</button>
      </form>
      {answer && (
        <div style={{ marginTop: '2rem' }}>
          <h2>Answer:</h2>
          <p>{answer}</p>
        </div>
      )}
    </main>
  );
}
