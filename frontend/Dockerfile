FROM oven/bun:alpine

WORKDIR /app

COPY package.json ./
COPY bun.lockb ./
COPY vite.config.js ./
COPY index.html ./

# RUN bun install

COPY src ./src

EXPOSE 8080

RUN bun install

CMD ["bun", "dev", "--port", "8080", "--host"]

# Health Check (Add this at the end)
HEALTHCHECK --interval=5s --timeout=3s CMD curl -f http://localhost:8080/health || exit 1

