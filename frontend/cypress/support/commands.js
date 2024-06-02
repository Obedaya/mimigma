Cypress.Commands.add('login', (username, password) => {
  cy.intercept({
            method: '*', // You can also use '*' to match all methods if needed
            url: /^http:\/\/localhost:([0-9]+)\/(.*)$/
        }, (req) => {

            req.url = req.url.replace('localhost', 'backend');

            // Continue with the modified request
            req.continue();
        }).as('dynamicRedirect');
  cy.visit('/');
  cy.get('input[id=username]').type(username);
  cy.get('input[id=passwort]').type(password);
  cy.get('button[type=submit]').click();
});
