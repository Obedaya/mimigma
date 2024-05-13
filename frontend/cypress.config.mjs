import { defineConfig } from 'cypress';

export default defineConfig({
  e2e: {
    baseUrl: 'http://frontend:8080',
    specPattern: 'cypress/e2e/*.spec.{js,jsx,ts,tsx}',
    video: true,
    screenshotsFolder: 'cypress/screenshots',
    videosFolder: 'cypress/videos',
    fixturesFolder: 'cypress/fixtures',
    supportFile: 'cypress/support/index.js',
  },
});
