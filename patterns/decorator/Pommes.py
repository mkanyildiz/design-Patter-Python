from patterns.decorator.Decorator import Decorator
__author__ = 'mwech'
"""
@author: Maximilian Wech
@version: 20141222
@description: ConcreteDecorator, Unterklasse von Decorator
"""
class Pommes(Decorator):
    preis = 2.50

    def __init__(self, speise):
        """
        Konstruktor
        :param speise: Konkrete Speise
        """
        self.teil = speise
        Decorator.__init__(self, speise)