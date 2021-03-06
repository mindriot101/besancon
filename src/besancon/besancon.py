from .spectraltype import SpectralType
from .api import BesanconApi
from .colour import Colour
import requests

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
        return self

    def set_magnitude_limit(self, passband, bright=None, faint=None):
        bright_limit = bright if bright else self.magnitude_limits[passband][0]
        faint_limit = faint if faint else self.magnitude_limits[passband][1]

        if bright_limit > faint_limit:
            faint_limit, bright_limit = bright_limit, faint_limit

        self.magnitude_limits[passband] = [bright_limit, faint_limit]
        return self

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
        return self

    def set_luminosity_classes(self, classes):
        if min(classes) <= 0 or max(classes) > 7:
            raise RuntimeError("Invalid classes passed, must be in range 1-7")

        self.luminosity_classes = classes
        return self

    def build_api_spectral_type_limits(self):
        lower, upper = self.spectral_type_limits
        return {
                'spectyp_min': lower.api_spectype,
                'subspectyp_min': lower.api_subspectype,
                'spectyp_max': upper.api_spectype,
                'subspectyp_max': upper.api_subspectype,
                }

    def build_magnitude_limits(self):
        original_limits = self.magnitude_limits
        order = ['V', 'U', 'B', 'R', 'I', 'J', 'K', 'H', 'L']

        oo_keys = [original_limits[key][0] for key in order]
        ff_keys = [original_limits[key][1] for key in order]

        oo_keys.extend([row[1] for row in self.colour_limits])
        ff_keys.extend([row[2] for row in self.colour_limits])

        return {
                'oo': oo_keys,
                'ff': ff_keys,
                }

    def update_colours(self):
        return {'colind': [row[0] for row in self.colour_limits]}

    def query(self, lat, long, area):
        if not self.email:
            raise RuntimeError("No email set")

        params = BesanconApi(self).build_given_params()
        params.update({
            'latit': lat,
            'longit': long,
            'soli': area,
            'email': self.email,
            })

        # Flatten the arrays (from astroquery)
        for _ in xrange(2):  # deal with nested lists
            for k,v in params.items():
                if isinstance(v,list) or (isinstance(v,tuple) and len(v) > 1):
                    if k in params:
                        del params[k]
                    for ii,x in enumerate(v):
                        params['%s[%i]' % (k,ii)] = x

        return requests.post(BesanconApi.URL, data=params)

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
