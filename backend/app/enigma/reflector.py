import string
from .reflector_config import UKW_A, UKW_B, UKW_C, UKW_N

class Reflector:
    def __init__(self, variant):
        variants = {
            "UKW_A": UKW_A,
            "UKW_B": UKW_B,
            "UKW_C": UKW_C,
            "UKW_N": UKW_N
        }

        if variant in variants:
            self.variant_mapping = variants[variant]
        else:
            raise Exception(f"Invalid input: {variant}")

    # Expects A B C or N for the respective Enigma (reflector) variants 
    # A B or C for Enigma I or M3 and N for Enigma Nord
    def encrypt(self, input):
        if input in string.ascii_uppercase:
            return self.variant_mapping[input]
        else:
            raise Exception(f"Invalid input: {input}")

# Example usage:
# from reflector import Reflector
# r = Reflector("UKW_A")    # "UKW_A" is the Enigma Reflector Version
# r.encrypt("B")            # "B" is the letter to be 'encrypted'

