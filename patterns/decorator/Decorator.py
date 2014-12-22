from patterns.decorator.Speise import Speise
__author__ = 'mwech'

class Decorator(Speise):
    def __init__(self, speise):
        """
        Konstruktor
        :param speise: Konkrete Speise
        """
        self.teil = speise

    def getPreis(self):
        """
        Zurückliefern des Preises einer Speise
        :return:
        """
        return self.teil.getPreis() + \
        Speise.getPreis(self)

    def getBezeichnung(self):
        """
        Zurückliefern der Bezeichnung einer Speise
        :return:
        """
        return self.teil.getBezeichnung() + \
        ' mit ' + Speise.getBezeichnung(self)