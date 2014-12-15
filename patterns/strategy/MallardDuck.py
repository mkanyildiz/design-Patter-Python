
from strategy.Duck import Duck
from strategy.Fly import Fly
from strategy.Quack import Quack


class MallardDuck(Duck):
    def __init__(self):
        Duck.__init__(self)
        fly_instance = Fly()
        self.set_fly_behavior(fly_instance)
        quack_instance = Quack()
        self.set_quack_behavior(quack_instance)
        print("I'm a real Mallard Duck")