from patterns.strategy.QuackBehavior import QuackBehavior

__author__ = 'Muhammed5'
class MuteQuack(QuackBehavior):
    """
    MuteQuack
    :param QuackBehavior: reference of a class
    """
    def quack(self):
        """

        :return: just printing out the result
        """
        print("<< Silence >>")