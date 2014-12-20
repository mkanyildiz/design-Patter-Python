from patterns.decorator.Decorator import Decorator
__author__ = 'mwech'

class Salat(Decorator):
    preis = 4.25

    def __init__(self, speise):
        Decorator.__init__(self, speise)