import { useMemo, useState } from "react";
import "./App.css";

const API_BASE =
  (import.meta?.env?.VITE_API_BASE || "http://localhost:3001").replace(/\/$/, "");

export default function App() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [data, setData] = useState(null);

  const [name, setName] = useState("Yesh");
  const [message, setMessage] = useState("Hello from UI");

  const payload = useMemo(
    () => ({ name: name.trim(), message: message.trim() }),
    [name, message]
  );

  async function callHealth() {
    setLoading(true);
    setError("");
    setData(null);
    try {
      const res = await fetch(`${API_BASE}/health`);
      if (!res.ok) throw new Error(`HTTP ${res.status} ${res.statusText}`);
      const json = await res.json();
      setData({ endpoint: "/health", json });
    } catch (e) {
      setError(String(e?.message || e));
    } finally {
      setLoading(false);
    }
  }

  // Optional: only works if your API has POST /echo (I’ll give you that below)
  async function callEcho() {
    setLoading(true);
    setError("");
    setData(null);
    try {
      const res = await fetch(`${API_BASE}/echo`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status} ${res.statusText}`);
      const json = await res.json();
      setData({ endpoint: "/echo", json });
    } catch (e) {
      setError(String(e?.message || e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ maxWidth: 820, margin: "40px auto", padding: 16 }}>
      <h1 style={{ marginBottom: 6 }}>Phase 3.40 — Frontend Calls API</h1>
      <p style={{ marginTop: 0, opacity: 0.8 }}>
        UI: <code>http://localhost:5173</code> → API: <code>{API_BASE}</code>
      </p>

      <div style={{ display: "grid", gap: 10, marginTop: 18 }}>
        <label>
          Name
          <input
            style={{ width: "100%", padding: 10, marginTop: 6 }}
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>

        <label>
          Message
          <input
            style={{ width: "100%", padding: 10, marginTop: 6 }}
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
        </label>

        <div style={{ display: "flex", gap: 10, marginTop: 8 }}>
          <button onClick={callHealth} disabled={loading}>
            {loading ? "Calling..." : "GET /health"}
          </button>

          <button onClick={callEcho} disabled={loading}>
            {loading ? "Calling..." : "POST /echo"}
          </button>
        </div>

        {error ? (
          <div style={{ padding: 12, border: "1px solid #f99" }}>
            <b>Error:</b> {error}
            <div style={{ marginTop: 6, opacity: 0.8 }}>
              If this is a CORS error, fix it in the API (next section).
            </div>
          </div>
        ) : null}

        <div style={{ marginTop: 8 }}>
          <h3 style={{ marginBottom: 6 }}>Response</h3>
          <pre
            style={{
              background: "#111",
              color: "#eee",
              padding: 14,
              borderRadius: 10,
              overflowX: "auto",
            }}
          >
            {data ? JSON.stringify(data, null, 2) : "No response yet."}
          </pre>
        </div>
      </div>
    </div>
  );
}