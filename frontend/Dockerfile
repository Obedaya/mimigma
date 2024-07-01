FROM oven/bun:alpine

WORKDIR /app

# Update the package list and upgrade packages to fix vulnerabilities
RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
    libcrypto3=3.1.6-r0 \
    libssl3=3.1.6-r0

COPY package.json ./
COPY bun.lockb ./
COPY vite.config.js ./
COPY index.html ./

RUN bun install esbuild@0.22.0

# RUN bun install

COPY src ./src

EXPOSE 8080

RUN bun install

CMD ["bun", "dev", "--port", "8080", "--host"]

