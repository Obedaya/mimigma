describe('Keyboard Click Test', () => {
  beforeEach(() => {
    cy.visit('/main', { timeout: 10000 });
    cy.login('admin', 'password');
  });

  it('should send the correct letter to the backend when a keyboard key is clicked', () => {
    const keys = ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O', 
                  'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
                  'P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L'];

    keys.forEach((key) => {
      cy.clickKeyAndWait(key);
    });
  });
});

