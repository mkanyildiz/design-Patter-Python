from abc import ABCMeta, abstractmethod
__author__ = 'mwech'

class AbstractWetterstation:
    __metaclass__ = ABCMeta

    observers = []
    state = 0

    def __init__(self):
        self.observers = []
        self.state = 0

    def register(self, observer):
        self.observers.append(observer)
        return self

    def set_state(self, new_state):
        self.state = new_state
        self.notify()

    def get_state(self):
        return self.state

    def notify(self):
        for observer in self.observers:
            observer.update()
