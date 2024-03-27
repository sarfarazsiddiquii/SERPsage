"use client";
import { useState, useEffect } from 'react';

export default function Home() {
  const [inputText, setInputText] = useState('');
  const [apiData, setApiData] = useState<any>(null);
  const [submitted, setSubmitted] = useState(false);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(event.target.value);
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setSubmitted(true);
    console.log(inputText);
    try {
      const response = await fetch('http://localhost:8080/api/home', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ website_name: inputText }),
      });
      if (response.ok) {
        const data = await response.json();
        setApiData(data);
      } else {
        console.error('Failed to fetch API data');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>Welcome to SERPsage !</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inputText}
          onChange={handleInputChange}
          placeholder="Enter website name here"
        />
        <button type="submit">Submit</button>
      </form>
      {submitted && apiData && (
        <div>
          <h2>API Data:</h2>
          <pre>{JSON.stringify(apiData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
