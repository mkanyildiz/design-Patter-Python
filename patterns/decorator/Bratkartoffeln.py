from patterns.decorator.Decorator import Decorator
__author__ = 'mwech'

class Bratkartoffel(Decorator):
    preis = 3.15

    def __init__(self, speise):
        Decorator.__init__(self, speise)