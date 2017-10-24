#!/usr/bin/env python3
# Python Text RPG by Me
import cmd, textwrap, sys, os, time, random

screen_width = 100

#Player setup
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'

myPlayer = player()

####Title Screen####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() #placeholder
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
    print("Use up, down, left right to move")
    print("Type your commands to do them")
    print("use look to inspect something")
     print("Good luck and have fun!")
    title_screen_selections()

#game function
def start_game():



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

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False
                 'b1': False, 'b2': False, 'b3': False, 'b4': False
                 'c1': False, 'c2': False, 'c3': False, 'c4': False
                 'd1': False, 'd2': False, 'd3': False, 'd4': False
                 }

zonemap = {'a1': {
           ZONENAME: 'Town Market',
           DESCRIPTION = 'There are lots of delicious foods to eat'
           EXAMINATION = 'You see fruits and bananas everywhere'
           SOLVED = False
           UP = '',
           DOWN = 'b1',
           LEFT = '',
           RIGHT = 'a2',
           },
           'a2': {
           ZONENAME: 'Town Entrance',
           DESCRIPTION = 'There"s a massive door that leads to the town.'
           EXAMINATION = 'You see guards and a town ahead.'
           SOLVED = False
           UP = '',
           DOWN = 'b2',
           LEFT = 'a1',
           RIGHT = 'a3',
           },
           'a3' :{
           ZONENAME: 'Town Square',
           DESCRIPTION = 'There"s a festival today!'
           EXAMINATION = 'You see balloons and kids running around.'
           SOLVED = False
           UP = ''
           DOWN = 'b3',
           LEFT = 'a2',
           RIGHT = 'a4',
           },
           'a4' :{
           ZONENAME: 'Town Hall',
           DESCRIPTION = 'This is Town Hall.'
           EXAMINATION = 'You see the Town Hall'
           SOLVED = False
           UP = '',
           DOWN = 'b4',
           LEFT = 'a3',
           RIGHT = '',
           },
          'b1' :{
           ZONENAME: "",
           DESCRIPTION = 'description'
           EXAMINATION = 'examine'
           SOLVED = False
           UP = 'up', 'north'
           DOWN = 'down', 'south'
           LEFT = 'left', 'west'
           RIGHT = 'right', 'east'
           },
          'b2' :{
           ZONENAME: 'Home',
           DESCRIPTION = 'This is your home'
           EXAMINATION = 'Your home looks the same - nothing has changed'
           SOLVED = False
           UP = 'a2',
           DOWN = 'c2',
           LEFT = 'b1',
           RIGHT = 'b3',
           },
           'b3' :{
           ZONENAME: '',
           DESCRIPTION = 'description'
           EXAMINATION = 'examine'
           SOLVED = False
           UP = 'up', 'north'
           DOWN = 'down', 'south'
           LEFT = 'left', 'west'
           RIGHT = 'right', 'east'
           },


   }

### GAME INTERACTIVITY ###
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.position][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n" + "========================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ['move', 'to', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:


