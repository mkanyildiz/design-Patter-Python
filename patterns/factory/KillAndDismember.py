from factory.GameElementFactory import GameElementFactory
from factory.KungFuGuy import KungFuGuy
from factory.NastyWeapon import NastyWeapon

__author__ = 'Muhammed5'
class KillAndDismember(GameElementFactory):
    def makeCharacter(self): return KungFuGuy()
    def makeObstacle(self): return NastyWeapon()
