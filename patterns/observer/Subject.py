from abc import ABCMeta, abstractmethod
from patterns.observer.AbstractSubject import AbstractWetterstation

__author__ = 'mwech'

class Wetterstation(AbstractWetterstation):

    def show_state(self):
        print("Subject: Current State = %s"  (self.state))
