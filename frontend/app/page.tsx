"use client";

import { use, useState, useEffect} from 'react';

export default function Home() {
  const [inputText, setInputText] = useState('');

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputText(event.target.value);
  };

  const [apiData, setApiData] = useState<any>(null);

  useEffect(() => {
    fetch('http://localhost:8080/api/home')
      .then(response => response.json())
      .then(data => {
        // Set the API data to the state
        setApiData(data);
      })
      .catch(error => {
        // Handle any errors
        console.error(error);
      });
  }, []);

  // Render the API data on the screen



  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    // You can perform any action with the inputText here, for example, log it.
    console.log(inputText);
  };

  return (
    <div>
      <h1>Welcome to SERPsage !</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inputText}
          onChange={handleInputChange}
          placeholder="Enter text here"
        />
        <button type="submit">Submit</button>
      </form>
      {apiData && (
        <div>
          <h2>API Data:</h2>
          <pre>{JSON.stringify(apiData, null, 2)}</pre>
        </div>
      )}
    </div>
  )};
