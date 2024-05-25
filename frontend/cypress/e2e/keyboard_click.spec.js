describe('Keyboard Click Test', () => {
  beforeEach(() => {
    cy.visit('/main');
  });

  it('should send the correct letter to the backend when a keyboard key is clicked', () => {
    // Intercept the backend request and alias it
    cy.intercept('POST', '/keyboard*').as('keyPress');

    // Define all the keys in the keyboard
    const keys = ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O', 
                  'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
                  'P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L'];

    // Loop through each key and click it
    keys.forEach((key) => {
      cy.get('.lower .key').contains(key).click();

      // Wait for the backend request and validate the query parameter
      cy.wait('@keyPress').then((interception) => {
        expect(interception.request.url).to.include(`key=${key}`);
      });

      // Optionally check that the key is highlighted correctly
      cy.get(`.lower .key:contains(${key})`).should('have.class', 'highlighted');
    });
  });
});

