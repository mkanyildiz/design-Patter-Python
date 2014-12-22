__author__ = 'Muhammed5'
import abc
class Duck(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def set_fly_behavior(self, fb):
        """

        :param fb: flybehavior
        :return: nothing
        """
        self._fly_behavior = fb

    @abc.abstractmethod
    def set_quack_behavior(self, qb):
        """

        :param qb:quackbehavior
        :return:
        """
        self._quack_behavior = qb

    @abc.abstractmethod
    def perform_fly(self):
        """

        :return: nothing
        """
        self._fly_behavior.fly()

    @abc.abstractmethod
    def perform_quack(self):
        """

        :return: nothing
        """
        self._quack_behavior.quack()