__author__ = 'Muhammed5'
import abc
class QuackBehavior():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def quack(self):
        """Method documentation"""
        return