from abc import ABCMeta, abstractmethod
__author__ = 'mwech'

class AbstractThermometer:
    __metaclass__ = ABCMeta

    wetterstation = 0

    def __init__(self, objekt):
        self.wetterstation = objekt.registriereThermometer(self)

    def set_temperatur(self, new_temperatur):
        self.wetterstation.set_temperatur(new_temperatur)

    def update(self):
        self.handle_temperatur_update()

    @abstractmethod
    def handle_temperatur_update(self):
        raise NotImplementedError()
