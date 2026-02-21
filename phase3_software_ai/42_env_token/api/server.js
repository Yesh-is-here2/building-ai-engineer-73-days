require("dotenv").config();
const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

const TOKEN = process.env.AUTH_TOKEN || "";

function requireBearer(req, res, next) {
  const hdr = req.headers.authorization || "";
  const expected = `Bearer ${TOKEN}`;
  if (!TOKEN) {
    return res.status(500).json({ ok: false, error: "Server misconfigured", hint: "Set AUTH_TOKEN in .env" });
  }
  if (hdr !== expected) {
    return res.status(401).json({ ok: false, error: "Unauthorized", hint: "Send header: Authorization: Bearer <token>" });
  }
  next();
}

app.get("/health", (req, res) => {
  res.json({ ok: true, service: "phase3.42-api", at: new Date().toISOString() });
});

app.get("/me", requireBearer, (req, res) => {
  res.json({ ok: true, user: "authorized", at: new Date().toISOString() });
});

const PORT = process.env.PORT || 3003;
app.listen(PORT, () => console.log(`API running on http://localhost:${PORT}`));
