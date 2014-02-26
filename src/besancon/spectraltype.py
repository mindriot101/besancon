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

    reverse_map = {
            "O": "1",
            "B": "2",
            "A": "3",
            "F": "4",
            "G": "5",
            "K": "6",
            "M": "7",
            "C": "8",
            "DA": "9",
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

    def __lt__(self, other):
        if self == other:
            return False

        if self.reverse_map[self.spectral_class] < self.reverse_map[other.spectral_class]:
            return True
        elif self.reverse_map[self.spectral_class] > self.reverse_map[other.spectral_class]:
            return False
        else:
            return self.spectral_subclass < other.spectral_subclass

    def __repr__(self):
        return '.'.join(map(str, [self.spectral_class, self.spectral_subclass]))


SpectralType.LOWER_LIMIT = SpectralType("O", 0)
SpectralType.UPPER_LIMIT = SpectralType("DA", 9)
