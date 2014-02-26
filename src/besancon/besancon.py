from .spectraltype import SpectralType


class Besancon(object):
    def __init__(self, email=None):
        self.email = email
        self.spectral_type_limits = [SpectralType.LOWER_LIMIT,
                SpectralType.UPPER_LIMIT]
        self.magnitude_limits = self.setup_magnitude_limits()

    def limit_spectral_type(self, lower=None, upper=None):
        lower_spectral_type = (SpectralType.from_string(lower) if lower
                else SpectralType.LOWER_LIMIT)
        upper_spectral_type = (SpectralType.from_string(upper) if upper
                else SpectralType.UPPER_LIMIT)

        if upper_spectral_type < lower_spectral_type:
            lower_spectral_type, upper_spectral_type = upper_spectral_type, lower_spectral_type

        self.spectral_type_limits = [lower_spectral_type,
                upper_spectral_type]

    def query(self, *args, **kwargs):
        raise RuntimeError("no email set")

    @staticmethod
    def setup_magnitude_limits():
        return {
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
