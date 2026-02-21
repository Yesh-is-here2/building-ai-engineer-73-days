const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

function aiStub(prompt) {
  const p = String(prompt || "").trim();

  if (!p) return { answer: "Please provide a prompt.", model: "stub-v1" };

  // tiny "ai-like" behaviors
  if (/summarize/i.test(p)) {
    return {
      model: "stub-v1",
      answer:
        "Summary (stub): Identify the main point, list 23 key details, and restate the conclusion in 12 lines.",
    };
  }

  if (/todo|plan|steps/i.test(p)) {
    return {
      model: "stub-v1",
      answer:
        "Plan (stub): 1) Define goal 2) Break into tasks 3) Implement smallest piece 4) Test 5) Iterate and document.",
    };
  }

  // default: echo + simple transformation
  return {
    model: "stub-v1",
    answer: `AI (stub) response: I received your prompt: "${p}". A good next step is to be more specific about inputs/outputs.`,
  };
}

app.get("/health", (req, res) => {
  res.json({ ok: true, service: "phase3.45-ai-api", at: new Date().toISOString() });
});

app.post("/ai", (req, res) => {
  const { prompt = "", user = "demo-user" } = req.body || {};
  const out = aiStub(prompt);
  res.json({
    ok: true,
    user,
    prompt,
    ...out,
    at: new Date().toISOString(),
  });
});

const PORT = process.env.PORT || 3004;
app.listen(PORT, () => console.log(`AI API running on http://localhost:${PORT}`));
