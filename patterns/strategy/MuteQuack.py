from strategy.QuackBehavior import QuackBehavior

__author__ = 'Muhammed5'
class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")