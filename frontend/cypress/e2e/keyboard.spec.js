describe('Virtual Keyboard Test', () => {
    beforeEach(() => {
        cy.visit('/main');
        cy.login('admin', 'password');
    });

    it('should highlight the letter in the lamp panel when a keyboard button is pressed', () => {
        cy.intercept({
            method: '*', // You can also use '*' to match all methods if needed
            url: /^http:\/\/localhost:([0-9]+)\/(.*)$/
        }, (req) => {

            req.url = req.url.replace('localhost', 'backend');

            // Continue with the modified request
            req.continue();
        }).as('dynamicRedirect');

        cy.get('body').trigger('keydown', { key: 'A' });

        cy.get('.lamp').contains('D').should('have.class', 'highlighted');

        cy.get('body').trigger('keyup', { key: 'A' });

        cy.get('.lamp').contains('D').should('not.have.class', 'highlighted');
    });
});
