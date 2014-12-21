from factory.Character import Character

__author__ = 'Muhammed5'
class Kitty(Character):
    def interactWith(self, obstacle):
        print("Kitty has encountered a",
        obstacle.action())