__author__ = 'Muhammed5'
import abc
# Abstract factory class
class UIFactory:
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def getToolboxWindow(self): pass

    @abc.abstractmethod
    def getLayersWindow(self): pass

    @abc.abstractmethod
    def getMainWindow(self): pass