print("Welcome to the pass/fail calculator")
marks = int(input("How much you get? "))
if marks >= 33:
    print('You passed!')
elif marks > 100:
    print("There might be an error in the marks")
else:
    print("You failed")