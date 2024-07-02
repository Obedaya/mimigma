import pytest
from app.enigma.plugboard import Plugboard

@pytest.fixture
def input_plugs():
    return [("A", "B"), ("C", "D"), ("E", "F")]

def test_initialize_plugboard(input_plugs):
    plugboard = Plugboard(input_plugs)
    assert plugboard.plugs == input_plugs
def test_plugboard_valid_input(input_plugs):
    plugboard = Plugboard(input_plugs)
    assert plugboard.encrypt("A") == "B"

def test_plugboard_invalid_input(input_plugs):
    plugboard = Plugboard(input_plugs)
    assert plugboard.encrypt("K") == "K"

