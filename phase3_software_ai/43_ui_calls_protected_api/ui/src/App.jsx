import { useState } from "react";
import "./App.css";

const API_BASE = "http://localhost:3003"; // your Phase 3.42 server

export default function App() {
  const [token, setToken] = useState("devtoken123");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function callHealth() {
    setError("");
    setResult(null);
    try {
      const r = await fetch(`${API_BASE}/health`);
      const json = await r.json();
      setResult({ endpoint: "/health", status: r.status, json });
    } catch (e) {
      setError(String(e));
    }
  }

  async function callMe() {
    setError("");
    setResult(null);
    try {
      const r = await fetch(`${API_BASE}/me`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      const json = await r.json();
      setResult({ endpoint: "/me", status: r.status, json });
    } catch (e) {
      setError(String(e));
    }
  }

  return (
    <div style={{ maxWidth: 900, margin: "60px auto", padding: 20 }}>
      <h1 style={{ textAlign: "center" }}>Phase 3.43 — UI Calls Protected API</h1>
      <p style={{ textAlign: "center", opacity: 0.7 }}>
        UI: http://localhost:5173 → API: {API_BASE}
      </p>

      <div style={{ display: "grid", gap: 12, marginTop: 24 }}>
        <label>
          Token (Bearer):
          <input
            value={token}
            onChange={(e) => setToken(e.target.value)}
            style={{ width: "100%", padding: 10, marginTop: 6 }}
            placeholder="devtoken123"
          />
        </label>

        <div style={{ display: "flex", gap: 10 }}>
          <button onClick={callHealth}>GET /health</button>
          <button onClick={callMe}>GET /me (protected)</button>
        </div>

        <h3>Response</h3>
        <pre
          style={{
            background: "#111",
            color: "#eee",
            padding: 16,
            borderRadius: 10,
            minHeight: 160,
            overflow: "auto",
          }}
        >
          {error
            ? `ERROR:\n${error}`
            : result
            ? JSON.stringify(result, null, 2)
            : "No response yet."}
        </pre>
      </div>
    </div>
  );
}