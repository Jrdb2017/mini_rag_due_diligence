fetch('http://localhost:8000/ask', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      question: "What is the revenue for AlphaTech Inc. in 2023?"
    })
  })
    .then(response => response.json())
    .then(data => {
      console.log('Answer:', data.answer);
    })
    .catch(error => {
      console.error('Error:', error);
    });