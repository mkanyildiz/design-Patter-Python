from strategy.FlyNoWay import FlyNoWay
from strategy.MuteQuack import MuteQuack

from strategy.Duck import Duck

class DecoyDuck(Duck):
    """
    DecoyDuck
    :param Duck: Reference of the class Duck
    """
    def __init__(self):
        """

        :return: nothing
        """
        Duck.__init__(self)
        fly_no_way_instance = FlyNoWay()
        self._fly_behavior = fly_no_way_instance
        mute_instance = MuteQuack()
        self._quack_behavior = mute_instance
        print("I'm a Decoy Duck")