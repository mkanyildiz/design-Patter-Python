from abc import ABCMeta, abstractmethod
__author__ = 'mwech'

class AbstractThermometer:
    __metaclass__ = ABCMeta

    subject = 0

    def __init__(self, obj):
        self.subject = obj.register(self)

    def set_state(self, new_state):
        self.subject.set_state(new_state)

    def update(self):
        self.handle_state_change()

    @abstractmethod
    def handle_state_change(self):
        raise NotImplementedError()
