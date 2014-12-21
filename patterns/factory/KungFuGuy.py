from factory.Character import Character

__author__ = 'Muhammed5'
class KungFuGuy(Character):
    def interactWith(self, obstacle):
        print("KungFuGuy now battles a",
        obstacle.action())