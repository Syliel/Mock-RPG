#!/usr/bin/env python3
# Python Text RPG by Me
import cmd, textwrap, sys, os, time, random, zonemap

screen_width = 100

#Player setup
class Character(object):
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 200
        self.mp = 0
        self.attack = 10
        self.gold = 60
        self.pots = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False

myPlayer = Character()


class Warrior(Character):
    def __init__(self):
        Character.__init__(self)
        self.hp += 100
        self.mp += 50

warrior = Warrior()

class Mage(Character):
    def __init__(self):
        Character.__init__(self)
        self.hp += 60
        self.mp += 100

mage = Mage()

class Priest(Character):
    def __init__(self):
        Character.__init__(self)
        self.hp += 50
        self.mp += 50

priest = Priest()

class Goblin:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.attack = 5
        self.cpgain = 100

GoblinIG = Goblin("Goblin")

class Bear:
    def __init__(self, name):
        self.name = name
        self.hp = 70
        self.attack = 10
        self.cpgain = 150

BearIG = Bear("Bear")


####Title Screen####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game() #placeholder
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower () == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('##############################')
    print('# Welcome to the Text RPG!!! #')
    print('##############################')
    print('           ~Play~             ')
    print('           ~Help~             ')
    print('           ~Quit~             ')
    title_screen_selections()

def help_menu():
    os.system('clear')
    print("\n" + "Use up, down, left right to move")
    print("\n" + "Type your commands to do them")
    print("\n" + "Use look to inspect something")
    print("\n" + "Good luck and have fun!")
    title_screen_selections()



####MAP####
"""
    a1   a2 a3 a4
    ---------------
    |   |  |  |   |a4
    ---------------
    |   |  |  |   |b4
    ---------------
    |   |  |  |   |c4
    ---------------
    |   |  |  |   |d4
    ---------------
"""


solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }


### GAME INTERACTIVITY ###
def print_location():
        print('\n' + ('#' * (4 + len(myPlayer.location))))
        print('# ' + zonemap.zonemap[myPlayer.location]["ZONENAME"] + ' #')
        print('# ' + zonemap.zonemap[myPlayer.location]["DESCRIPTION"] + ' #')
        print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n" + "========================")
    print("What would you like to do?")
    action = input("\n> ")
    acceptable_actions = ['move', 'to', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look', 'explore', 'fight', 'run']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk', 'explore']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())
    elif action.lower() in ['fight']:
        fight()

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask + "\n> ")
    if dest in ['up', 'north']:
        destination = zonemap.zonemap[myPlayer.location]["UP"]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap.zonemap[myPlayer.location]["LEFT"]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap.zonemap[myPlayer.location]["RIGHT"]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap.zonemap[myPlayer.location]["DOWN"]
        movement_handler(destination)


def movement_handler(destination):
    if destination == '':
       print("\n" + "You cannot go that direction. Try again!")
    else:
        myPlayer.location = destination
        print("\n" + "You have moved to the " + zonemap.zonemap[myPlayer.location]["ZONENAME"] + ".")
        print_location()

def player_examine(action):
    if zonemap.zonemap[myPlayer.location]["SOLVED"]:
        print("\n" + "You have already exhausted this zone.")
    else:
        print("\n" + zonemap.zonemap[myPlayer.location]["EXAMINATION"])



def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        #here handle if puzzles have been solved, boss defeated.

def setup_game():
    global player_name
    os.system('clear')

    ### Name Collecting###
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")


    question2 = "What role do you want to play?\n"
    question2added = "(You can play as warrior, priest or mage)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("\n> ")
    valid_jobs = ['warrior', 'mage', 'priest']
    if player_job.lower() == 'warrior':
        myPlayer = Warrior()
    if player_job.lower() == 'mage':
        myPlayer = Mage()
    if player_job.lower() == 'priest':
        myPlayer = Priest()
    print("Your are now a " + str(player_job) + "." + " Your HP and MP are " + str(myPlayer.hp) + " and " + str(myPlayer.mp) + '!\n')
    print("You have " + str(myPlayer.gold) + ' gold!\n')
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")


    #Introduction
    question3 = "\n Hello, " + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = "Welcome to this fantasy world!\n"
    speech2 = "I hope it greets you well!\n"
    speech3 = "Just make sure not to get too lost...\n"
    speech4 = "Hehehheh...\n"

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    os.system('clear')
    print("###################")
    print("# Let's start now #")
    print("###################")
    main_game_loop()

def fight():
    global myPlayer
    global enemy
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        enemy = GoblinIG
    else:
        enemy = BearIG
    os.system('clear')
    print("%s     vs     %s" % (player_name, enemy.name))
    Pattack = random.randint(0, myPlayer.attack)
    Eattack = random.randint(0, enemy.attack)
    if Pattack == 0:
        print("You missed")
    else:
        print("You hit the monster for " + str(myPlayer.attack) + "damage")
        enemy.hp -= myPlayer.attack
    if Eattack == 0:
        print("The enemy missed")
    else:
        print("The monster hit for " + str(enemy.attack) + "damage")
        myPlayer.hp -= enemy.attack
    while myPlayer.hp > 0:
        fight()
    if myPlayer.hp <= 0:
        print("You lose.")
    if enemy.hp <= 0:
        print("You win the fight")
        main_game_loop()

title_screen()
