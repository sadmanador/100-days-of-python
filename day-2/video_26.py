print("Welcome to the tip calculator")
totalBill = input("What was your total bill? ")
percentageOfBill = input("What percentage tip would you like to give? example: 10,12,15 ")
percentageTip = int(percentageOfBill) / 100 * int(totalBill)
billAndTip = int(totalBill) + percentageTip
numberOfPersons = input("How many person to split the bill? ")
finalBill = billAndTip / int(numberOfPersons)
print(f"Each person have to pay ${round(finalBill,2)}")