import MyGameMethods as gm

gm.intro()
next_turn = None
gm.randomAttack()
chance = gm.firstTurn()
if chance == 1:
    user_choice = gm.askUser()
    if user_choice == 1 or user_choice == 2:
        gm.comp_health = gm.attack(user_choice, gm.comp_health)
        gm.print_health(gm.user_health,gm.comp_health)
    else:
        gm.user_health = gm.heal(user_choice, gm.user_health)
        gm.print_health(gm.user_health,gm.comp_health)
    next_turn = "Computer"
else:
    computer_choice = gm.computer_choice(gm.comp_health)
    if computer_choice == 1 or computer_choice == 2:
        gm.user_health = gm.attack(computer_choice, gm.user_health)
        gm.print_health(gm.user_health,gm.comp_health)
    else:
        gm.comp_health = gm.heal(computer_choice, gm.comp_health)
        gm.print_health(gm.user_health, gm.comp_health)
    next_turn = "User"

while True:
    gm.randomAttack()
    if(next_turn == "User"):
        user_choice = gm.askUser()
        if user_choice == 1 or user_choice == 2:
            gm.comp_health = gm.attack(user_choice, gm.comp_health)
            gm.print_health(gm.user_health,gm.comp_health)

        else:
            gm.user_health = gm.heal(user_choice, gm.user_health)
            gm.print_health(gm.user_health,gm.comp_health)
        if gm.check_win(gm.comp_health):
            print("You Won!!")
            break
        else:
            next_turn = "Computer"
    else:
        computer_choice = gm.computer_choice(gm.comp_health)
        if computer_choice == 1 or computer_choice == 2:
            gm.user_health = gm.attack(computer_choice, gm.user_health)
            gm.print_health(gm.user_health,gm.comp_health)
        else:
            gm.comp_health = gm.heal(computer_choice, gm.comp_health)
            gm.print_health(gm.user_health,gm.comp_health)
        next_turn = "User"
        if gm.check_win(gm.user_health):
            print("Evil Computer Won!")
            break
        else:
            next_turn = "User"

