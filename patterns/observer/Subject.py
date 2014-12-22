from abc import ABCMeta, abstractmethod
from patterns.observer.AbstractSubject import AbstractWetterstation
__author__ = 'mwech'
"""
@author: Maximilian Wech
@version: 20141222
@description: Klasse, welche über die derzeitige Temperatur informiert. Ruft abstrakte Klasse auf.
"""

class Wetterstation(AbstractWetterstation):

    def show_temperatur(self):
        """
        Ermittelt derzeitige Temperatur und gibt diese aus.
        """
        print("Wetterstation: Derzeitige Temperatur: = %s"  (self.temperatur))
