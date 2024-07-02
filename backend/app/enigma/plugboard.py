class Plugboard:
    # Extract Plugboard setting from db and save it as a variable

    def __init__(self, plugs):
        self.plugs = plugs

    def encrypt(self, input):
        for plug in self.plugs:
            if input in plug:
                return plug[1] if input == plug[0] else plug[0]
        return input

# Example usage:
# p = Plugboard([["A", "B"], ["C", "D"]])
# encrypted_letter = p.encrypt("D")  # "C"
# print(encrypted_letter)