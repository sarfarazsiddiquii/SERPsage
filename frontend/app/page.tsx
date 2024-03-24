"use client";
import { useState } from 'react';

export default function Home() {
  const [text, setText] = useState('');
  const [sitemapLinks, setSitemapLinks] = useState([]);

  const handleSubmit = async () => {
    try {
      const response = await fetch('/generate-sitemap', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: text })
      });

      if (response.ok) {
        const data = await response.json();
        const links = data.links;
        setSitemapLinks(links);
      } else {
        console.error('Failed to fetch sitemap:', response.statusText);
      }
    } catch (error) {
      console.error('An error occurred:', error);
    }
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
      <div className="sitemap-links">
        <h2>Links in sitemap:</h2>
        <ul>
          {sitemapLinks.map((link, index) => (
            <li key={index}>{link}</li>
          ))}
        </ul>
      </div>
    </main>
  );
}
