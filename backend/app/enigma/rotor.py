# ROTOR.py
from ..crud import get_rotor_settings
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models import RotorSettings
from ..database import get_db

def get_rotor_settings_from_db(user_id: int, db: Session) -> tuple:
    settings = db.query(RotorSettings).filter(RotorSettings.user_id == user_id).first()
    if settings is None:
        raise HTTPException(status_code=404, detail="Settings not found")

    # Extracting values from RotorSettings object
    machine_type = settings.machine_type
    rotors = settings.rotors
    rotor_positions = settings.rotor_positions
    ring_positions = settings.ring_positions

    return machine_type, rotors, rotor_positions, ring_positions

class RotorMachine:
    def __init__(self, machine_type, rotors, rotor_positions, ring_positions):
        self.machine_type = machine_type  # Type of Enigma machine (M1, M3, Norway)
        self.rotors = rotors  # List of rotors (e.g., ["I", "II", "III"])
        
        # Initial rotor positions (e.g., "AAA" -> [0, 0, 0])
        self.rotor_positions = [ord(pos) - ord('A') for pos in rotor_positions]
        
        # Ring settings positions (e.g., "AAA" -> [0, 0, 0])
        self.ring_positions = [ord(pos) - ord('A') for pos in ring_positions]
        
        # Determine the appropriate Enigma machine class
        self.machine = self.get_machine_class()

        # Initialize notches and turnovers for each rotor
        self.notches = []
        self.turnovers = []
        for rotor in self.rotors:
            rotor_method = self.get_rotor_method(rotor)
            _, notch, turnover = rotor_method('A')
            self.notches.append(ord(notch) - ord('A'))
            self.turnovers.append(turnover)

    def get_machine_class(self):
        if self.machine_type == "M1":
            return EnigmaM1
        elif self.machine_type == "M3":
            return EnigmaM3
        elif self.machine_type == "NW":
            return EnigmaNorway
        else:
            raise ValueError("Unknown machine type")

    def get_rotor_method(self, rotor):
        return getattr(self.machine, f"rotor_{rotor}")

    def advance_rotors(self):
        # Initial advancement (rightmost rotor always advances)
        advance_next = True

        for i in range(len(self.rotors)):
            if advance_next:
                self.rotor_positions[i] = (self.rotor_positions[i] + 1) % 26
                advance_next = self.rotor_positions[i] == self.notches[i]

    def encrypt_letter(self, letter):
        # Encryption forward (through the rotors to the reflector)
        for i, rotor in enumerate(self.rotors):
            # Calculate the shift taking into account rotor and ring positions
            shifted_position = (self.rotor_positions[i] - self.ring_positions[i]) % 26
            rotor_method = self.get_rotor_method(rotor)
            letter, _, _ = rotor_method(letter, shifted_position)
            
            # Adjust the result taking into account the ring position
            letter = chr((ord(letter) - ord('A') + self.ring_positions[i]) % 26 + ord('A'))
        

        return letter

    def encrypt_letter_reverse(self, letter):
        # Encryption reverse (back through the rotors from the reflector)
        for i in reversed(range(len(self.rotors))):
            # Calculate the shift taking into account rotor and ring positions
            shifted_position = (self.rotor_positions[i] - self.ring_positions[i]) % 26
            rotor_method = self.get_rotor_method(self.rotors[i])
            letter, _, _ = rotor_method(letter, shifted_position, reverse=True)
            
            # Adjust the result taking into account the ring position
            letter = chr((ord(letter) - ord('A') + self.ring_positions[i]) % 26 + ord('A'))
        
        return letter

class EnigmaM1:
    @staticmethod
    def rotor_I(letter, position=0):
        wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        notch = "Y"
        turnover = "Q"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_II(letter, position=0):
        wiring = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        notch = "M"
        turnover = "E"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_III(letter, position=0):
        wiring = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        notch = "D"
        turnover = "V"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_IV(letter, position=0):
        wiring = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
        notch = "R"
        turnover = "J"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_V(letter, position=0):
        wiring = "VZBRGITYUPSDNHLXAWMJQOFECK"
        notch = "H"
        turnover = "Z"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover


class EnigmaM3:
    @staticmethod
    def rotor_I(letter, position=0):
        return EnigmaM1.rotor_I(letter, position)

    @staticmethod
    def rotor_II(letter, position=0):
        return EnigmaM1.rotor_II(letter, position)

    @staticmethod
    def rotor_III(letter, position=0):
        return EnigmaM1.rotor_III(letter, position)

    @staticmethod
    def rotor_IV(letter, position=0):
        return EnigmaM1.rotor_IV(letter, position)

    @staticmethod
    def rotor_V(letter, position=0):
        return EnigmaM1.rotor_V(letter, position)

    @staticmethod
    def rotor_VI(letter, position=0):
        wiring = "JPGVOUMFYQBENHZRDKASXLICTW"
        notch = "HU"
        turnover = "ZM"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_VII(letter, position=0):
        wiring = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
        notch = "HU"
        turnover = "ZM"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_VIII(letter, position=0):
        wiring = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
        notch = "HU"
        turnover = "ZM"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover


class EnigmaNorway:
    @staticmethod
    def rotor_I(letter, position=0):
        wiring = "WTOKASUYVRBXJHQCPZEFMDINLG"
        notch = "Y"
        turnover = "Q"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_II(letter, position=0):
        wiring = "GJLPUBSWEMCTQVHXAOFZDRKYNI"
        notch = "M"
        turnover = "E"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_III(letter, position=0):
        wiring = "JWFMHNBPUSDYTIXVZGRQLAOEKC"
        notch = "D"
        turnover = "V"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover
    
    @staticmethod
    def rotor_IV(letter, position=0):
        wiring = "FGZJMVXEPBWSHQTLIUDYKCNRAO"
        notch = "R"
        turnover = "V"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover
    
    @staticmethod
    def rotor_V(letter, position=0):
        wiring = "HEJXQOTZBVFDASCILWPGYNMURK"
        notch = "H"
        turnover = "Z"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + position) % 26
        encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover


# Utility function to advance the rotor
def advance_rotor(position):
    new_position = (position + 1) % 26
    return new_position

"""
# Example usage
user_id = 1
db_session = Session()

# Retrieve rotor settings from the database
machine_type, rotors, rotor_positions, ring_positions = get_rotor_settings_from_db(user_id, db_session)

# Create a RotorMachine instance with retrieved settings
rotor_machine = RotorMachine(machine_type, rotors, rotor_positions, ring_positions)

# Now you can use rotor_machine to encrypt or decrypt messages
encrypted_letter = rotor_machine.encrypt_letter("A")
reverse_letter = rotor_machine.encrypt_letter_reverse("X")
print(f"Encrypted letter: {encrypted_letter}")

# Close the database session when done
#db_session.close()

"""