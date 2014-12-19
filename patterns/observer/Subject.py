from abc import ABCMeta, abstractmethod
from patterns.observer.AbstractSubject import AbstractWetterstation

__author__ = 'mwech'

class Wetterstation(AbstractWetterstation):

    def show_temperatur(self):
        print("Wetterstation: Derzeitige Temperatur: = %s"  (self.temperatur))
