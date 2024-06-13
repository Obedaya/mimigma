describe('Virtual Keyboard Test', () => {
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

    it('should highlight the letter in the lamp panel when a keyboard button is pressed', () => {
        cy.get('body').trigger('keydown', {key: 'A'});

        cy.get('.lamp').contains('S').should('have.class', 'highlighted');

        cy.get('body').trigger('keyup', {key: 'A'});

        cy.get('.lamp').contains('S').should('not.have.class', 'highlighted');
    });

    it('should highlight a the right letter in the lamp panel when a keyboard button is pressed twice', () => {
        cy.get('body').trigger('keydown', {key: 'A'});
        cy.get('.lamp').contains('S').should('have.class', 'highlighted');
        cy.get('body').trigger('keyup', {key: 'A'});
        cy.get('.lamp').contains('S').should('not.have.class', 'highlighted');

        cy.get('body').trigger('keydown', {key: 'A'});
        cy.get('.lamp').contains('S').should('have.class', 'highlighted');
        cy.get('body').trigger('keyup', {key: 'A'});
        cy.get('.lamp').contains('S').should('not.have.class', 'highlighted');
    });

    it('should rotate the rotor when a keyboard button is pressed', () => {
        cy.get('body').trigger('keydown', {key: 'A'});
        cy.wait(100);
        cy.get('body').trigger('keyup', {key: 'A'});
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').eq(2).find('div[class=currentletter]').contains('B');
    });
    it('should rotate the second rotor when the first rotor completes a full rotation', () => {
        var genArr = Array.from({length: 26}, (v, k) => k + 1)
        cy.wrap(genArr).each((index) => {
            cy.get('body').trigger('keydown', {key: 'A'});
            cy.wait(100);
            cy.get('body').trigger('keyup', {key: 'A'});
        })
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').eq(1).find('div[class=currentletter]').contains('B');
    });

    it('should rotate the third rotor when the second rotor completes a full rotation', () => {
        cy.get('div[id="settings-button"]').click();
        cy.get('button[id=DropdownPosition3]').click();
        cy.get('.initial-menu.show .dropdown-item.dropdown-initial').contains('V').click();
        cy.get('button[id=DropdownPosition2]').click();
        cy.get('.initial-menu.show .dropdown-item.dropdown-initial').contains('E').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click({force: true});
        cy.get('body').trigger('keydown', {key: 'A'});
        cy.wait(100);
        cy.get('body').trigger('keyup', {key: 'A'});
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').eq(0).find('div[class=currentletter]').contains('B');
    });
});