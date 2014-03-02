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
            add_colour_limit(0, "J-H", 0.3).
            set_luminosity_classes([1, 2]))
    return BesanconApi(b).build_given_params()


def test_root_url(besancon):
    assert besancon.URL == 'http://model.obs-besancon.fr/modele_form.php'

def test_default_luminosity_classes(default_besancon):
    assert default_besancon.keyword_defaults['lumi'] == list(range(1, 8))

@pytest.mark.xfail
def test_params_construction(params):
    keys = ['lumi', 'spectyp_min']
    values = [[1, 2], 1]
    for (key, value) in zip(keys, values):
        assert params[key] == value

def test_given_spectype(full_custom_params):
    pass

def test_given_lumi(full_custom_params):
    assert full_custom_params['lumi'] == [1, 2]
