from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..crud import get_rotor_settings
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
        
        # Ring settings positions (e.g., "000" -> [0, 0, 0])
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

        # Print initial positions for verification
        print(f"Initial rotor positions: {self.rotor_positions}")
        print(f"Initial ring positions: {self.ring_positions}")

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

                """# Implement double-stepping logic for Enigma M3 and similar machines
                if i == 2 and self.machine_type == "M3" and advance_next:
                    self.rotor_positions[1] = (self.rotor_positions[1] + 1) % 26
                elif i == 1 and self.machine_type == "M3" and self.rotor_positions[1] == (self.notches[1] - 1):
                    self.rotor_positions[2] = (self.rotor_positions[2] + 1) % 26"""
            else:
                break
    """def advance_rotors(self):
        advance_next = True

        for i in reversed(range(len(self.rotors))):
            if advance_next:
                self.rotor_positions[i] = (self.rotor_positions[i] + 1) % 26
                advance_next = self.rotor_positions[i] == self.notches[i]
                # Implement double-stepping logic for Enigma M3 and similar machines
                if i == 2 and self.machine_type == "M3" and advance_next:
                    self.rotor_positions[1] = (self.rotor_positions[1] + 1) % 26
                elif i == 1 and self.machine_type == "M3" and self.rotor_positions[1] == (self.notches[1] - 1):
                    self.rotor_positions[2] = (self.rotor_positions[2] + 1) % 26

                # Print current rotor positions for verification
                print(f"Rotor {self.rotors[i]} position: {self.rotor_positions[i]}")

            else:
                break"""

    def encrypt_letter(self, letter):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, rotor in enumerate(self.rotors):
            rotor_position = self.rotor_positions[i]
            ring_position = self.ring_positions[i]

            # Calculate shift based on rotor and ring positions
            shift = (rotor_position + ring_position) % 26

            # Get rotor encryption method
            rotor_method = self.get_rotor_method(rotor)

            # Calculate encrypted index
            encrypted_index = (alphabet.index(letter) + shift) % 26

            # Encrypt the letter using the rotor method
            letter, _, _ = rotor_method(alphabet[encrypted_index])

            # Adjust the result considering the ring position
            letter = alphabet[(alphabet.index(letter) - ring_position) % 26]

            # Print encrypted letter for current rotor
            print(f"Encrypted letter after rotor {self.rotors[i]}: {letter}")

        return letter


    def encrypt_letter_reverse(self, letter):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i in reversed(range(len(self.rotors))):
            rotor_position = self.rotor_positions[i]
            ring_position = self.ring_positions[i]

            # Calculate the shift taking into account rotor and ring positions
            shifted_position = (self.rotor_positions[i] - self.ring_positions[i]) % 26

            # Get rotor encryption method
            rotor_method = self.get_rotor_method(self.rotors[i])

            # Encrypt the letter using the rotor method in reverse
            letter, _, _ = rotor_method(letter, shifted_position, reverse=True)

            # Adjust the result considering the ring position
            letter = alphabet[(alphabet.index(letter) + ring_position) % 26]

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
