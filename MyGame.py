import MyGameMethods as gm

next_turn = None
gm.randomAttack()
chance = gm.firstTurn()
if chance == 1:
    user_choice = gm.askUser()
    if user_choice == 1 or user_choice == 2:
        gm.comp_health = gm.attack(user_choice, gm.comp_health)
        print ("Computer's health after this attack is {}\n".format(gm.comp_health))
    else:
        gm.user_health = gm.heal(user_choice, gm.user_health)
        print ("User's health after heal is {}\n".format(gm.user_health))
    next_turn = "Computer"
else:
    computer_choice = gm.computer_choice(gm.comp_health)
    if computer_choice == 1 or computer_choice == 2:
        gm.user_health = gm.attack(computer_choice, gm.user_health)
        print ("User's health after this attack is {}\n".format(gm.user_health))
    else:
        gm.comp_health = gm.heal(computer_choice, gm.comp_health)
        print ("Computer's health after heal is {}\n".format(gm.comp_health))
    next_turn = "User"

while True:
    gm.randomAttack()
    if(next_turn == "User"):
        user_choice = gm.askUser()
        if user_choice == 1 or user_choice == 2:
            gm.comp_health = gm.attack(user_choice, gm.comp_health)
            print ("Computer's health after this attack is {}\n".format(gm.comp_health))
        else:
            gm.user_health = gm.heal(user_choice, gm.user_health)
            print ("User's health after heal is {}\n".format(gm.user_health))
        if gm.check_win(gm.comp_health):
            print("User Won!!")
            break
        else:
            next_turn = "Computer"
    else:
        computer_choice = gm.computer_choice(gm.comp_health)
        if computer_choice == 1 or computer_choice == 2:
            gm.user_health = gm.attack(computer_choice, gm.user_health)
            print ("User's health after this attack is {}\n".format(gm.user_health))
        else:
            gm.comp_health = gm.heal(computer_choice, gm.comp_health)
            print ("Computer's health after heal is {}\n".format(gm.comp_health))
        next_turn = "User"
        if gm.check_win(gm.user_health):
            print("Computer Won!")
            break
        else:
            next_turn = "User"

