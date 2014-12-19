from abc import ABCMeta, abstractmethod
from patterns.observer.AbstractObserver import AbstractThermometer

__author__ = 'mwech'

class Thermometer(AbstractThermometer):

    old_temperatur = 0.0
    new_temperatur = 0.0
    thermometerID = 0

    def set_thermometerID(self, thermometerID):
        self.thermometerID = thermometerID

    def handle_temperatur_update(self):
        self.old_temperatur = self.new_temperatur
        self.new_temperatur = self.wetterstation.get_temperatur()
        print("Thermometer %d: Ursprüngliche Temperatur: '%s' jetzt: '%s'." % (self.thermometerID, self.old_temperatur, self.new_temperatur))

