from besancon.colour import Colour


def test_valid_colour():
    assert Colour.valid_colour("J-H")

def test_invalid_colour():
    assert not Colour.valid_colour("A-Q")
