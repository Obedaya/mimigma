# Use the oven/bun image as a base
FROM oven/bun:alpine AS builder

WORKDIR /app

# Install build dependencies
COPY package.json ./
COPY bun.lockb ./
COPY vite.config.js ./
COPY index.html ./

RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
    libcrypto3=3.1.6-r0 \
    libssl3=3.1.6-r0

# Install dependencies
RUN bun install

# Remove esbuild from node_modules 
RUN rm -rf node_modules/esbuild

COPY src ./src

# Create a smaller final image without build dependencies
FROM oven/bun:alpine

WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /app /app

EXPOSE 8080

CMD ["bun", "dev", "--port", "8080", "--host"]
