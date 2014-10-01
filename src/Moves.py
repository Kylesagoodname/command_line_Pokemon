'''
Created on Aug 14, 2014

@author: kyle
'''
class Move(object):
    def __init__(self):
        pass

class Scratch(Move):
    name = "Scratch"
    damage = 20
    
class Ember(Move):
    name = "Ember"
    damage = 30

class Tackle(Move):
    name = "Tackle"
    damage = 20
    
class WaterGun(Move):
    name = "WaterGun"
    damage = 30
   
class VineWhip(Move):
    name = "Vine Whip"
    damage = 40