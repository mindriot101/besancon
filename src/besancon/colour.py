import re

class Colour(object):

    colour_regex = re.compile(r'[UBVRIJHKL]-[UBVRIJHKL]')

    @classmethod
    def valid_colour(cls, colour):
        return cls.colour_regex.match(colour)
