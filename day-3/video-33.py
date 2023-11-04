print("Welcome to leap year finder")
year = int(input("enter any year? \n"))

if year % 4 == 0:
    if year % 100:
        if year % 400:
            print("it's a leap year") 
        else:
            print("it's not a leap year") 
    else:
        print("it's not a leap year")   
else:
    print("it's not a leap year")    