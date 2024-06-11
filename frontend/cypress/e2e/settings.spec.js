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
        // cy.get('button[id=modal-close-button]').click();
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').should('have.length', 4);

        cy.get('div[id="settings-button"]').click();
        cy.get('input[id=rotorCount]').clear().type('3');
        cy.get('button[id=modal-submit-button]').click();
        // cy.get('button[id=modal-close-button]').click();
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').should('have.length', 3);
    });

//     it('should change the rotor rotation, depending on the initial rotor setting', () => {
//         cy.get('button[id=DropdownPosition1]').click();
//         cy.get('a[class=dropdown-item]').contains('B').click();
//         cy.get('button[id=modal-submit-button]').click();
//         cy.get('button[id=modal-close-button]').click();
//         cy.get('div[class=rotor_panel]').find('div[class=rotor]').eq(0).find('div[class=currentletter]').contains('B');
//     });

    it('should send the correct rotor settings to the backend', () => {
        cy.get('button[id=modal-submit-button]').click();
        cy.get('button[id=modal-close-button]').click();
        cy.intercept('POST', '/rotor', {
            statusCode: 200,
            body: {
                "user_id": 4,
                "machine_type": "M3",
                "rotors": ["I", "I", "I"],
                "rotor_positions": "AAA",
                "ring_positions": "AAA"
            }
        });
    });
    it('should change the reflector, depending on the initial reflector setting', () => {
        cy.get('button[id=DropdownReflector]').click();
        cy.get('a[class=dropdown-item]').contains('B').click();
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
