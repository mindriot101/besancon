from besancon.spectraltype import SpectralType

def test_o_from_string():
    s = SpectralType.from_string("1.0")
    assert s.spectral_class == "O" and s.spectral_subclass == 0

def test_f_from_string():
    s = SpectralType.from_string("4.8")
    assert s.spectral_class == "F" and s.spectral_subclass == 8
