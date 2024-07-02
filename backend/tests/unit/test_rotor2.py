import pytest


from app.enigma.rotor import RotorMachine, EnigmaM1, EnigmaM3, EnigmaNorway


@pytest.fixture
def machine_m1():
    return RotorMachine("Enigma I", ["I", "II", "III", "IV", "V"], "AAA", "AAA")
@pytest.fixture
def machine_m3():
    return RotorMachine("Enigma M3", ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"], "AAA", "AAA")
@pytest.fixture
def machine_norway():
    return RotorMachine("Enigma Norway", ["I", "II", "III", "IV", "V"], "AAA", "AAA")
"""@pytest.fixture
def machine_custom():
    return RotorMachine("Custom Enigma ", ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "N_I", "N_II", "N_III", "N_IV", "N_V"], "AAA", "AAA")
"""


def test_init(machine_m1, machine_m3, machine_norway):
    assert machine_m1.machine_type == "Enigma I"
    assert machine_m1.rotors == ["I", "II", "III", "IV", "V"]
    assert machine_m1.rotor_positions == [0, 0, 0]
    assert machine_m1.ring_positions == [0, 0, 0]
    assert machine_m1.machine == EnigmaM1

    assert machine_m3.machine_type == "Enigma M3"
    assert machine_m3.rotors == ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
    assert machine_m3.rotor_positions == [0, 0, 0]
    assert machine_m3.ring_positions == [0, 0, 0]
    assert machine_m3.machine == EnigmaM3

    assert machine_norway.machine_type == "Enigma Norway"
    assert machine_norway.rotors == ["I", "II", "III", "IV", "V"]
    assert machine_norway.rotor_positions == [0, 0, 0]
    assert machine_norway.ring_positions == [0, 0, 0]
    assert machine_norway.machine == EnigmaNorway


def test_get_machine_class(machine_m1, machine_m3, machine_norway):
    assert machine_m1.get_machine_class() == EnigmaM1
    assert machine_m3.get_machine_class() == EnigmaM3
    assert machine_norway.get_machine_class() == EnigmaNorway

    with pytest.raises(ValueError):
        RotorMachine("Unknown", ["I", "II", "III"], "AAA", "AAA")





