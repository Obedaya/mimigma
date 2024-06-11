import string
from .reflector_config import UKW_A, UKW_B, UKW_C, UKW_N

class Reflector:
    def __init__(self, variant):
        if variant in ["UKW_A","UKW_B","UKW_C","UKW_N"]:
            self.variant = variant
        else:
            raise Exception(f"Invalid input: {variant}")

    # Expects A B C or N for the respective Enigma (reflector) variants 
    # A B or C for Enigma I or M3 and N for Enigma Nord
    def encrypt(self, input):       
        if input in list(string.ascii_uppercase):
             return(eval(self.variant + "[" + "input" +"]"))
        else:
            raise Exception(f"Invalid input: {input}")
    
    # Example usage:
    # from reflector import Reflector
    # r = Reflector("UKW_A")    # "UKW_A" is the Enigma Reflector Version
    # r.encrypt("B")        # "B" is the letter to be 'encrypted'
