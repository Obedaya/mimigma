describe('Plugboard Test', () => {
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

    it('should highlight and connect two letters in the plugboard when two plugboard button are selected', () => {
        cy.get('.plugboard .plug').contains('A').click();
        cy.get('.plugboard .plug').contains('A').should('have.class', 'temporary');
        cy.get('.plugboard .plug').contains('B').click();
        cy.get('.plugboard .plug').contains('A').should('not.have.class', 'temporary');
        cy.get('.plugboard .plug').contains('B').should('have.class', 'red');
        cy.get('.plugboard .plug').contains('A').should('have.class', 'red');
    });

    it('should remove the connection between two letters in the plugboard when a selected plug is clicked', () => {
        cy.get('.plugboard .plug').contains('A').click();
        cy.get('.plugboard .plug').contains('B').click();
        cy.get('.plugboard .plug').contains('A').click();
        cy.get('.plugboard .plug').contains('A').should('not.have.class', 'red');
        cy.get('.plugboard .plug').contains('B').should('not.have.class', 'red');
    });

    it('should not connect two letters in the plugboard when the same plug is clicked twice', () => {
        cy.get('.plugboard .plug').contains('A').click();
        cy.get('.plugboard .plug').contains('A').click();
        cy.get('.plugboard .plug').contains('A').should('not.have.class', 'red');
        cy.get('.plugboard .plug').contains('A').should('not.have.class', 'temporary');
    });

    it('should not connect more than 5 pairs of letters in the plugboard', () => {
        cy.get('.plugboard .plug').contains('A').click();
        cy.get('.plugboard .plug').contains('B').click();
        cy.get('.plugboard .plug').contains('C').click();
        cy.get('.plugboard .plug').contains('D').click();
        cy.get('.plugboard .plug').contains('E').click();
        cy.get('.plugboard .plug').contains('F').click();
        cy.get('.plugboard .plug').contains('G').click();
        cy.get('.plugboard .plug').contains('H').click();
        cy.get('.plugboard .plug').contains('I').click();
        cy.get('.plugboard .plug').contains('J').click();

        cy.get('.plugboard .plug').contains('K').click();
        cy.get('.plugboard_alert').should('exist');
    });

    it('should change the encrypted letter, when a plug pair is selected', () => {
        cy.get('.plugboard .plug').contains('A').click();
        cy.get('.plugboard .plug').contains('B').click();
        cy.get('body').trigger('keydown', {key: 'A'});
        cy.get('.lamp').contains('B').should('have.class', 'highlighted');
        cy.get('body').trigger('keyup', {key: 'A'});
        cy.get('.lamp').contains('B').should('not.have.class', 'highlighted');
    });
});