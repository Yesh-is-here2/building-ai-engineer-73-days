# syntax=docker/dockerfile:1

FROM node:20-alpine

RUN addgroup -S app && adduser -S app -G app

WORKDIR /app

COPY app/package*.json ./
RUN npm ci --omit=dev

COPY app/server.js ./server.js

ENV NODE_ENV=production
ENV PORT=3004
ENV MODEL_NAME=stub-v1

EXPOSE 3004

HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD wget -qO- http://127.0.0.1:3004/health || exit 1

USER app

CMD ["npm", "start"]