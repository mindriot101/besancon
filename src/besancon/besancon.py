from .spectraltype import SpectralType
from .colour import Colour


class Besancon(object):
    def __init__(self, email=None):
        self.email = email
        self.spectral_type_limits = [SpectralType.LOWER_LIMIT,
                SpectralType.UPPER_LIMIT]
        self.magnitude_limits = self.setup_magnitude_limits()
        self.colour_limits = self.setup_colour_limits()
        self.luminosity_classes = self.setup_luminosity_classes()

    def limit_spectral_type(self, lower=None, upper=None):
        lower_spectral_type = (SpectralType.from_string(lower) if lower
                else SpectralType.LOWER_LIMIT)
        upper_spectral_type = (SpectralType.from_string(upper) if upper
                else SpectralType.UPPER_LIMIT)

        if upper_spectral_type < lower_spectral_type:
            lower_spectral_type, upper_spectral_type = upper_spectral_type, lower_spectral_type

        self.spectral_type_limits = [lower_spectral_type,
                upper_spectral_type]

    def set_magnitude_limit(self, passband, bright=None, faint=None):
        bright_limit = bright if bright else self.magnitude_limits[passband][0]
        faint_limit = faint if faint else self.magnitude_limits[passband][1]

        if bright_limit > faint_limit:
            faint_limit, bright_limit = bright_limit, faint_limit

        self.magnitude_limits[passband] = [bright_limit, faint_limit]

    def add_colour_limit(self, index, colour, lower=None, upper=None):
        if lower is None and upper is None:
            return self

        if not 0 <= index <= 3:
            raise RuntimeError("Invalid index {0}, must be 0-3".format(index))

        colour = colour.upper()

        if not Colour.valid_colour(colour):
            msg = "Invalid colour: {0} (magnitues must be UBVRIJHKL)".format(colour)
            raise RuntimeError(msg)


        old_colour_limits = self.colour_limits[index][-2:]
        lower_value = lower if lower is not None else old_colour_limits[0]
        upper_value = upper if upper is not None else old_colour_limits[1]

        self.colour_limits[index] = (colour, lower_value, upper_value)

    def set_luminosity_clases(self, classes):
        if min(classes) <= 0 or max(classes) > 7:
            raise RuntimeError("Invalid classes passed, must be in range 1-7")

        self.luminosity_classes = classes

    def query(self, *args, **kwargs):
        raise RuntimeError("no email set")

    @staticmethod
    def setup_colour_limits():
        return [
                ('B-V', -99.0, 99.0),
                ('U-B', -99.0, 99.0),
                ('V-I', -99.0, 99.0),
                ('V-K', -99.0, 99.0),
                ]

    @staticmethod
    def setup_luminosity_classes():
        return [1, 2, 3, 4, 5, 6, 7]



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
