Cypress.Commands.add('login', (username, password) => {
  cy.visit('/');
  cy.get('input[id=username]').type(username);
  cy.get('input[id=passwort]').type(password);
  cy.get('button[type=submit]').click();
});
