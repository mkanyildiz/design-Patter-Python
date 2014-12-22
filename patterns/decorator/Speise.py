__author__ = 'mwech'
"""
@author: Maximilian Wech
@version: 20141222
@description: Component
"""
class Speise:
    def getBezeichnung(self):
        """
        Zurückgeben der Bezeichnung einer Speise
        :return: Klassenname
        """
        return self.__class__.__name__

    def getPreis(self):
        """
        Zurückgeben des Preises einer Speise
        :return: Preis
        """
        return self.__class__.preis