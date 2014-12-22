from abc import ABCMeta, abstractmethod
from patterns.observer.AbstractObserver import AbstractThermometer
__author__ = 'mwech'
"""
@author: Maximilian Wech
@version: 20141222
@description: Verwendung der abstrakten Klasse um neue Thermometer zu definieren und neue Temperaturen zu speichern.
"""

class Thermometer(AbstractThermometer):

    old_temperatur = 0.0
    new_temperatur = 0.0
    thermometerID = 0

    def set_thermometerID(self, thermometerID):
        """
        Identifizierung eines Thermometers durch eine Bezeichnung
        :param thermometerID: die Bezeichnung des Thermometers
        """
        self.thermometerID = thermometerID

    def temperatur_update(self):
        """
        Observer überschreibt alte Temperatur mit einer neuen und gibt diese aus.
        """
        self.old_temperatur = self.new_temperatur
        self.new_temperatur = self.wetterstation.get_temperatur()
        print("Thermometer %d: Ursprüngliche Temperatur: '%s' jetzt: '%s'." % (self.thermometerID, self.old_temperatur, self.new_temperatur))

