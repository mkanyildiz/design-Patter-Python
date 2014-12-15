from strategy.DecoyDuck import DecoyDuck
from strategy.FlyRocketPower import FlyRocketPowered
from strategy.MallardDuck import MallardDuck
from strategy.ModelDuck import ModelDuck

__author__ = 'Muhammed5'

if __name__ == "__main__":

    print('#'*80)
    print("Mallard Duck")
    print('#'*80)
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    print('#'*80)
    print("Model Duck")
    print('#'*80)
    model = ModelDuck()
    model.perform_fly()
    fly_rocket_powered_instance = FlyRocketPowered()
    model.set_fly_behavior(fly_rocket_powered_instance)
    model.perform_fly()

    print('#'*80)
    print("Decoy Duck")
    print('#'*80)
    decoy = DecoyDuck()
    decoy.perform_fly()
    decoy.perform_quack()