#from rotor import Rotor
#from reflector import Reflector
#from plugboard import Plugboard

class Enigma:
    def __init__(self): #, rotor_settings, reflector_settings, plugboard_settings):
        pass
   
   
    """def __init__(self, rotor_settings, reflector_settings, plugboard_settings):
        self.rotors = [Rotor(setting) for setting in rotor_settings]
        self.reflector = Reflector(reflector_settings)
        self.plugboard = Plugboard(plugboard_settings)
        
    def encrypt_letter(self, letter):
        #plugboard before the rotors
        letter = self.plugboard.swap(letter)
        
        #through the rotors forwards
        for rotor in self.rotors:
            letter = rotor.forward(letter)
        
        #through the reflector
        letter = self.reflector.reflect(letter)
        
        #through the rotors backwards
        for rotor in reversed(self.rotors):
            letter = rotor.backward(letter)
        
        #plugboard after the rotors
        letter = self.plugboard.swap(letter)
        
        #rotate the rotors
        self.rotate_rotors()
        
        return letter
    
    def rotate_rotors(self):
        #rotate the first rotor
        rotate_next = self.rotors[0].rotate()
        
        #cascading rotation of the rotors
        for i in range(1, len(self.rotors)):
            if rotate_next:
                rotate_next = self.rotors[i].rotate()
            else:
                break

    def encrypt_message(self, message):
        encrypted_message = ''
        for letter in message:
            if letter.isalpha():
                encrypted_message += self.encrypt_letter(letter.upper())
            else:
                encrypted_message += letter  #non-alphabetic characters are not encrypted
        return encrypted_message"""