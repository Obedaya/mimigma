const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    // Base URL of your running application
    baseUrl: 'http://localhost:8080',

    // Where your test files are located
    specPattern: 'tests/e2e/*.cy.{js,jsx,ts,tsx}',

    // Enable or disable video recording of test runs.
    // Videos are highly useful for understanding test failures in CI environments
    video: false,

    // Enable or disable taking screenshots on test failure
    screenshotOnRunFailure: true,

    // Configuration for retries
    retries: {
      // Configure retry attempts for 'run' mode (non-interactive, typically in CI)
      runMode: 2,
      // Configure retry attempts for 'open' mode (interactive mode)
      openMode: 0,
    },

    // Set the viewport dimensions for all tests
    viewportWidth: 1280,
    viewportHeight: 720,

    // Custom environment variables
    env: {
      // Example: Define API URL to be used in tests
      apiUrl: 'http://localhost:3001/api',
    },

    // Modify browser launch arguments, preferences, and extensions
    setupNodeEvents(on, config) {
      // Implement event listeners here
      // Example: on('before:browser:launch', (browser = {}, launchOptions) => { ... })
    },
  },

  // Global configuration options
  projectId: 'your-project-id', // Optional: Used when recording runs to the Cypress Dashboard

  // Default browser to use for tests
  // Cypress supports 'chrome', 'firefox', 'electron', 'edge', etc.
  // You can also specify a browser path to use a specific version or type of browser
  browser: 'chrome',
});
