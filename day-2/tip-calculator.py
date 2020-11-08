print("Welcome to the Tip Calculator.\n")

bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

splitted_bill = round(((bill * (tip / 100 + 1)) / people), 2)

print(f"\nEach person should pay ${splitted_bill}.")