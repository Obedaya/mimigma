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

        # Ring settings positions (e.g., "000" -> [0, 0, 0])
        self.ring_positions = [ord(pos) - ord('A') for pos in ring_positions]

        # Determine the appropriate Enigma machine class
        self.machine = self.get_machine_class()

        # Initialize notches and turnovers for each rotor
        self.turnovers = []
        for rotor in self.rotors:
            rotor_method = self.get_rotor_method(rotor)
            _, _, turnovers = rotor_method('A')
            # Convert notches to list of positions
            self.turnovers.append([ord(n) - ord('A') for n in turnovers])

    def get_machine_class(self):
        if self.machine_type == "Enigma I":
            return EnigmaM1
        elif self.machine_type == "Enigma M3":
            return EnigmaM3
        elif self.machine_type == "Enigma Norway":
            return EnigmaNorway
        elif self.machine_type == "Custom Enigma":
            return CustomEnigma
        else:
            raise ValueError("Unknown machine type")

    def get_rotor_method(self, rotor):
        return getattr(self.machine, f"rotor_{rotor}")

    def advance_rotors(self):
        # Determine which rotors need to be stepped
        advance_next = [False] * len(self.rotors)
        advance_next[-1] = True  # The rightmost rotor always advances

        for i in reversed(range(len(self.rotors) - 1)):
            if self.rotor_positions[i + 1] in self.turnovers[i + 1]:
                advance_next[i] = True

        # Perform the rotor advancement
        for i in reversed(range(len(self.rotors))):
            if advance_next[i]:
                self.rotor_positions[i] = (self.rotor_positions[i] + 1) % 26

    def encrypt_letter(self, letter):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = alphabet.index(letter)

        # Iterate through rotors in reverse order
        for i in reversed(range(len(self.rotors))):
            shift = (self.rotor_positions[i] + self.ring_positions[i]) % 26
            rotor_method = self.get_rotor_method(self.rotors[i])
            index = (index + shift) % 26
            print(f"Letter before rotor {self.rotors[i]}: {alphabet[index]}")
            letter, _, _ = rotor_method(alphabet[index])
            index = (alphabet.index(letter) - shift) % 26
            print(f"Letter after rotor {self.rotors[i]}: {letter}")

        return alphabet[index]

    def encrypt_letter_reverse(self, letter):
        # This method should process the letter back through the rotors in the opposite direction
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = alphabet.index(letter)

        # Iterate through rotors in forward order
        for i in range(len(self.rotors)):
            shift = (self.rotor_positions[i] + self.ring_positions[i]) % 26
            rotor_method = self.get_rotor_method(self.rotors[i])
            index = (index + shift) % 26
            print(f"Letter before rotor {self.rotors[i]}: {alphabet[index]}")
            letter, _, _ = rotor_method(alphabet[index], reverse=True)
            index = (alphabet.index(letter) - shift) % 26
            print(f"Letter after rotor {self.rotors[i]}: {letter}")

        return alphabet[index]


class EnigmaM1:
    @staticmethod
    def rotor_I(letter, position=0, reverse=False):
        wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "Y"
        turnover = "Q"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_II(letter, position=0, reverse=False):
        wiring = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "M"
        turnover = "E"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_III(letter, position=0, reverse=False):
        wiring = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "D"
        turnover = "V"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_IV(letter, position=0, reverse=False):
        wiring = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "R"
        turnover = "J"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_V(letter, position=0, reverse=False):
        wiring = "VZBRGITYUPSDNHLXAWMJQOFECK"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "H"
        turnover = "Z"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover


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
        notches = "HU"
        turnover = "ZM"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_VII(letter, position=0, reverse=False):
        wiring = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "HU"
        turnover = "ZM"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_VIII(letter, position=0, reverse=False):
        wiring = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "HU"
        turnover = "ZM"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover


class EnigmaNorway:
    @staticmethod
    def rotor_I(letter, position=0, reverse=False):
        wiring = "WTOKASUYVRBXJHQCPZEFMDINLG"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "Y"
        turnover = "Q"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_II(letter, position=0, reverse=False):
        wiring = "GJLPUBSWEMCTQVHXAOFZDRKYNI"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "M"
        turnover = "E"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_III(letter, position=0, reverse=False):
        wiring = "JWFMHNBPUSDYTIXVZGRQLAOEKC"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "D"
        turnover = "V"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_IV(letter, position=0, reverse=False):
        wiring = "FGZJMVXEPBWSHQTLIUDYKCNRAO"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "R"
        turnover = "V"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_V(letter, position=0, reverse=False):
        wiring = "HEJXQOTZBVFDASCILWPGYNMURK"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "H"
        turnover = "Z"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover


class CustomEnigma:
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
        notches = "HU"
        turnover = "ZM"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_VII(letter, position=0, reverse=False):
        wiring = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "HU"
        turnover = "ZM"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_VIII(letter, position=0, reverse=False):
        wiring = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "HU"
        turnover = "ZM"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_N_I(letter, position=0, reverse=False):
        wiring = "WTOKASUYVRBXJHQCPZEFMDINLG"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "Y"
        turnover = "Q"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_N_II(letter, position=0, reverse=False):
        wiring = "GJLPUBSWEMCTQVHXAOFZDRKYNI"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "M"
        turnover = "E"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_N_III(letter, position=0, reverse=False):
        wiring = "JWFMHNBPUSDYTIXVZGRQLAOEKC"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "D"
        turnover = "V"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_N_IV(letter, position=0, reverse=False):
        wiring = "FGZJMVXEPBWSHQTLIUDYKCNRAO"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "R"
        turnover = "V"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

    @staticmethod
    def rotor_N_V(letter, position=0, reverse=False):
        wiring = "HEJXQOTZBVFDASCILWPGYNMURK"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        notches = "H"
        turnover = "Z"
        if reverse:
            index = (wiring.index(letter) - position) % 26
            encrypted_letter = alphabet[index]
        else:
            index = (alphabet.index(letter) + position) % 26
            encrypted_letter = wiring[index]
        return encrypted_letter, notches, turnover

def advance_rotor(position):
    new_position = (position + 1) % 26
    return new_position
