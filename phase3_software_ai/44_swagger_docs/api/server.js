const express = require("express");
const cors = require("cors");
const swaggerUi = require("swagger-ui-express");
const swaggerJsdoc = require("swagger-jsdoc");

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 3004;

// OpenAPI spec via JSDoc
const swaggerSpec = swaggerJsdoc({
  definition: {
    openapi: "3.0.0",
    info: {
      title: "Phase 3.44 - Swagger Docs API",
      version: "1.0.0",
      description: "Simple Express API documented using Swagger (OpenAPI 3.0).",
    },
    servers: [{ url: `http://localhost:${PORT}` }],
  },
  apis: [__filename],
});

// Serve raw spec + Swagger UI
app.get("/openapi.json", (req, res) => res.json(swaggerSpec));
app.use("/docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));

// Nice root page (prevents 'Cannot GET /')
app.get("/", (req, res) => {
  res.type("text").send(
    [
      "Phase 3.44 - Swagger Docs API",
      `Health: http://localhost:${PORT}/health`,
      `Swagger UI: http://localhost:${PORT}/docs`,
      `OpenAPI JSON: http://localhost:${PORT}/openapi.json`,
    ].join("\n")
  );
});

/**
 * @openapi
 * /health:
 *   get:
 *     summary: Health check
 *     description: Returns service status and timestamp.
 *     responses:
 *       200:
 *         description: OK
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 ok: { type: boolean }
 *                 service: { type: string }
 *                 at: { type: string }
 */
app.get("/health", (req, res) => {
  res.json({ ok: true, service: "phase3.44-swagger-api", at: new Date().toISOString() });
});

/**
 * @openapi
 * /echo:
 *   post:
 *     summary: Echo message
 *     description: Returns back the name/message and a friendly reply.
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               name: { type: string, example: "Yesh" }
 *               message: { type: string, example: "Hello from Swagger" }
 *     responses:
 *       200:
 *         description: Echo response
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 ok: { type: boolean }
 *                 received:
 *                   type: object
 *                   properties:
 *                     name: { type: string }
 *                     message: { type: string }
 *                 reply: { type: string }
 *                 at: { type: string }
 */
app.post("/echo", (req, res) => {
  const { name = "anonymous", message = "" } = req.body || {};
  res.json({
    ok: true,
    received: { name, message },
    reply: `Hello ${name}! I got your message: "${message}"`,
    at: new Date().toISOString(),
  });
});

app.listen(PORT, () => {
  console.log(`API running on http://localhost:${PORT}`);
  console.log(`Swagger UI on http://localhost:${PORT}/docs`);
});
