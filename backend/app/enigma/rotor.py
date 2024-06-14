from sqlalchemy.orm import Session
from ..crud import get_rotor_settings
from fastapi import HTTPException
from ..models import RotorSettings

def get_rotor_settings_from_db(user_id: int, db: Session) -> tuple:
    settings = db.query(RotorSettings).filter(RotorSettings.user_id == user_id).first()
    if settings is None:
        raise HTTPException(status_code=404, detail="Settings not found")

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
        # self.turnovers = []
        for rotor in self.rotors:
            rotor_method = self.get_rotor_method(rotor)
            _, notch, _ = rotor_method('A')
            self.notches.append(ord(notch) - ord('A'))


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

    """def advance_rotors(self):
        # Initial advancement (rightmost rotor always advances)
        advance_next = True

        for i in range(len(self.rotors)):
            if advance_next:
                self.rotor_positions[i] = (self.rotor_positions[i] + 1) % 26
                advance_next = self.rotor_positions[i] == self.notches[i]
            else:
                break"""

    def advance_rotors(self):
        advance_next = True

        for i in reversed(range(len(self.rotors))):
            if advance_next:
                self.rotor_positions[i] = (self.rotor_positions[i] + 1) % 26
                advance_next = self.rotor_positions[i] == self.notches[i]
            else:
                break

    def encrypt_letter(self, letter):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, rotor in enumerate(self.rotors):
            shift = (self.rotor_positions[i] + self.ring_positions[i]) % 26
            rotor_method = self.get_rotor_method(rotor)
            index = (alphabet.index(letter) + shift) % 26
            letter, _, _ = rotor_method(alphabet[index])
            
            # Adjust the result taking into account the ring position
            letter = chr((ord(letter) - ord('A') - self.ring_positions[i]) % 26 + ord('A'))
        
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
    def rotor_I(letter, position=0, reverse=False):
        wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "Y"
        turnover = "Q"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_II(letter, position=0, reverse=False):
        wiring = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "M"
        turnover = "E"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_III(letter, position=0, reverse=False):
        wiring = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "D"
        turnover = "V"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_IV(letter, position=0, reverse=False):
        wiring = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "R"
        turnover = "J"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_V(letter, position=0, reverse=False):
        wiring = "VZBRGITYUPSDNHLXAWMJQOFECK"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "H"
        turnover = "Z"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

class EnigmaM3:
    @staticmethod
    def rotor_I(letter, position=0, reverse=False):
        return EnigmaM1.rotor_I(letter, position, reverse)

    @staticmethod
    def rotor_II(letter, position=0, reverse=False):
        return EnigmaM1.rotor_II(letter, position, reverse)

    @staticmethod
    def rotor_III(letter, position=0, reverse=False):
        return EnigmaM1.rotor_III(letter, position, reverse)

    @staticmethod
    def rotor_IV(letter, position=0, reverse=False):
        return EnigmaM1.rotor_IV(letter, position, reverse)

    @staticmethod
    def rotor_V(letter, position=0, reverse=False):
        return EnigmaM1.rotor_V(letter, position, reverse)

    @staticmethod
    def rotor_VI(letter, position=0, reverse=False):
        wiring = "JPGVOUMFYQBENHZRDKASXLICTW"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "HU"
        turnover = "ZM"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_VII(letter, position=0, reverse=False):
        wiring = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "HU"
        turnover = "ZM"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_VIII(letter, position=0, reverse=False):
        wiring = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "HU"
        turnover = "ZM"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

class EnigmaNorway:
    @staticmethod
    def rotor_I(letter, position=0, reverse=False):
        wiring = "WTOKASUYVRBXJHQCPZEFMDINLG"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "Y"
        turnover = "Q"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_II(letter, position=0, reverse=False):
        wiring = "GJLPUBSWEMCTQVHXAOFZDRKYNI"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "M"
        turnover = "E"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

    @staticmethod
    def rotor_III(letter, position=0, reverse=False):
        wiring = "JWFMHNBPUSDYTIXVZGRQLAOEKC"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "D"
        turnover = "V"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover
    
    @staticmethod
    def rotor_IV(letter, position=0, reverse=False):
        wiring = "FGZJMVXEPBWSHQTLIUDYKCNRAO"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "R"
        turnover = "V"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover
    
    @staticmethod
    def rotor_V(letter, position=0, reverse=False):
        wiring = "HEJXQOTZBVFDASCILWPGYNMURK"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notch = "H"
        turnover = "Z"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notch, turnover

def advance_rotor(position):
    new_position = (position + 1) % 26
    return new_position
