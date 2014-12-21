from factory.GameElementFactory import GameElementFactory
from factory.Kitty import Kitty
from factory.Puzzle import Puzzle

__author__ = 'Muhammed5'
class KittiesAndPuzzles(GameElementFactory):
    def makeCharacter(self): return Kitty()
    def makeObstacle(self): return Puzzle()
