import pytest
from besancon import Besancon
from besancon.api import BesanconApi


@pytest.fixture
def besancon():
    b = Besancon()
    b.set_luminosity_classes([1, 2]) # Add some data to check
    q = BesanconApi(b)
    return q

@pytest.fixture
def default_besancon():
    b = Besancon()
    q = BesanconApi(b)
    return q

@pytest.fixture
def params():
    b = Besancon()
    b.set_luminosity_classes([1, 2]) # Add some data to check
    q = BesanconApi(b)
    return q.build_params()

@pytest.fixture
def full_custom_params():
    b = (Besancon(email="test@example.com").
            limit_spectral_type("1.0", "9.5").
            set_magnitude_limit("V", 10.0, 100.0).
            add_colour_limit(0, "J-H", 0.3, 1.2).
            set_luminosity_classes([1, 2]))
    return BesanconApi(b).build_given_params()


def test_root_url(besancon):
    assert besancon.URL == 'http://model.obs-besancon.fr/modele_form.php'

def test_default_luminosity_classes(default_besancon):
    assert default_besancon.keyword_defaults['lumi'] == list(range(1, 8))

def test_given_spectype(full_custom_params):
    for (key, value) in zip(['spectyp_min', 'subspectyp_min',
        'spectyp_max', 'subspectyp_max'],
        [1, 0, 9, 5]):
        assert full_custom_params[key] == value

def test_given_lumi(full_custom_params):
    assert full_custom_params['lumi'] == [1, 2]

def test_magnitude_limits(full_custom_params):
    assert full_custom_params['oo'] == [10.] + [-99] * 8 + [0.3, -99, -99, -99]
    assert full_custom_params['ff'] == [100.0] + [99] * 8 + [1.2, 99, 99, 99]
    assert full_custom_params['colind'] == ['J-H', 'U-B', 'V-I', 'V-K']
    
