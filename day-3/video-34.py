print("Welcome to the rollercoaster!")
height = int(input("What is you height in CM? "))
bill = 0

if height >= 120:
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print(f"Child ticket ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth ticket ${bill}")
    else:
        bill = 12
        print(f"Adult ticket ${bill}")

    wants_photo = input("Do you want a photo? Y or N.\n")
    if wants_photo == 'Y':
        bill += 3
 
    
    print(f"Your total bill is ${bill}")
else:
    print("Sorry, you're not allow to ride")
