print("Welcome to the Tip Calculator.\n")

bill = float(input("What was the total bill? $"))
num_of_people = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

splitted_bill = round(((bill * (percentage / 100 + 1)) / num_of_people), 2)

print(f"\nEach person should pay ${splitted_bill}.")