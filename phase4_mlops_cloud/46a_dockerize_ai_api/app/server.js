'use strict';

const express = require('express');

const app = express();
app.use(express.json({ limit: '1mb' }));

const PORT = Number(process.env.PORT || 3004);
const MODEL = process.env.MODEL_NAME || 'stub-v1';

app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'ok',
    service: 'ai-api',
    model: MODEL
  });
});

app.post('/ai', (req, res) => {
  const { user, prompt } = req.body || {};

  if (!user || !prompt) {
    return res.status(400).json({
      error: 'Missing required fields: user, prompt'
    });
  }

  const answer =
    `Stub summary for "${user}": ` +
    `Bearer tokens are used so clients can send a credential in the Authorization header ` +
    `to access protected resources without resending passwords each request.`;

  return res.status(200).json({
    model: MODEL,
    user,
    prompt,
    answer
  });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`[ai-api] listening on http://0.0.0.0:${PORT}`);
});