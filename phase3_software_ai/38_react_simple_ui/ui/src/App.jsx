import { useMemo, useState } from "react";
import "./App.css";

export default function App() {
  const [name, setName] = useState("Yesh");
  const [message, setMessage] = useState("Hello UI");
  const [submitted, setSubmitted] = useState(null);

  const preview = useMemo(() => {
    return {
      name: name.trim(),
      message: message.trim(),
      atLocal: new Date().toLocaleString(),
      module: "3.38",
    };
  }, [name, message]);

  function onSubmit(e) {
    e.preventDefault();
    setSubmitted(preview);
  }

  return (
    <div style={{ maxWidth: 720, margin: "40px auto", padding: 16 }}>
      <h1>Phase 3.38 — React Simple UI</h1>

      <form onSubmit={onSubmit} style={{ display: "grid", gap: 12 }}>
        <label>
          Name
          <input
            value={name}
            onChange={(e) => setName(e.target.value)}
            style={{ width: "100%", padding: 10, marginTop: 6 }}
          />
        </label>

        <label>
          Message
          <input
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            style={{ width: "100%", padding: 10, marginTop: 6 }}
          />
        </label>

        <button type="submit" style={{ padding: 10 }}>
          Submit
        </button>
      </form>

      <h2 style={{ marginTop: 24 }}>Live Preview</h2>
      <pre style={{ background: "#111", color: "#ddd", padding: 12 }}>
        {JSON.stringify(preview, null, 2)}
      </pre>

      <h2 style={{ marginTop: 24 }}>Last Submitted</h2>
      {submitted ? (
        <pre style={{ background: "#111", color: "#ddd", padding: 12 }}>
          {JSON.stringify(submitted, null, 2)}
        </pre>
      ) : (
        <p>Nothing submitted yet.</p>
      )}
    </div>
  );
}