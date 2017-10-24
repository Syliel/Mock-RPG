#!/usr/bin/env python3
# Python Text RPG by Me
import cmd, textwrap, sys, os, time, random

screen_width = 100

#Player setup
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.attack = 10
        self.gold = 0
        self.pots = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False

myPlayer = player()

class Goblin:
    def __init__(self, name):
        self.name = name
        self.hp = 30
        self.attack = 10
        self.cpgain = 100

GoblinIG = Goblin("Goblin")

class Bear:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 20
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
            start_game()
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

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }

zonemap = {'a1': {
           ZONENAME: 'Town Market',
           DESCRIPTION: 'There are lots of delicious foods to eat.',
           EXAMINATION: 'You can sell and buy here.',
           SOLVED: False,
           UP: '',
           DOWN: 'b1',
           LEFT: '',
           RIGHT: 'a2',
           },
           'a2': {
           ZONENAME: 'Town Entrance',
           DESCRIPTION: 'There\'s a massive door that leads to the town.',
           EXAMINATION: 'You see guards and a town ahead.',
           SOLVED: False,
           UP: '',
           DOWN: 'b2',
           LEFT: 'a1',
           RIGHT: 'a3',
           },
           'a3' :{
           ZONENAME: 'Town Square',
           DESCRIPTION: 'There\'s a festival today!',
           EXAMINATION: 'You see balloons and kids running around.',
           SOLVED: False,
           UP: '',
           DOWN: 'b3',
           LEFT: 'a2',
           RIGHT: 'a4',
           },
           'a4' :{
           ZONENAME: 'Town Hall',
           DESCRIPTION: 'This is Town Hall.',
           EXAMINATION: 'You see the Town Hall',
           SOLVED: False,
           UP: '',
           DOWN: 'b4',
           LEFT: 'a3',
           RIGHT: '',
           },
          'b1' :{
           ZONENAME: 'West Fields',
           DESCRIPTION: 'You see an enemy ahead!',
           EXAMINATION: 'You can fight the goblin or run',
           SOLVED: False,
           UP: 'a1',
           DOWN: 'c1',
           LEFT: '',
           RIGHT: 'b2',
           },
          'b2' :{
           ZONENAME: 'Home',
           DESCRIPTION: 'This is your home',
           EXAMINATION: 'There\'s nothing to do here. Go out and explore!',
           SOLVED: False,
           UP: 'a2',
           DOWN: 'c2',
           LEFT: 'b1',
           RIGHT: 'b3',
           },
           'b3' :{
           ZONENAME: 'East Fields',
           DESCRIPTION: 'You see something shiny',
           EXAMINATION: 'You pick up the shiny object. You gain 50 cp',
           SOLVED: False,
           UP: 'a3',
           DOWN: 'c3',
           LEFT: 'b2',
           RIGHT: 'b4',
           },
           'b4' :{
           ZONENAME: 'Field\'s Edge',
           DESCRIPTION: 'The edge of a vast field. You see something south.',
           EXAMINATION: 'There\'s nothing here',
           SOLVED: False,
           UP: 'a4',
           DOWN: 'c4',
           LEFT: 'b3',
           RIGHT: '',
           },

           'c1' :{
           ZONENAME: 'West Mountains',
           DESCRIPTION: 'You see something to fight.',
           EXAMINATION: 'You can fight or run!',
           SOLVED: False,
           UP: 'b1',
           DOWN: 'd1',
           LEFT: '',
           RIGHT: 'c2',
           },
           'c2' :{
           ZONENAME: 'Mountains',
           DESCRIPTION: 'These mountains are steep, but you feel you can go travese them.',
           EXAMINATION: 'You see lots of snow, but nothing else.',
           SOLVED: False,
           UP: 'b2',
           DOWN: 'd2',
           LEFT: 'c1',
           RIGHT: 'c3',
           },
           'c3' :{
           ZONENAME: 'East Mountains',
           DESCRIPTION: 'You see something shiny here!',
           EXAMINATION: 'You\'ve picked up 60 cp!',
           SOLVED: False,
           UP: 'b3',
           DOWN: 'd3',
           LEFT: 'c2',
           RIGHT: 'c4',
           },
           'c4' :{
           ZONENAME: 'Mountains Edge',
           DESCRIPTION: 'You see something up ahead!',
           EXAMINATION: 'You can fight or run!',
           SOLVED: False,
           UP: 'b4',
           DOWN: 'd4',
           LEFT: 'c3',
           RIGHT: '',
           },
           'd1' :{
           ZONENAME: 'West Village',
           DESCRIPTION: 'This is the West Village',
           EXAMINATION: 'Oddly, there\'s no townfolk around',
           SOLVED: False,
           UP: 'c1',
           DOWN: '',
           LEFT: '',
           RIGHT: 'd2',
           },
           'd2' :{
           ZONENAME: 'Village Center',
           DESCRIPTION: 'You see one lady who seems to be going through her purse',
           EXAMINATION: 'You talk to the lady, but she doesn\'t respond.',
           SOLVED: False,
           UP: 'c2',
           DOWN: '',
           LEFT: 'd1',
           RIGHT: 'd3',
           },
           'd3' :{
           ZONENAME: 'East Village',
           DESCRIPTION: 'You see something shiny!',
           EXAMINATION: 'You\'ve picked up 30 cp!',
           SOLVED: False,
           UP: 'c3',
           DOWN: '',
           LEFT: 'd2',
           RIGHT: 'd4',
           },
           'd4' :{
           ZONENAME: 'Village Edge',
           DESCRIPTION: 'This is the end of the village.',
           EXAMINATION: 'You see nothing ahead of you.',
           SOLVED: False,
           UP: 'c4',
           DOWN: '',
           LEFT: 'd3',
           RIGHT: '',
           },

   }

### GAME INTERACTIVITY ###
def print_location():
        print('\n' + ('#' * (4 + len(myPlayer.location))))
        print('# ' + zonemap[myPlayer.location][ZONENAME] + ' #')
        print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
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
        player_prefight(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask + "\n> ")
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    if destination == '':
       print("\n" + "You cannot go that direction. Try again!")
    else:
        myPlayer.location = destination
        print("\n" + "You have moved to the " + zonemap[myPlayer.location][ZONENAME] + ".")
        print_location()

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("\n" + "You have already exhausted this zone.")
    else:
        print("\n" + zonemap[myPlayer.location][EXAMINATION])

def player_prefight(action):
    global enemy
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        enemy = GoblinIG
    else:
        enemy = BearIG
    fight()

def fight():
    print("%s     vs     %s" % (myPlayer.name, enemy.name))




def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        #here handle if puzzles have been solved, boss defeated.

def setup_game():
    os.system('clear')

    ### Name Collecting###
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

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
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print('You are now a ' + player_job + '!\n')
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print('You are now a ' + player_job + '!\n')
    #Player stats
    if myPlayer.job is 'warrior':
        self.hp = 120
        self.mp = 20
    elif myPlayer.job is 'mage':
        self.hp = 40
        self.mp = 120
    elif myPlayer.job is 'priest':
        self.hp = 60
        self.mp = 60

    #Introduction
    question3 = "Welcome, " + player_name + " the " + player_job + ".\n"
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



title_screen()
