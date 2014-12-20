from patterns.decorator.Decorator import Decorator
__author__ = 'mwech'

class Pommes(Decorator):
    preis = 2.50

    def __init__(self, speise):
        Decorator.__init__(self, speise)