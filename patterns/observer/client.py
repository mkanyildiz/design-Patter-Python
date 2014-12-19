from abc import ABCMeta, abstractmethod
from patterns.observer.Observer import Thermometer
from patterns.observer.Subject import Wetterstation

__author__ = 'mwech'

if __name__ == "__main__":
    wetterstation = Wetterstation()

    temp1 = Thermometer(wetterstation)
    temp1.set_thermometerID(1)

    temp2 = Thermometer(wetterstation)
    temp2.set_thermometerID(2)

    temp1.set_state("1 set by Observer 1")
    temp2.set_state("2 set by Observer 2")
