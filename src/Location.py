'''
Created on Aug 14, 2014

@author: kyle
'''
class Location(object):
    locations = []
    def __init__(self):
        pass

    def load(self, trainer):  
        counter = 1
        print self.name
        print self.description + "\n"
        print "What would you like to do?"
        for location in self.locations:
            print str(counter) + ". Go to " + location
            counter += 1
        for person in self.people:
            print str(counter) + ". Talk to " + person
            counter += 1
        
        
        
        user_input = input()
        if user_input <= len(self.locations):
            return "L" + self.locations[user_input - 1]
        elif user_input <= len(self.locations) + len(self.people):
            return"P" + self.people[user_input - 1 - len(self.locations)]
         
        else:
           
            print "test"


    
    


class OaksLab(Location):
    name = "Oaks Lab"
    description = "You walk through the doors of Oak's Lab and are greeted by a familiar face. The lab is bustling with activity."
    locations = ["PalletTown"]
    people = ["ProfOak"]
    
    
class Home(Location):
    name = "Home"
    description = "You walk in through the front door and smell the warm aroma of fresh baked apple pie."
    locations = ["PalletTown"]
    people = ["Mom"]
    
    

        
class PalletTown(Location):
    name = "Pallet Town"
    description = "You walk out into the sunshine of Pallet Town and you begin to feel at home."
    locations = ["OaksLab", "Home", "Route1"]
    people = ["PalletTownMan1"]

class Route1(Location):
    name = "Route 1"
    description = "You come across a grassy pasture teeming with wild Pokemon. The wind blows gently.."
    locations = ["PalletTown"]
    people = ["Gary"]
    