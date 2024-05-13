describe('Login Page E2E Tests', function() {
  beforeEach(function() {
    cy.fixture('login-data').then(function(data) {
      this.data = data;
    });
  });

  it('Successfully logs in with valid credentials', function() {
    cy.visit('/');
    cy.get('input[id=username]').type(this.data.username);
    cy.get('input[id=passwort]').type(this.data.password);
    cy.get('button[type=submit]').click();
    //cy.url().should('include', '/main');
  });
});