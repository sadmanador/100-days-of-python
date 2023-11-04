currentAge = input("what is your current age?")

yearsLeft = 90 - int(currentAge)
print(yearsLeft)

monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365

print(f"You have days {daysLeft} left, weeks {weeksLeft} left and months {monthsLeft} left")
