from besancon import Besancon
from besancon.spectraltype import SpectralType
from unittest import TestCase
import pytest


def setup_module(module):
    module.BESANCON = lambda: Besancon(email='test@example.com')


class BesanconTester(TestCase):
    def setUp(self):
        self.b = BESANCON()


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
        self.b.limit_spectral_type("1.0", "9.5")
        assert self.b.spectral_type_limits == [SpectralType("O", 0),
                SpectralType("DA", 5)]

    def test_set_single_lower_value(self):
        self.b.limit_spectral_type("3.2")
        assert self.b.spectral_type_limits == [SpectralType("A", 2),
                SpectralType("DA", 9)]

    def test_set_single_upper_value(self):
        self.b.limit_spectral_type(upper="5.1")
        assert self.b.spectral_type_limits == [SpectralType("O", 0),
                SpectralType("G", 1)]

    def test_correct_way_round(self):
        self.b.limit_spectral_type(lower="5.1", upper="1.2")
        assert self.b.spectral_type_limits == [SpectralType("O", 2),
                SpectralType("G", 1)]


class TestMagnitudeLimits(BesanconTester):
    def test_default_magnitude_limits(self):
        assert self.b.magnitude_limits == {
                'U': [-99.0, 99.0],
                'B': [-99.0, 99.0],
                'V': [10.0, 18.0],
                'R': [-99.0, 99.0],
                'I': [-99.0, 99.0],
                'J': [-99.0, 99.0],
                'H': [-99.0, 99.0],
                'K': [-99.0, 99.0],
                'L': [-99.0, 99.0],
                }


