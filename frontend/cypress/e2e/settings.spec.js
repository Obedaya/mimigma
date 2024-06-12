describe('Settings', () => {
    beforeEach(() => {
        cy.visit('/main');
        cy.login('admin', 'password');
        cy.get('div[id="settings-button"]').click();
        cy.intercept({
            method: '*', // You can also use '*' to match all methods if needed
            url: /^http:\/\/localhost:([0-9]+)\/(.*)$/
        }, (req) => {

            req.url = req.url.replace('localhost', 'backend');

            // Continue with the modified request
            req.continue();
        }).as('dynamicRedirect');
    });

    it('should change rotor settings, when the rotor count is changed', () => {
        cy.get('input[id=rotorCount]').clear().type('4');
        cy.get('th').contains('Rotor 4').should('exist');

        cy.get('input[id=rotorCount]').clear().type('3');
        cy.get('th').contains('Rotor 4').should('not.exist');
    });

    it('should display the correct amount of rotors, if the rotor count is changed', () => {
        cy.get('input[id=rotorCount]').clear().type('4');
        cy.get('button[id=modal-submit-button]').click();
        cy.get('button[id=modal-close-button]').click();
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').should('have.length', 4);

        cy.get('div[id="settings-button"]').click();
        cy.get('input[id=rotorCount]').clear().type('3');
        cy.get('button[id=modal-submit-button]').click();
        cy.get('button[id=modal-close-button]').click();
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').should('have.length', 3);
    });

    it('should change the rotor variant, depending on the initial rotor setting', () => {
        cy.get('button[id=DropdownRotor3]').click();
        cy.get('.variant-menu.show .dropdown-item.dropdown-variant').contains('II').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click();
        cy.get('div[id="settings-button"]').click();
        cy.get('.dropdown-menu.variant-menu').contains('II').should('exist');
    });

    it('should change the rotor rotation, depending on the initial rotor setting', () => {
        cy.get('button[id=DropdownPosition3]').click();
        cy.get('.initial-menu.show .dropdown-item.dropdown-initial').contains('B').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click();
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').eq(2).find('div[class=currentletter]').contains('B');
    });

    it('should change the rotor ring, depending on the initial ring setting', () => {
        cy.get('button[id=DropdownRing3]').click();
        cy.get('.ring-menu.show .dropdown-item.dropdown-ring').contains('B').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click();
        cy.get('div[id="settings-button"]').click();
        cy.get('.dropdown-menu.ring-menu').contains('B').should('exist');
    });

    it('should change the rotor turnover, depending on the initial rotor variant', () => {
        cy.get('button[id=DropdownRotor3]').click();
        cy.get('.variant-menu.show .dropdown-item.dropdown-variant').contains('I').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click();
        var genArr = Array.from({length: 17}, (v, k) => k + 1)
        cy.wrap(genArr).each((index) => {
            cy.get('body').trigger('keydown', {key: 'A'});
            cy.wait(100);
            cy.get('body').trigger('keyup', {key: 'A'});
        })
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').eq(2).find('div[class=currentletter]').contains('R');
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').eq(1).find('div[class=currentletter]').contains('B');
    });

    it('should send the correct rotor settings to the backend', () => {
        cy.get('button[id=modal-submit-button]').click();
        cy.get('button[id=modal-close-button]').click();
        cy.intercept('POST', '/rotor', {
            statusCode: 200,
            body: {
                "user_id": 4,
                "machine_type": "M3",
                "rotors": ["I", "II", "III"],
                "rotor_positions": "AAA",
                "ring_positions": "AAA"
            }
        });
    });
    it('should change the reflector, depending on the initial reflector setting', () => {
        cy.get('button[id=DropdownReflector]').click();
        cy.get('.dropdown-item.dropdown-reflector').contains('B').click();
        cy.get('button[id=modal-submit-button]').click();
        // cy.get('button[id=modal-close-button]').click();
    });

    it('should send the correct reflector settings to the backend', () => {
        cy.get('button[id=modal-submit-button]').click();
        // cy.get('button[id=modal-close-button]').click();
        cy.intercept('POST', '/reflector', {
            statusCode: 200,
        });
    });
});
