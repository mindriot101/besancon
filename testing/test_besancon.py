from besancon import Besancon
from besancon.spectraltype import SpectralType
from unittest import TestCase
import pytest

def setup_module(module):
    module.BESANCON = Besancon(email='test@example.com')

class BesanconTester(TestCase):
    def setUp(self):
        self.b = BESANCON


class TestEmail(BesanconTester):
    def test_query_without_email_fails(self):
        b = Besancon()
        with pytest.raises(RuntimeError) as err:
            b.query(lat=20.3, long=51.2, area=64.0)

        assert "no email set" in str(err).lower()


    def test_set_email(self):
        assert self.b.email == "test@example.com"


class TestSpectralType(BesanconTester):
    def test_spectral_type_limit(self):
        self.b = Besancon()
        self.b.limit_spectral_type("1.0", "9.5")
        assert self.b.spectral_type_limits == [SpectralType("O", 0),
                SpectralType("DA", 5)]
