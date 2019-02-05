import random
import numpy as np
from collections import OrderedDict
import time

user_health = 100
comp_health = 100

moves = OrderedDict()
moves['X'] = 'x'
moves['Frost Bolt'] = 0
moves['Fire Bolt'] = 0
moves['Super Heal'] = 0


def intro():
    print("-----------------------------------------------------")
    print("\tWelcome to this Magical Game called SuperPower!!")
    print("-----------------------------------------------------")
    print("The rules for the game are very simple")
    print("You and the Evil-Computer have 3 Super Powers")
    print("\t1. Frost Bolt which deal damage between 18 to 25")
    print("\t2. Fire Bolt which deal damage between 10 and 35")
    print("\t3. Super Heal which increase health between 18 to 25")
    print("--------------------------------------------------")
    print("\tYour Goal is to defeat this Evil Computer")
    print("--------------------------------------------------")
    print("\t BEST OF LUCK!\n")
    time.sleep(5)


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
        print ("\n"*50)
    if choice == 1 or choice == 2:
        print("USER have chosen {} Attack which will do {} damage to the Computer".format(moves.keys()[choice],
                                                                                          moves.values()[
                                                                                              choice]))
    else:
        print("USER have chosen Super Heal which will heal USER by {}".format(moves.values()[choice]))
    return choice


def attack(index, health):
    new_health = health - moves.values()[index]
    if new_health < 0:
        new_health = 0
    return new_health


def heal(index, health):
    if health < 100:
        new_health = health + moves.values()[index]
    else:
        new_health = 100
    if new_health > 100:
        new_health = 100
    return new_health


def firstTurn():
    turn = random.randint(1, 2)
    if turn == 1:
        print("User will play first!")

    else:
        print("Computer will play first!")

    return turn


def computer_choice(health):
    print("Thinking....\n")
    time.sleep(1.5)
    print ("\n" * 50)
    if health <= 35:
        choice = np.random.choice(np.arange(1, 4), p=[0.2, 0.3, 0.5])
        if choice == 1 or choice == 2:
            print("COMPUTER have chosen {} Attack which will do {} damage to the USER".format(moves.keys()[choice],
                                                                                              moves.values()[
                                                                                                  choice]))
        else:
            print("COMPUTER have chosen Super Heal which will COMPUTER you by {}".format(moves.values()[choice]))
        return choice

    else:
        choice = random.randint(1, 3)
        if choice == 1 or choice == 2:
            print("COMPUTER have chosen {} Attack which will do {} damage to the USER".format(moves.keys()[choice],
                                                                                              moves.values()[
                                                                                                  choice]))
        else:
            print("COMPUTER have chosen Super Heal which will Computer you by {}".format(moves.values()[choice]))

        return choice


def print_health(uh, ch):
    print ("################")
    print ("User Health : {}".format(uh))
    print ("Comp Health : {}".format(ch))
    print ("################")


def check_win(health):
    if health <= 0:
        return True
    else:
        return False
