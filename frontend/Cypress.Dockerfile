FROM node:14
RUN apt-get update && apt-get install -y \
    libgtk2.0-0 \
    libgtk-3-0 \
    libgbm-dev \
    libnotify-dev \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libasound2 \
    libxtst6 \
    xauth \
    xvfb

# Install Bun
RUN curl -fsSL https://bun.sh/install | bash

# Install Cypress
RUN bun add cypress

# Install npx with Bun
RUN bun add -g npx

# Set PATH after Bun and npx installation
ENV PATH="/usr/local/lib/node_modules/npm/bin:${PATH}"
ENV PATH="/root/.bun/bin:${PATH}"  

# Setup workspace
WORKDIR /e2e
COPY . .
