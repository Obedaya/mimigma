describe('Login Page E2E Tests', function () {
    beforeEach(function () {
        cy.fixture('login-data').then(function (data) {
            this.data = data;
        });
    });

    it('Successfully logs in with valid credentials', function () {
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

    it('Fails to log in with invalid credentials', function () {
        cy.intercept({
            method: '*', // You can also use '*' to match all methods if needed
            url: /^http:\/\/localhost:([0-9]+)\/(.*)$/
        }, (req) => {

            req.url = req.url.replace('localhost', 'backend');

            // Continue with the modified request
            req.continue();
        }).as('dynamicRedirect');
        cy.visit('/');
        cy.get('input[id=username]').type('invalid');
        cy.get('input[id=passwort]').type('invalid');
        cy.get('button[type=submit]').click();
        cy.get('div[class=try-again]').should('exist');
    });

    it('Fails to log in with empty credentials', function () {
        cy.visit('/');
        cy.get('form[class=login-form]').within(() => {
            cy.log('Check if the form is invalid when empty');
            cy.get('input:invalid').should('have.length', 2);

            cy.log('Check if the form is invalid when only username is filled');
            cy.get('input[id=username]').type(this.data.username);
            cy.get('input:invalid').should('have.length', 1);

            cy.log('Check if the form is invalid when only password is filled');
            cy.get('input[id=username]').clear();
            cy.get('input[id=passwort]').type(this.data.password);
            cy.get('input:invalid').should('have.length', 1);
        });
    });
});