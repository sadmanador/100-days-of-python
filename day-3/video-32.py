height = input("enter your height in meter? ")
weight = input("enter your weight in Kg? ")

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f'Your MBI is {bmi}, which means you are under weight')
elif bmi < 25:
    print(f'Your MBI is {bmi}, which means you are normal weight')
elif bmi < 30:
    print(f'Your MBI is {bmi}, which means you are over weight')
elif bmi < 35:
    print(f'Your MBI is {bmi}, which means you are obese')
else:
    print(f'Your MBI is {bmi}, which means you are clinically obese')
