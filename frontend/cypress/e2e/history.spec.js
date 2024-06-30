describe('History', () => {
    beforeEach(() => {
        cy.visit('/main');
        cy.login('admin', 'password');
        cy.intercept({
            method: '*', // You can also use '*' to match all methods if needed
            url: /^http:\/\/localhost:([0-9]+)\/(.*)$/
        }, (req) => {

            req.url = req.url.replace('localhost', 'backend');

            // Continue with the modified request
            req.continue();
        }).as('dynamicRedirect');
    });
    afterEach(() => {
        cy.resetsettings();
    });

    it('should display the letter and encrypted letter in the output field when a keyboard button is pressed', () => {
        cy.wait(1000);
        cy.get('body').type('A');

        cy.get('#history').contains('A : B');
    });
});