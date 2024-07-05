import pytest
from app.enigma.reflector import Reflector

@pytest.mark.parametrize("variant", ["UKW_A", "UKW_B", "UKW_C", "UKW_N"])

#testet ob die Klasse mit der richtigen Variante initialisiert wird
def test_valid_variant(variant):
    reflector = Reflector(variant)
    assert reflector.variant_mapping is not None  # Ensure the mapping is set

@pytest.mark.parametrize("variant", ["UKW_Z", "UKW_G", "UKW_F"])
#test of exception
def test_invalid_variant(variant):
    with pytest.raises(Exception, match="Invalid input"):
        Reflector(variant)
@pytest.fixture
def reflector():
    return Reflector("UKW_A")

#test of encrypt methode
@pytest.mark.parametrize("letter, encrypted_letter", [("A", "E"), ("B", "J"), ("C", "M")])
def test_encrypt_valid_input(reflector, letter, encrypted_letter):
    assert reflector.encrypt(letter) == encrypted_letter