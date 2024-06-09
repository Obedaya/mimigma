FROM cypress/browsers:latest

# Install Bun
RUN apt-get update && apt-get install -y curl
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:${PATH}"

# Install Cypress
RUN bun add cypress

# Setup workspace
WORKDIR /app
COPY . /app

CMD [ "bun", "cypress", "run" ]
