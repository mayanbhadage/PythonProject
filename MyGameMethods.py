import random
from collections import OrderedDict

user_health = 100
comp_health = 100
current_player = None
moves = OrderedDict()
moves['X'] = 'x'
moves['Frost Bolt'] = 0
moves['Fire Bolt'] = 0
moves['Super Heal'] = 0


def randomAttack():
    moves['Frost Bolt'] = random.randint(18, 25)
    moves['Fire Bolt'] = random.randint(10, 35)
    moves['Super Heal'] = random.randint(18, 25)


def askUser():
    choice = None

    while choice > 3 or choice < 1:
        print('1 : FROST BOLT dmg(18-25)')
        print('2 : FIRE BOLT dmg(10-35)')
        print('3 : SUPER HEAL heal(18-25)\n')
        try:
            choice = int(raw_input("Please Choose Your Move (1 - 3)\n"))
        except:
            continue

    if choice == 1 or choice == 2:
        print("USER have choosen {} Attack which will do {} damage to the Computer".format(moves.keys()[choice],
                                                                                                  moves.values()[
                                                                                                      choice]))
    else:
        print("USER have choosen Super Heal which will heal you by {}".format(moves.values()[choice]))
    return choice


def attack(index, health):
    new_health = health - moves.values()[index]
    if new_health < 0:
        new_health = 0
    return new_health

def heal(index, health):
    if(health<100):
        new_health = health + moves.values()[index]
    else:
        new_health = 100
    if(new_health>100):
        new_health = 100
    return new_health

def firstTurn():
    turn = random.randint(1, 2)
    if(turn == 1):
        print("User will play first!")

    else:
        print("Computer will play first!")

    return turn

def computer_choice():
    choice = random.randint(1, 3)
    if choice == 1 or choice == 2:
        print("COMPUTER have choosen {} Attack which will do {} damage to the USER".format(moves.keys()[choice],
                                                                                                  moves.values()[
                                                                                                      choice]))
    else:
        print("COMPUTER have choosen Super Heal which will heal you by {}".format(moves.values()[choice]))

    return choice



def check_win(health):
    if health <= 0:
        return True
    else:
        return False