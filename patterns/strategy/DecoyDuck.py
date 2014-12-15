#!/usr/bin/python
# -*- coding: <encoding name> -*-
from strategy.Duck import Duck
from strategy.FlyNoWay import FlyNoWay
from strategy.MuteQuack import MuteQuack

__author__ = 'Muhammed5'


class DecoyDuck(Duck):
    def __init__(self):
        Duck.__init__(self)
        fly_no_way_instance = FlyNoWay()
        self.set_fly_behavior(fly_no_way_instance)
        mute_instance = MuteQuack()
        self.set_quack_behavior(mute_instance)
        print("I'm a Decoy Duck")