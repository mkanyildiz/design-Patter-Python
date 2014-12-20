from patterns.decorator.Speise import Speise
__author__ = 'mwech'

class Decorator(Speise):
    def __init__(self, speise):
        self.teil = speise

    def getPreis(self):
        return self.teil.getPreis() + \
        Speise.getPreis(self)

    def getBezeichnung(self):
        return self.teil.getBezeichnung() + \
        ' mit ' + Speise.getBezeichnung(self)