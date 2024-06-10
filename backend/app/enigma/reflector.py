import string
from .reflector_config import UKW_A, UKW_B, UKW_C, UKW_N

class Reflector:
    def __init__(self, variant):
        self.variant = variant

    # Expects A B C or N for the respective Enigma (reflector) variants 
    # A B or C for Enigma I or M3 and N for Enigma Nord
    def encrypt(self, input):       
        if self.variant in ["A","B","C","N"] and input in list(string.ascii_uppercase):
             return(eval("UKW_" + self.variant + "[" + "input" +"]"))
        else:
            raise Exception("Invalid input.")
    
    # Example usage:
    # from reflector import Reflector
    # r = Reflector("A")    # "A" is Enigma the Enigma Version
    # r.encrypt("B")        # "B" is the letter to be 'encrypted'
