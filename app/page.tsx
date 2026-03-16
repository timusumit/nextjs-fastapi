"use client";
import { useState } from "react";

export default function TravelPage() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState("");

  const askAI = async () => {
    setResult("Thinking...");
    const response = await fetch("/api/py/hello", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: input }),
    });
    const data = await response.json();
    setResult(data.message);
  };

  return (
    <div style={{ padding: "50px", textAlign: "center", fontFamily: "sans-serif" }}>
      <h1>🌍 AI Travel Planner</h1>
      <p>Where do you want to go?</p>
      <input 
        type="text" 
        value={input} 
        onChange={(e) => setInput(e.target.value)} 
        placeholder="Ex: 3 days in Paris..."
        style={{ padding: "10px", width: "300px", borderRadius: "5px", border: "1px solid #ccc" }}
      />
      <button onClick={askAI} style={{ padding: "10px 20px", marginLeft: "10px", cursor: "pointer" }}>
        Plan My Trip
      </button>
      <div style={{ marginTop: "30px", whiteSpace: "pre-wrap", textAlign: "left", maxWidth: "600px", margin: "30px auto" }}>
        {result}
      </div>
    </div>
  );
}
