class SpectralType(object):

    class_map = {
            "1": "O",
            "2": "B",
            "3": "A",
            "4": "F",
            "5": "G",
            "6": "K",
            "7": "M",
            "8": "C",
            "9": "DA",
            }

    def __init__(self, spectral_class, spectral_subclass):
        self.spectral_class = spectral_class
        self.spectral_subclass = spectral_subclass

    @classmethod
    def from_string(cls, st):
        parts = st.split('.')
        spectral_class = cls.class_map[ parts[0] ]
        spectral_subclass = int(parts[-1])

        return cls(spectral_class, spectral_subclass)

    def __eq__(self, other):
        return (self.spectral_class == other.spectral_class and
                self.spectral_subclass == other.spectral_subclass)


SpectralType.LOWER_LIMIT = SpectralType("O", 0)
SpectralType.UPPER_LIMIT = SpectralType("DA", 9)
