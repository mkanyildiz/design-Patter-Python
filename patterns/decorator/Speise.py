__author__ = 'mwech'

class Speise:
    def getBezeichnung(self):
        return self.__class__.__name__
    def getPreis(self):
        return self.__class__.preis