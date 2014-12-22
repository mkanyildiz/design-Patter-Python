__author__ = 'Muhammed5'
import abc
class QuackBehavior():
    """
    QuackBehavior
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def quack(self):
        """
        :return: empty
        """
        return