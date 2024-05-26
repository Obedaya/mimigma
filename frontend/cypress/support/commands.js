Cypress.Commands.add('login', (username, password) => {
  cy.visit('/');
  cy.get('input[id=username]').type(username);
  cy.get('input[id=passwort]').type(password);
  cy.get('button[type=submit]').click();
});

Cypress.Commands.add('clickKeyAndWait', (key) => {
  cy.intercept('POST', `/keyboard?key=${key}`).as(`keyPress${key}`);
  cy.get('.lower .key').contains(key).click();
  cy.wait(`@keyPress${key}`, { timeout: 10000 }).then((interception) => {
    cy.log(`Intercepted URL for ${key}: ${interception.request.url}`);
    expect(interception.request.url).to.include(`key=${key}`);
  });
});
