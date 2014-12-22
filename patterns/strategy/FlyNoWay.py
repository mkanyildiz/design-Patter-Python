from patterns.strategy.FlyBehavior import FlyBehavior

__author__ = 'Muhammed5'
class FlyNoWay(FlyBehavior):
    """
    FlyNoWay
    :param FlyBehavior: reference of the class FlyBehavior
    """
    def fly(self):
        """

        :return: jsut printing our the result
        """
        print("I can't fly")