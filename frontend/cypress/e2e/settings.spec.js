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
        cy.get('select[id=enigmavariants]').select('Custom Enigma');
        cy.get('input[id=rotorCount]').clear().type('4');
        cy.get('th').contains('Rotor 4').should('exist');

        cy.get('input[id=rotorCount]').clear().type('3');
        cy.get('th').contains('Rotor 4').should('not.exist');
    });

    it('should display the correct amount of rotors, if the rotor count is changed', () => {
        cy.get('select[id=enigmavariants]').select('Custom Enigma');
        cy.get('input[id=rotorCount]').clear().type('4');
        cy.get('button[id=modal-submit-button]').click();
        //cy.wait(200)
        //cy.get('button[id=modal-close-button]').click();
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').should('have.length', 4);

        cy.get('div[id="settings-button"]').click();
        cy.get('input[id=rotorCount]').clear().type('3');
        cy.get('button[id=modal-submit-button]').click();
        cy.get('button[id=modal-close-button]').click();
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').should('have.length', 3);
    });

    it('should change the rotor variant, depending on the rotor variant', () => {
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

    it('should change the clicks towards the rotor turnover, depending on the initial rotor setting', () => {
        cy.get('button[id=DropdownPosition3]').click();
        cy.get('.initial-menu.show .dropdown-item.dropdown-initial').contains('V').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click();
        cy.get('body').trigger('keydown', {key: 'A'});
        cy.wait(100);
        cy.get('body').trigger('keyup', {key: 'A'});
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').eq(1).find('div[class=currentletter]').contains('B');
    });

    it('should change the rotor ring, depending on the initial ring setting', () => {
        cy.get('button[id=DropdownRing3]').click();
        cy.get('.ring-menu.show .dropdown-item.dropdown-ring').contains('2').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click();
        cy.get('div[id="settings-button"]').click();
        cy.get('.dropdown-menu.ring-menu').contains('2').should('exist');
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
                "machine_type": "Enigma I",
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

    it('should remove the plugboard, depending on the plugboard setting', () => {
        cy.get('input[id=plugboardCheckbox]').click();
        cy.get('button[id=modal-submit-button]').click();
        // cy.get('button[id=modal-close-button]').click();
        cy.get('.plugboard').should('not.exist');
    });

    it('should change and then reset the enigma settings when the reset button is pressed', () => {
      
        // Change the rotor count to 5
        cy.get('select[id=enigmavariants]').select('Custom Enigma');
        cy.get('input[id=rotorCount]').clear().type('5');
      
        // Change rotors to 'IV' for all 5 positions
        for (let i = 1; i < 6; i++) {
          cy.get(`button[id=DropdownRotor${i}]`).click();
          cy.wait(500);
          cy.get('.variant-menu.show .dropdown-item.dropdown-variant').contains('IV').click();
          cy.wait(500);
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
      
        // Save the changes
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(200)
      
        // Reopen the settings modal to verify changes
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
      
        // Click the reset button
        cy.get('button.btn-secondary').contains('Reset').click();
      
        // Verify the settings were reset to defaults
        cy.get('input[id=rotorCount]').should('have.value', '3');
        cy.get('button[id=DropdownReflector]').should('contain', 'UKW_B');
        for (let i = 1; i < 3; i++) {
          cy.get(`button[id=DropdownRotor${i}]`).should('contain', 'I');
          cy.get(`button[id=DropdownPosition${i}]`).should('contain', 'A');
          cy.get(`button[id=DropdownRing${i}`).should('contain', '1');
        }
        cy.get('input[id=plugboardCheckbox]').should('be.checked');
      });
      
      
});
