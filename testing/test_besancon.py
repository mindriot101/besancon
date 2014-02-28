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

    def test_default_spectral_type_limits(self):
        assert self.b.spectral_type_limits == [SpectralType("O", 0),
                SpectralType("DA", 9)]


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

    def test_set_magnitude_limit(self):
        self.b.set_magnitude_limit("V", 5.0, 7.0)
        assert self.b.magnitude_limits['V'] == [5.0, 7.0]

    def test_add_single_limit(self):
        self.b.set_magnitude_limit("B", bright=10.0)
        assert self.b.magnitude_limits['B'] == [10.0, 99.0]

    def test_add_wrong_way_round(self):
        self.b.set_magnitude_limit("U", 12.0, 3.0)
        assert self.b.magnitude_limits['U'] == [3.0, 12.0]

    def test_do_nothing(self):
        self.b.set_magnitude_limit("J")
        assert self.b.magnitude_limits['J'] == [-99.0, 99.0]

class TestColourLimits(BesanconTester):
    def test_default_limits(self):
        assert self.b.colour_limits == [
                ('B-V', -99.0, 99.0),
                ('U-B', -99.0, 99.0),
                ('V-I', -99.0, 99.0),
                ('V-K', -99.0, 99.0),
                ]

    def test_set_limit(self):
        self.b.add_colour_limit(0, 'J-H', 0.0, 1.2)
        assert self.b.colour_limits == [
                ('J-H', 0.0, 1.2),
                ('U-B', -99.0, 99.0),
                ('V-I', -99.0, 99.0),
                ('V-K', -99.0, 99.0),
                ]

    def test_only_one(self):
        self.b.add_colour_limit(0, 'J-H', lower=0.0)
        assert self.b.colour_limits == [
                ('J-H', 0.0, 99.0),
                ('U-B', -99.0, 99.0),
                ('V-I', -99.0, 99.0),
                ('V-K', -99.0, 99.0),
                ]

    def test_neither(self):
        before = self.b.colour_limits
        self.b.add_colour_limit(0, 'J-H')
        assert self.b.colour_limits == before

    def test_invalid_index(self):
        with pytest.raises(RuntimeError) as err:
            self.b.add_colour_limit(-1, 'J-H', 0.1, 0.5)

        assert "invalid index -1, must be 0-3" in str(err).lower()

        with pytest.raises(RuntimeError) as err:
            self.b.add_colour_limit(5, 'J-H', 0.1, 0.5)

        assert "invalid index 5, must be 0-3" in str(err).lower()

    def test_invalid_colour(self):
        with pytest.raises(RuntimeError) as err:
            self.b.add_colour_limit(0, "A-Q", 0.1, 0.5)

        assert "invalid colour: a-q" in str(err).lower()

class TestLuminosityClasses(BesanconTester):
    def test_default_classes(self):
        assert self.b.luminosity_classes == [1, 2, 3, 4, 5, 6, 7]

    def test_change_classes(self):
        self.b.set_luminosity_classes([1, 2, 3, 4, 5])
        assert self.b.luminosity_classes == [1, 2, 3, 4, 5]

    def test_error_with_invalid_classes(self):
        with pytest.raises(RuntimeError) as err:
            self.b.set_luminosity_classes([0, 1, 20])

        assert "invalid classes passed" in str(err).lower()


class TestQuery(BesanconTester):
    pass
