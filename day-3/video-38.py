print("Welcome to the treasure island \n Your mission is to find the treasure.")
way = input("which path you want to go? right of left \n")

if way == 'right':
    print("Game over, try again!")
else:
    path = input("What you wanna do? wait or swim \n")
    if path == 'swim':
        print("Game over, try again!")

    door = input("which door you wanna enter? red, yellow or blue? \n")
    if door == "yellow":
        print("you win!")
    else:
        print("Game over, try again!")
