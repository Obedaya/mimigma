FROM cypress/browsers:node-20.14.0-chrome-126.0.6478.114-1-ff-127.0.1-edge-126.0.2592.61-1

# Install Bun
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:${PATH}"

# Install Cypress
RUN bun add cypress

# Setup workspace
WORKDIR /app
COPY . /app
RUN ls -al cypress/support
CMD [ "bun", "cypress", "run" ]
