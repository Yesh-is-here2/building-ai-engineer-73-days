const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/health", (req, res) => {
  res.json({ ok: true, service: "phase3.40-api", at: new Date().toISOString() });
});

app.post("/echo", (req, res) => {
  const { name = "anonymous", message = "" } = req.body || {};
  res.json({
    ok: true,
    received: { name, message },
    reply: `Hello ${name}! I got your message: "${message}"`,
    at: new Date().toISOString(),
  });
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`API running on http://localhost:${PORT}`));
