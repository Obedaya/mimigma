# Use the oven/bun:alpine image as a base
FROM oven/bun:alpine AS builder

WORKDIR /app

# Install required Alpine packages to address CVEs
RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
    libcrypto3=3.1.6-r0 \
    libssl3=3.1.6-r0

# Copy package files
COPY package.json ./
COPY bun.lockb ./

# Install dependencies
RUN bun install

# Remove esbuild from node_modules if installed
RUN rm -rf node_modules/esbuild

# Copy application files
COPY vite.config.js ./
COPY index.html ./
COPY src ./src

# Create an image without build dependencies
FROM oven/bun:alpine

WORKDIR /app

# Install required Alpine packages to address CVEs
RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
    libcrypto3=3.1.6-r0 \
    libssl3=3.1.6-r0

# Copy only the necessary files from the builder stage
COPY --from=builder /app /app

# Ensure esbuild is removed in the final image
RUN rm -rf node_modules/esbuild

EXPOSE 8080

CMD ["bun", "dev", "--port", "8080", "--host"]