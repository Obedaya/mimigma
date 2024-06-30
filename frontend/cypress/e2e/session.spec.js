describe('Session Test', () => {
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

    it('should save the settings, after reload', () => {
        cy.get('div[id="settings-button"]').click();
        // Change the rotor count to 5
        cy.get('select[id=enigmavariants]').select('Custom Enigma');
        cy.get('input[id=rotorCount]').clear().type('5');

        // Change rotors to 'IV' for all 5 positions
        for (let i = 1; i < 6; i++) {
            cy.get(`button[id=DropdownRotor${i}]`).click();
            cy.get('.variant-menu.show .dropdown-item.dropdown-variant').contains('IV').click();
        }

        // Change initial positions to 'B' for all 5 positions
        for (let i = 1; i < 6; i++) {
            cy.get(`button[id=DropdownPosition${i}]`).click();
            cy.get('.initial-menu.show .dropdown-item.dropdown-initial').contains('B').click();

        }

        // Change ring positions to '2' for all 5 positions
        for (let i = 1; i < 6; i++) {
            cy.get(`button[id=DropdownRing${i}]`).click();
            cy.get('.ring-menu.show .dropdown-item.dropdown-ring').contains('2').click();
        }

        // Change the reflector to 'UKW_C'
        cy.get('button[id=DropdownReflector]').click();
        cy.get('.dropdown-reflector').contains('UKW_C').click();

        // Uncheck the plugboard
        cy.get('input[id=plugboardCheckbox]').uncheck();

        cy.wait(500);
        // Save the changes
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500);

        cy.reload();
        cy.wait(5000);

        cy.get('div[id="settings-button"]').click();

        // Verify the changes were applied
        cy.get('input[id=rotorCount]').should('have.value', '5');
        cy.get('button[id=DropdownReflector]').should('contain', 'UKW_C');

        for (let i = 1; i < 6; i++) {
            cy.get(`button[id=DropdownRotor${i}]`).should('contain', 'IV');
            cy.get(`button[id=DropdownPosition${i}]`).should('contain', 'B');
            cy.get(`button[id=DropdownRing${i}`).should('contain', '2');
        }
        cy.get('input[id=plugboardCheckbox]').should('not.be.checked');
    });

    it('should save the plugboard settings, after reload', () => {
        wait(100);
        cy.get('.plugboard .plug').contains('A').click();
        cy.get('.plugboard .plug').contains('B').click();
        cy.get('.plugboard .plug').contains('B').should('have.class', 'red');
        cy.get('.plugboard .plug').contains('A').should('have.class', 'red');
        cy.reload();
        cy.wait(5000);
        cy.get('.plugboard .plug').contains('B').should('have.class', 'red');
        cy.get('.plugboard .plug').contains('A').should('have.class', 'red');
    });

    it('should save the history, after reload', () => {
        cy.get('body').trigger('keydown', {key: 'A'});
        cy.wait(100);
        cy.get('body').trigger('keyup', {key: 'A'});
        cy.get('#history').contains('B');
        cy.reload();
        cy.wait(5000);
        cy.get('#history').contains('B');
    });

    it('should save the output, after reload', () => {
        cy.get('body').trigger('keydown', {key: 'A'});
        cy.wait(100);
        cy.get('body').trigger('keyup', {key: 'A'});
        cy.get('#output').contains('A : B');
        cy.reload();
        cy.wait(5000);
        cy.get('#output').contains('A : B');
    });
});
