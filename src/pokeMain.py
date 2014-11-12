import Person
import Pokemon
import Item
import Moves
import Location
from random import randint

def main():
    print "Welcome to the world of Pokemon!\n"
    
    user_input = raw_input("Let's start off by getting your name.\n")
    trainer = Person.Trainer(user_input)
    print "Hi there, " + user_input + ". Prepare yourself for the journey you are about to embark upon!\n"
     
    rival = Person.Enemy("Gary", [Pokemon.Squirtle(5)])
    
    pokemon = Pokemon(1)

    
    user_input = 4
    while user_input > 3:
        user_input = input("Choose your Pokemon\n1.Charmander\n2.Squirtle\n3.Bulbasaur\n")
        if user_input == 1:
            pokemon = Pokemon.Charmander(5)
        elif user_input == 2:
            pokemon = Pokemon.Squirtle(5)
        elif user_input == 3:
            pokemon = Pokemon.Bulbasaur(5)
        else: 
            print "Please choose from numbers 1-3\n"
    
    
    print "You chose " + pokemon.name
    trainer.party.append(pokemon)
    user_input = input("1. Menu\n2. Battle \n")
    if user_input == 1:
        menu(trainer)
    elif user_input == 2:
        preBattle(trainer, rival)
        print "This is a change"
         

#General menu for gameplay and in battle
def menu(trainer):
    '''
    print "1. Party"
    print "2. Bag"
    print "3. Exit"
    '''
    user_input = input()
    count = 1
    if user_input == 1:
        for pokemon in trainer.party:
            print str(count) + "." + pokemon.name + " Lvl: " + str(pokemon.level) + " (HP: " + str(pokemon.health) + "/100)\n"
            count = count + 1
    elif user_input == 2:
        print trainer.name + "'s Bag:\n"
        for item in trainer.bag:
            print str(count) + "." + item.name + " x " + str(item.quantity) + "\n"
            count = count + 1
    elif user_input == 3:
        return "n"
    
        
    print "Press B to go back"
    
    while user_input != "B":
        user_input = raw_input()
        if user_input == "B":
            menu(trainer)
        else:
            print "Incorrect, try again"

#Initial screen that displays before battle    
def preBattle(trainer1, trainer2):
    print trainer2.name + " challenges " + trainer1.name + " to a battle!"
    print "Let the battle begin!\n"
    battleTransition(trainer1, trainer2)
    
def battleTransition(trainer1, trainer2):
    currentAttacker = trainer1.party[0]
    currentDefender = trainer2.party[0]
    print trainer1.name + " yells Go " + currentAttacker.name + "! I choose you!"
    print trainer2.name + " yells Go " + currentDefender.name + "! I choose you!\n"
    battle(currentAttacker, currentDefender, trainer1)
    
def battle(Pokemon1, Pokemon2, trainer): 
    coin = 1
    
    while Pokemon1.health > 0 and Pokemon2.health > 0:
        
        
         
        if coin % 2 == 1:
            print "What would you like to do?"
            decision = battleMenu(Pokemon1, Pokemon2)
            if decision == 1: 
                chooseMove(Pokemon1, Pokemon2)
                #User decides to run
            elif decision == 2:
                #Change this method call so that it only brings up the menu
                menu(trainer)
            elif decision == 3:
                break
        #Enemy pokemon's turn
        elif coin % 2 == 0:
            print "Enemy " + Pokemon2.name + " chooses a move..."
            enemyMove(Pokemon2, Pokemon1)
        coin = coin + 1
        
    if Pokemon1.health <= 0:
        print Pokemon1.name + " has fainted."
    elif Pokemon2.health <=0:
        print Pokemon2.name + " has fainted."
        
    else:
        print "You run away."
    
def enemyMove(attacker, defender):
    number_moves = len(attacker.moves)
    move = randint(0, number_moves - 1)
    print attacker.name + " attacks " + defender.name + " with " + attacker.moves[move].name + " for " + str(attacker.moves[move].damage) + " damage."
    defender.health = defender.health - attacker.moves[move].damage
        
    
def chooseMove(attacker, defender):
    choice = False
    #Loops until user makes a valid move choice
    while (not choice):
        print "Pick a move for " + attacker.name + " to use"
        count = 0;
        for move in attacker.moves:
            count = count + 1
            print str(count) + "." + move.name
        
        
        
        option = input()
        option = option - 1
        
        if option <= len(attacker.moves):
            print attacker.name + " attacks " + defender.name + " with " + attacker.moves[option].name + " for " + str(attacker.moves[option].damage) + " damage."
            defender.health = defender.health - attacker.moves[option].damage
            choice = True
        else:
            print "Invalid choice. Choose a number 1 - " + str(len(attacker.moves)) + "\n"
            
        
    print "\n"

    
def battleMenu(Pokemon1, Pokemon2):
    print Pokemon1.name + " (Health: " + str(Pokemon1.health) +")"
    print Pokemon2.name + " (Health: " + str(Pokemon2.health) +")"
    print "\n"
    
    user = input("1.Fight\n2.Bag\n3.Run\n")
    return user

#Gives the users a decision tree
def decision(options):
    counter = 1
    for option in options:
        print str(counter) + ". " + option
        counter += 1
    user_input = raw_input()
    while user_input > counter or user_input < 1 or user_input:
        print "Invalid choice"
        decision(options)
    print "\n"
    
    return user_input
    
    
    
    
    
    
def test():
    user = Person.Trainer()
    user.party = [Pokemon.Charmander(5)]
    user.name = "Kyle"
    gameState = True
    currArea = "PalletTown"
    while gameState == True:
        
        area = eval("Location." + currArea + "()")
        userDecision = area.load(Person)
        
        
        decisionType = userDecision[0]
        strLength = len(userDecision)
        userDecision = userDecision[1:strLength]
        #If decision is an area, we want to load it on next loop
        if decisionType == "L":
            
            currArea = userDecision
            print "wesdfsdaff"
            break
        #If decision is a person, we want to talk to them on next loop
        elif decisionType == "P":
            npc = eval("Person." + userDecision + "()")
            print npc.name + ": " + npc.dialogue
            if (npc.battle == True):
                preBattle(user, npc)
                
            break
        #If decision is a battle, we want to load it and load location after commencing
        


   
test()

    
    
        