from abc import ABCMeta, abstractmethod
__author__ = 'mwech'
"""
@author: Maximilian Wech
@version: 20141222
@description: Abstrakte Klasse, welche die Funktionen für Observer simuliert.
"""


class AbstractThermometer:
    __metaclass__ = ABCMeta

    wetterstation = 0

    def __init__(self, objekt):
        """
        Konstruktor
        :param objekt:Thermometer
        """
        self.wetterstation = objekt.registriereThermometer(self)

    def set_temperatur(self, new_temperatur):
        """
        Setzen einer neuen Temperatur; Weitergabe an das Observable - die Wetterstation.
        :param new_temperatur: neue Temperatur die ein Thermometer misst.
        """
        self.wetterstation.set_temperatur(new_temperatur)

    def update(self):
        """
        Aufruf der abstrakten Methoden
        """
        self.temperatur_update()

    @abstractmethod
    def temperatur_update(self):
        """
        Abstrakte Methode, wird in der Observer Klasse überschrieben.
        :raise NotImplementedError:
        """
        raise NotImplementedError()
