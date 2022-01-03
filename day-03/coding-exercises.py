# 1 - Odd or Even

# modulo operator: % -> returns the remainder(int) of the division

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This number is even.")
else: 
    print("This number is odd.")

# 2 - BMI 2.0

height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))

bmi = round(weight / (height**2))
res = ""

if (bmi < 18):
    res = "you are underweight"
elif (bmi < 25):
    res = "you have a normal weight"
elif (bmi < 30):
    res = "you are slightly overweight"
elif (bmi < 35):
    res = "you are obese"
else:
    res = "you are clinically obese"

print(f"Your BMI is {bmi}, {res}.")


# 3 - Leap Year

year = int(input("\nWhich year you want to check? "))
isLeap = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            isLeap = True
        else:
            isLeap = False
    else:
        isLeap = True
else:
    isLeap = False

if isLeap:
    print("Leap year.")
else:
    print("Not leap year.")

# 4 - Pizza Order Practice

print("\nWelcome to Pizza Venezia!")
size = input("What size pizza do you want? Small (S), Medium (M) or Large (L): ")
add_pepperoni = input("Do you want extra pepperoni? Y or N: ")
add_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
elif size == 'L':
    bill = 25
        
if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    elif size == 'M' or size == 'L':
        bill += 3

if add_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")

# 5 - Love Calculator

print("\nWelcome to the Love Calculator.")

my_name = input("What's your name? ")
your_name = input("What's their name? ")
all_names = (my_name + your_name).lower()

key = "truelove"

true = all_names.count(key[0]) + all_names.count(key[1]) + all_names.count(key[2]) + all_names.count(key[3])
love = all_names.count(key[4]) + all_names.count(key[5]) + all_names.count(key[6]) + all_names.count(key[7])

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}%. you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your love score is {love_score}%. you are alright together.")
else:
    print(f"\nYour love score is {love_score}%.")
