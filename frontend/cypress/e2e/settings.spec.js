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
        cy.get('button[id=modal-close-button]').click();
        cy.wait(200);
        cy.resetsettings();
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
        cy.wait(200);
        cy.resetsettings();
    });

    it('should change the rotor variant, depending on the rotor variant', () => {
        cy.get('button[id=DropdownRotor3]').click();
        cy.get('.variant-menu.show .dropdown-item.dropdown-variant').contains('II').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click();
        cy.get('div[id="settings-button"]').click();
        cy.get('.dropdown-menu.variant-menu').contains('II').should('exist');
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click();
        cy.wait(200);
        cy.resetsettings();
    });

    it('should change the rotor rotation, depending on the initial rotor setting', () => {
        cy.get('button[id=DropdownPosition3]').click();
        cy.get('.initial-menu.show .dropdown-item.dropdown-initial').contains('B').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click();
        cy.get('div[class=rotor_panel]').find('div[class=rotor]').eq(2).find('div[class=currentletter]').contains('B');
        cy.wait(200);
        cy.resetsettings();
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
        cy.resetsettings();
    });

    it('should change the rotor ring, depending on the initial ring setting', () => {
        cy.get('button[id=DropdownRing3]').click();
        cy.get('.ring-menu.show .dropdown-item.dropdown-ring').contains('2').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click();
        cy.get('div[id="settings-button"]').click();
        cy.get('.dropdown-menu.ring-menu').contains('2').should('exist');
        cy.get('button[id="reset-btn"]').contains('Reset').click();
    });
    it('should change the encrypted letter, depending on the ring setting', () => {
        cy.get('button[id=DropdownRing3]').click();
        cy.get('.ring-menu.show .dropdown-item.dropdown-ring').contains('2').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        cy.get('button[id=modal-close-button]').click();
        cy.get('body').trigger('keydown', {key: 'A'});
        cy.wait(100);
        cy.get('.lamp').contains('U').should('have.class', 'highlighted');
        cy.get('body').trigger('keyup', {key: 'U'});
        cy.resetsettings();
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
        cy.resetsettings();
    });

    it('should change the reflector, depending on the initial reflector setting', () => {
        cy.get('button[id=DropdownReflector]').click();
        cy.get('.dropdown-item.dropdown-reflector').contains('UKW_A').click();
        cy.wait(500)
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(500)
        //cy.get('button[id=modal-close-button]').click();
        cy.get('body').trigger('keydown', {key: 'A'});
        //cy.wait(100);
        cy.get('.lamp').contains('S').should('have.class', 'highlighted');
        cy.get('body').trigger('keyup', {key: 'S'});
        cy.resetsettings();
    });

    it('should remove the plugboard, depending on the plugboard setting', () => {
        cy.get('input[id=plugboardCheckbox]').click();
        cy.wait(500);
        cy.get('button[id=modal-submit-button]').click();
        // cy.get('button[id=modal-close-button]').click();
        cy.get('.plugboard').should('not.exist');
        cy.wait(200);
        cy.resetsettings();
    });

    it('should change and then reset the enigma settings when the reset button is pressed', () => {

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

        // Save the changes
        cy.get('button[id=modal-submit-button]').click();
        cy.wait(1000)

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
        cy.get('button[id=DropdownReflector]').should('contain', 'UKW_B');
        for (let i = 1; i < 3; i++) {
            cy.get(`button[id=DropdownRotor${i}]`).should('contain', 'I');
            cy.get(`button[id=DropdownPosition${i}]`).should('contain', 'A');
            cy.get(`button[id=DropdownRing${i}`).should('contain', '1');
        }
        cy.get('input[id=plugboardCheckbox]').should('be.checked');

        cy.get('button[id="reset-btn"]').contains('Reset').click();
    });

    it('should change settings for every enigma variant', () => {
        // Enigma I
        cy.get('select[id=enigmavariants]').select('Enigma I');
        cy.get('button[id=DropdownRotor3]').click();
        let rotorVariantsM1 = ['I', 'II', 'III', 'IV', 'V'];
        let reflectorVariantsM1 = ['UKW_A', 'UKW_B', 'UKW_C'];
        for (let i = 0; i < 5; i++) {
            cy.get('.variant-menu.show .dropdown-item.dropdown-variant').contains(rotorVariantsM1[i]);
        }
        for (let i = 0; i < 3; i++) {
            cy.get('.dropdown-item.dropdown-reflector').contains(reflectorVariantsM1[i]);
        }

        // Enigma M3
        cy.get('select[id=enigmavariants]').select('Enigma M3');
        cy.get('button[id=DropdownRotor3]').click();
        let rotorVariantsM3 = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII'];
        let reflectorVariantsM3 = ['UKW_B', 'UKW_C'];
        for (let i = 0; i < 8; i++) {
            cy.get('.variant-menu.show .dropdown-item.dropdown-variant').contains(rotorVariantsM3[i]);
        }
        for (let i = 0; i < 2; i++) {
            cy.get('.dropdown-item.dropdown-reflector').contains(reflectorVariantsM3[i]);
        }

        // Norway Enigma
        cy.get('select[id=enigmavariants]').select('Enigma Norway');
        cy.get('button[id=DropdownRotor3]').click();
        let rotorVariantsNorway = ['I', 'II', 'III', 'IV', 'V'];
        for (let i = 0; i < 3; i++) {
            cy.get('.variant-menu.show .dropdown-item.dropdown-variant').contains(rotorVariantsNorway[i]);
        }
        cy.get('.dropdown-item.dropdown-reflector').contains('UKW_N');

        // Custom Enigma
        cy.get('select[id=enigmavariants]').select('Custom Enigma');
        cy.get('button[id=DropdownRotor3]').click();
        let rotorVariantsCustom = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII'];
        let reflectorVariantsCustom = ['UKW_A', 'UKW_B', 'UKW_C', 'UKW_N'];
        for (let i = 0; i < 8; i++) {
            cy.get('.variant-menu.show .dropdown-item.dropdown-variant').contains(rotorVariantsCustom[i]);
        }
        for (let i = 0; i < 4; i++) {
            cy.get('.dropdown-item.dropdown-reflector').contains(reflectorVariantsCustom[i]);
        }
        cy.get('input[id=rotorCount]').should('exist');
        cy.get('button[id="reset-btn"]').contains('Reset').click();
    });

    it('should encrypt correctly with different enigma variants', () => {
        cy.get('select[id=enigmavariants]').select('Enigma I');
        cy.get('button[id=DropdownReflector]').click();
        cy.get('.dropdown-reflector').contains('UKW_A').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.get('button[id=modal-close-button]').click();

        cy.get('body').trigger('keydown', {key: 'A'});
        cy.wait(100);
        cy.get('.lamp').contains('S').should('have.class', 'highlighted');
        cy.get('body').trigger('keyup', {key: 'A'});

        cy.get('div[id="settings-button"]').click();
        cy.get('select[id=enigmavariants]').select('Enigma M3');
        cy.get('button[id=DropdownRotor3]').click();
        cy.get('.variant-menu.show .dropdown-item.dropdown-variant').contains('VIII').click();
        cy.get('button[id=modal-submit-button]').click();
        cy.get('button[id=modal-close-button]').click();

        cy.get('body').trigger('keydown', {key: 'A'});
        cy.wait(100);
        cy.get('.lamp').contains('R').should('have.class', 'highlighted');
        cy.get('body').trigger('keyup', {key: 'A'});

        cy.get('div[id="settings-button"]').click();
        cy.get('select[id=enigmavariants]').select('Enigma Norway');
        cy.wait(500);
        cy.get('button[id=modal-submit-button]').click();
        //cy.get('button[id=modal-close-button]').click();

        cy.get('body').trigger('keydown', {key: 'A'});
        cy.get('.lamp').contains('Q').should('have.class', 'highlighted');
        cy.get('body').trigger('keyup', {key: 'A'});

        cy.wait(200);
        cy.resetsettings();
    });


});
