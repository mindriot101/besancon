from besancon import Besancon
from besancon.spectraltype import SpectralType
from unittest import TestCase
import pytest

def test_set_email():
    b = Besancon(email="test@example.com")
    assert b.email == "test@example.com"

class TestSetters(TestCase):
    def setUp(self):
        self.b = Besancon(email='test@example.com')

    def test_query_without_email_fails(self):
        with pytest.raises(RuntimeError) as err:
            self.b.query(lat=20.3, long=51.2, area=64.0)

        assert "no email set" in str(err).lower()

    def test_spectral_type_limit(self):
        self.b = Besancon()
        self.b.limit_spectral_type("1.0", "9.5")
        assert self.b.spectral_type_limits == [SpectralType("O", 0),
                SpectralType("DA", 5)]
