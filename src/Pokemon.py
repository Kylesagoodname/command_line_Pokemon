import Moves
'''
Created on Aug 14, 2014

@author: kyle
'''
class Pokemon(object):
    health = 100
    def __init__(self, level):
        self.level = level

class Charmander(Pokemon):
    name = "Charmander"
    moves = [Moves.Scratch(), Moves.Ember()]
    
class Squirtle(Pokemon):
    name = "Squirtle"
    moves = [Moves.Tackle(), Moves.WaterGun()]
    
class Bulbasaur(Pokemon):
    name = "Bulbasaur"
    moves = [Moves.Tackle(), Moves.VineWhip()]    
