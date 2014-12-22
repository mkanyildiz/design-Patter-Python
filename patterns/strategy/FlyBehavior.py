import abc

__author__ = 'Muhammed5'

class FlyBehavior():
    """
    FlyBehavior
    :param:nothing
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def fly(self):
        """

        :return: is empty
        """
        return