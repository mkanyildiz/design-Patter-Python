from abc import ABCMeta, abstractmethod
__author__ = 'mwech'

class AbstractWetterstation:
    __metaclass__ = ABCMeta

    thermometer = []
    temperatur = 0

    def __init__(self):
        self.thermometer = []
        self.temperatur = 0

    def registriereThermometer(self, thermometer):
        self.thermometer.append(thermometer)
        return self

    def set_temperatur(self, new_temperatur):
        self.temperatur = new_temperatur
        self.notify()

    def get_temperatur(self):
        return self.temperatur

    def notify(self):
        for thermometer in self.thermometer:
            thermometer.update()
