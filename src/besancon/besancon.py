from .spectraltype import SpectralType

class Besancon(object):
    def __init__(self, email=None):
        self.email = email
        self.spectral_type_limits = [SpectralType.LOWER_LIMIT,
                SpectralType.UPPER_LIMIT]
    
    def limit_spectral_type(self, lower=None, upper=None):
        lower_spectral_type = SpectralType.from_string(lower) if lower else None
        upper_spectral_type = SpectralType.from_string(upper) if upper else None


        self.spectral_type_limits = [lower_spectral_type,
                upper_spectral_type]

    def query(self, *args, **kwargs):
        raise RuntimeError("no email set")
