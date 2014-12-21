from factory.GameEnvironment import GameEnvironment
from factory.KillAndDismember import KillAndDismember
from factory.KittiesAndPuzzles import KittiesAndPuzzles

__author__ = 'Muhammed5'

g1 = GameEnvironment(KittiesAndPuzzles())
g2 = GameEnvironment(KillAndDismember())
g1.play()
g2.play()