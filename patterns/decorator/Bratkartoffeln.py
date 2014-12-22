from patterns.decorator.Decorator import Decorator
__author__ = 'mwech'
"""
@author: Maximilian Wech
@version: 20141222
@description: ConcreteDecorator, Unterklasse von Decorator
"""
class Bratkartoffel(Decorator):
    preis = 3.15

    def __init__(self, speise):
        """
        Konstruktor
        :param speise: Konkrete Speise
        """
        Decorator.__init__(self, speise)