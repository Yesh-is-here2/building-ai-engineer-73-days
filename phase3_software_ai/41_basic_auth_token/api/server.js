const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

const TOKEN = process.env.API_TOKEN || "devtoken123";

// middleware: require Bearer token
function requireAuth(req, res, next) {
  const auth = req.headers.authorization || "";
  const [scheme, token] = auth.split(" ");
  if (scheme !== "Bearer" || token !== TOKEN) {
    return res.status(401).json({
      ok: false,
      error: "Unauthorized",
      hint: 'Send header: Authorization: Bearer <token>',
    });
  }
  next();
}

// public route (no token)
app.get("/health", (req, res) => {
  res.json({ ok: true, service: "phase3.41-api", at: new Date().toISOString() });
});

// protected routes
app.get("/me", requireAuth, (req, res) => {
  res.json({ ok: true, user: "authorized", at: new Date().toISOString() });
});

app.post("/echo", requireAuth, (req, res) => {
  const { name = "anonymous", message = "" } = req.body || {};
  res.json({
    ok: true,
    received: { name, message },
    reply: `Hello ${name}! Token auth passed.`,
    at: new Date().toISOString(),
  });
});

const PORT = process.env.PORT || 3002;
app.listen(PORT, () => console.log(`API running on http://localhost:${PORT}`));
