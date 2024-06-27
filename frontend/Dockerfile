FROM oven/bun:canary-alpine

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

