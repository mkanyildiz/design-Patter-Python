from abc import ABCMeta, abstractmethod
from patterns.observer.Observer import Thermometer
from patterns.observer.Subject import Wetterstation
__author__ = 'mwech'
"""
@author: Maximilian Wech
@version: 20141222
@description: Main
"""


if __name__ == "__main__":
    wetterstation = Wetterstation()

    thermometer1 = Thermometer(wetterstation)
    thermometer1.set_thermometerID(1)

    thermometer2 = Thermometer(wetterstation)
    thermometer2.set_thermometerID(2)

    thermometer1.set_temperatur("39.0 Grad Celsius - Thermometer1")
    thermometer2.set_temperatur("25.0 Grad Celsius - Thermometer2")
