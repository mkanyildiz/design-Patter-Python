from patterns.strategy.FlyBehavior import FlyBehavior

__author__ = 'Muhammed5'
class FlyRocketPowered(FlyBehavior):
    """
    FlyRocketPowered
    :param FlyBehavior:reference variable of the FlyBehavior class
    """
    def fly(self):
        """

        :return: printing out the result
        """
        print("I'm flying with a rocket!")