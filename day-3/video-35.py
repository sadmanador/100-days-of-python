print("Welcome to the pizza house")
size = input("What size of pizza do you want? S, M or L?")
add_pepperoni = input("Would you like to have some pepperoni? Y & N")
extra_cheese = input("Would you like to have extra cheese")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill+= 25
    
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is ${bill}")
