describe('Login Page E2E Tests', function() {
  beforeEach(function() {
    cy.fixture('login-data').then(function(data) {
      this.data = data;
    });
  });

  it('Successfully logs in with valid credentials', function() {
    cy.intercept({
            method: '*', // You can also use '*' to match all methods if needed
            url: /^http:\/\/localhost:([0-9]+)\/(.*)$/
        }, (req) => {

            req.url = req.url.replace('localhost', 'backend');

            // Continue with the modified request
            req.continue();
        }).as('dynamicRedirect');
    cy.visit('/');
    cy.get('input[id=username]').type(this.data.username);
    cy.get('input[id=passwort]').type(this.data.password);
    cy.get('button[type=submit]').click();
    cy.url().should('include', '/main');
  });
});