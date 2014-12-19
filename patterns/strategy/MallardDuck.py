from strategy.Duck import Duck
from strategy.Fly import Fly
from strategy.Quack import Quack


__author__ = 'Muhammed5'
class MallardDuck(Duck):
    def __init__(self):
        Duck.__init__(self)
        fly_instance = Fly()
        self._fly_behavior = fly_instance
        quack_instance = Quack()
        self._quack_behavior = quack_instance
        print("I'm a real Mallard Duck")
