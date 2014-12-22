from patterns.decorator.Fisch import Fisch
from patterns.decorator.Pommes import Pommes
from patterns.decorator.Salat import Salat
from patterns.decorator.Steak import Steak
from patterns.decorator.WienerSchnitzel import WienerSchnitzel
__author__ = 'mwech'
"""
@author: Maximilian Wech
@version: 20141222
@description: Main
"""
schnitzel = WienerSchnitzel()
print(schnitzel.getBezeichnung() + ": €" + str(schnitzel.getPreis()))

steak = Pommes(Steak())
print(steak.getBezeichnung() + ": €" + str(steak.getPreis()))

fisch = Salat(Pommes(Fisch()))
print(fisch.getBezeichnung() + ": €" + str(fisch.getPreis()))