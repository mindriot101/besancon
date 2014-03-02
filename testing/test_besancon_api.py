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


def test_root_url(besancon):
    assert besancon.URL == 'http://model.obs-besancon.fr/modele_form.php'

def test_default_luminosity_classes(default_besancon):
    assert default_besancon.keyword_defaults['lumi'] == list(range(1, 8))

def test_merged_luminosity_classes(besancon):
    assert besancon['lumi'] == [1, 2]
