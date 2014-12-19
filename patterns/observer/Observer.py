from abc import ABCMeta, abstractmethod
from patterns.observer.AbstractObserver import AbstractThermometer

__author__ = 'mwech'

class Thermometer(AbstractThermometer):

    old_state = 0
    new_state = 0
    thermometerID = 0

    def set_thermometerID(self, thermometerID):
        self.thermometerID = thermometerID

    def handle_state_change(self):
        self.old_state = self.new_state
        self.new_state = self.subject.get_state()
        print("Observer #%d: State Changed in Subject from '%s' to '%s'." % (self.thermometerID, self.old_state, self.new_state))

