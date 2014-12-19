import abc

__author__ = 'Muhammed5'

class FlyBehavior():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def fly(self):
        """Method documentation"""
        return