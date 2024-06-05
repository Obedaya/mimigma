describe('Output test', () => {
    beforeEach(() => {
        cy.visit('/main');
        cy.login('admin', 'password');
    });

    it('should display the letter in the output field when a keyboard button is pressed', () => {
        cy.intercept({
            method: '*', // You can also use '*' to match all methods if needed
            url: /^http:\/\/localhost:([0-9]+)\/(.*)$/
        }, (req) => {

            req.url = req.url.replace('localhost', 'backend');

            // Continue with the modified request
            req.continue();
        }).as('dynamicRedirect');

        cy.get('body').type('A');

        cy.get('#output').contains('A');
    });
});
