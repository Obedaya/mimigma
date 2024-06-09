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

Cypress.Commands.add('clickKeyAndWait', (key) => {
    cy.intercept({
        method: '*', // You can also use '*' to match all methods if needed
        url: /^http:\/\/localhost:([0-9]+)\/(.*)$/
    }, (req) => {

        req.url = req.url.replace('localhost', 'backend');

        // Continue with the modified request
        req.continue();
    }).as('dynamicRedirect');
    cy.intercept('POST', `/keyboard?key=${key}`).as(`keyPress${key}`);
    cy.wait(1000);
    cy.get('.lower .key').contains(key).click();
    cy.wait(`@keyPress${key}`, {timeout: 10000}).then((interception) => {
        cy.log(`Intercepted URL for ${key}: ${interception.request.url}`);
        expect(interception.request.url).to.include(`key=${key}`);
    });
});
