from strategy.Duck import Duck
from strategy.FlyNoWay import FlyNoWay
from strategy.SqueakQuack import SqueakQuack

__author__ = 'Muhammed5'
class ModelDuck(Duck):
    def __init__(self):
        Duck.__init__(self)
        fly_no_way_instance = FlyNoWay()
        self._fly_behavior = fly_no_way_instance
        squeak_instance = SqueakQuack()
        self._quack_behavior = squeak_instance
        print("I'm a Model Duck")