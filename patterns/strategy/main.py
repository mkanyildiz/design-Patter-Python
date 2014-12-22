# coding=utf-8
from patterns.strategy.DecoyDuck import DecoyDuck
from patterns.strategy.MallardDuck import MallardDuck
from patterns.strategy.ModelDuck import ModelDuck


class main():
    """
    main class
    """
    def __init__(self):
        """

        :return: nothing
        """
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
            model.perform_quack()

            print('#'*80)
            print("Decoy Duck")
            print('#'*80)
            decoy = DecoyDuck()
            decoy.perform_fly()
            decoy.perform_quack()

main()