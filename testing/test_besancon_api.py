import pytest
from besancon import Besancon
from besancon.api import BesanconApi


@pytest.fixture
def besancon():
    b = Besancon()
    b.set_luminosity_classes([1, 2]) # Add some data to check
    q = BesanconApi(b)
    return q


def test_payload_construction(besancon):
    assert besancon.payload

def test_root_url(besancon):
    assert besancon.URL == 'http://model.obs-besancon.fr/modele_form.php'
