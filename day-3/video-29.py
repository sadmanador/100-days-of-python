print("Welcome to the rollercoaster!")
height = int(input("What is you height in CM? "))

if height >= 120:
    age = int(input("How old are you? "))
    if age <= 18:
        print("You have to pay $7")
    else:
        print("You have to pay $12")
else:
    print("Sorry, you're not allow to ride")
