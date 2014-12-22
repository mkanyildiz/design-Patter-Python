__author__ = 'Muhammed5'
import abc
# Abstract factory class
class UIFactory:
    """
    UIFactory
    """
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def getToolboxWindow(self):
        """
        :return: nothing
        """
        pass

    def getLayersWindow(self):
        """
        :return: nothing
        """
        pass

    def getMainWindow(self):
        """
        :return: nothing
        """
        pass