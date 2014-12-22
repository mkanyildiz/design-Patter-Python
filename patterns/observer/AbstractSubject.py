from abc import ABCMeta, abstractmethod
__author__ = 'mwech'
"""
@author: Maximilian Wech
@version: 20141222
@description: Abstrakte Klasse, welche das Observable simuliert und die entsprechenden Methoden bereitstellt.
"""

class AbstractWetterstation:
    __metaclass__ = ABCMeta

    thermometer = []
    temperatur = 0

    def __init__(self):
        """
        Konstruktor
        """
        self.thermometer = []
        self.temperatur = 0

    def registriereThermometer(self, thermometer):
        """
        Methode zum Hinzufügen eines neuen / weiteren Theromometer (Observers)
        :param thermometer, Observer
        """
        self.thermometer.append(thermometer)
        return self

    def set_temperatur(self, new_temperatur):
        """
        Methode zum Setzen einer neuen Temperatur, welche von einem Thermometer angegeben wird.
        Die anderen Observer werden durch dieses Ereignis benachrichtigt (notify).
        :param new_temperatur:
        """
        self.temperatur = new_temperatur
        self.notify()

    def get_temperatur(self):
        """
        Zurückgeben der derzeitig eingestellten Temperatur
        """
        return self.temperatur

    def notify(self):
        """
        Den anderen Thermometern mitteilen, dass eine neue Temperatur gesetzt wurde; die update() Methode ausführen.
        """
        for thermometer in self.thermometer:
            thermometer.update()
