class BesanconApi(object):

    URL = 'http://model.obs-besancon.fr/modele_form.php'

    def __init__(self, besancon):
        self.besancon = besancon
        self.payload = 1
