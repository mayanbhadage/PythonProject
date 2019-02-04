import random
from collections import OrderedDict

user_health = 100
comp_health = 100
moves = OrderedDict()
moves['X'] = 'x'
moves['Frost Bolt'] = 0
moves['Fire Bolt'] = 0
moves['Super Heal'] = 0
def randomAttack():
    moves['Frost Bolt'] = random.randint(18,25)
    moves['Fire Bolt'] = random.randint(10, 35)
    moves['Super Heal'] = random.randint(18, 25)
def askUser():
    choice = None

    while choice > 3 or choice <1:
        print('1 : FROST BOLT dmg(18-25)')
        print('2 : FIRE BOLT dmg(10-35)')
        print('3 : SUPER HEAL heal(18-25)\n')
        try:
            choice = int(raw_input("Please Choose Your Move (1 - 3)"))
        except:
            continue

    if choice == 1 or choice == 2:
        print("You have choosen {} Attack which will do {} damage to the **OTHER PLAYER**".format(moves.keys()[choice],moves.values()[choice]))
    else:
        print("You have choosen Super Heal which will heal you by {}".format(moves.values()[choice]))
    return choice

def h_Attack(index,health):
    if (index == 1 or index == 2):
        health = health - moves.values()[index]
    else:
        health = health + moves.values()[index]
    print("Other player health after the attack is {}".format(health))
    return health


randomAttack()
index = askUser()
h_Attack(index,comp_health)

