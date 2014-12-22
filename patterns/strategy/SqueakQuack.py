from patterns.strategy.QuackBehavior import QuackBehavior

__author__ = 'Muhammed5'
class SqueakQuack(QuackBehavior):
    """
    SqueekQuack
    :param QuackBehavior: referecne of the class QuackBehavior
    """
    def quack(self):
        """

        :return: printing some data
        """
        print("Squeak")