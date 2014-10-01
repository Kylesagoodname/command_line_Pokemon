'''
Created on Aug 14, 2014

@author: kyle
'''
class Item(object):
    def __init__(self, quantity):
        self.quantity = quantity

class Pokeball(Item):
    type = "Ball"
    name = "Pokeball"

class SuperPotion(Item):
    type = "Potion"
    name = "Super Potion"
    heal = 50