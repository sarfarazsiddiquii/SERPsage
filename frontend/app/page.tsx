"use client"; 
import { useState } from 'react';

export default function Home() {
  const [text, setText] = useState('');

  const handleSubmit = () => {
    // Handle submit logic here
    console.log(text);
  };

  return (
    <main className="container">
      <p className="heading">Hello World</p>
      <div className="input-wrapper">
        <div className="mb-4">
          <input
            type="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            className="input"
          />
        </div>
        <button
          onClick={handleSubmit}
          className="button"
        >
          Submit
        </button>
      </div>
    </main>
  );
}
