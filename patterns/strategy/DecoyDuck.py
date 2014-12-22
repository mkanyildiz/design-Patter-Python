from patterns.strategy.Duck import Duck
from patterns.strategy.FlyNoWay import FlyNoWay
from patterns.strategy.MuteQuack import MuteQuack


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