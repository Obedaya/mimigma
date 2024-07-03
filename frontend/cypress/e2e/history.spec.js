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
        cy.resetsettings();
        cy.wait(1000);
        cy.get('button[id=modal-submit-button]').click();

        cy.wait(1000);
        cy.get('body').type('A');

        cy.get('#history').contains('A : B');
    });
    it('should only display 140 encrypted letter - key pairs', () => {
       var genArr = Array.from({length: 140}, (v, k) => k + 1)
        cy.wrap(genArr).each((index) => {
            cy.get('body').trigger('keydown', {key: 'A'});
            cy.wait(100);
            cy.get('body').trigger('keyup', {key: 'A'});
        })
        cy.get('#history').find('br').should('have.length', 140);
    });
});