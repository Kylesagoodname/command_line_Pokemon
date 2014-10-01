import Item
import Pokemon

class Person(object):

    party = []
    def __init__(self):
        pass
    
    
class Trainer(Person):
    name = ""
    bag = [Item.Pokeball(1)]
    
    def use(self, item):
        if item.quantity > 1:
            print "You can only use one at a time!"
        else:
            for obj in self.bag:
                if item.name == obj.name:
                    obj.quantity = obj.quantity - 1
                    if obj.quantity == 0:
                        self.bag.remove(obj)
                    return obj.quantity
                    
    def add(self, item):
        found = False
        for obj in self.bag:
            if item.name == obj.name:
                obj.quantity = obj.quantity + item.quantity
                found = True
        if (not found):
            self.bag.append(item)
    
#Enemy trainers are initialized with a party of pokemon
class Enemy(Person):
    def __init__(self, name, party):
        self.name = name
        self.party = party


class PalletTownMan1(Person):
    def __init_(self):
        pass
    battle = True;
    party = [Pokemon.Bulbasaur(5)]
    dialogue = "Hi, my name is Man."
    name = "Jerry"
    
   


