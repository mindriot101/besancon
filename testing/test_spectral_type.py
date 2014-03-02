from besancon.spectraltype import SpectralType

def test_o_from_string():
    s = SpectralType.from_string("1.0")
    assert s.spectral_class == "O" and s.spectral_subclass == 0

def test_f_from_string():
    s = SpectralType.from_string("4.8")
    assert s.spectral_class == "F" and s.spectral_subclass == 8

def test_lower_limit():
    assert SpectralType.LOWER_LIMIT == SpectralType("O", 0)

def test_upper_limit():
    assert SpectralType.UPPER_LIMIT == SpectralType("DA", 9)

def test_return_spectype():
    assert SpectralType.from_string("1.0").api_spectype == 1
    assert SpectralType.from_string("5.0").api_spectype == 5

def test_return_subspectype():
    assert SpectralType.from_string("1.2").api_subspectype == 2
    assert SpectralType.from_string("5.5").api_subspectype == 5
