#Comparison Operators
# > , < , >= , <= , == , !=

#Logical Operators
# and - or - not

#Conditional Operators
'''
if (condition):
    do this
elif (condition):
    do that
else:
    do the other
'''
'''
--- Nested if ---
if (condition):
    do this
    if (another condition):
        do that
    else:
        do the other
else:
    do the other other
'''

height = int(input("What is your height in cms? "))
age = int(input("What is your age? "))
bill = 0

if height > 120:
    print("\nYou can ride the rollercoaster!")
    if age < 12:
        bill = 5
        print(f"Ticket price is ${bill}.")
    elif age < 18:
        bill = 7
        print(f"Ticket price is ${bill}.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be okay.\nHave a free ride on us!")
    else:
        bill = 12
        print(f"Ticket price is ${bill}.")

    wants_photo = input("\nDo you want a photo taken ($3)? Y or N: ")
    if wants_photo == 'Y' or 'y':
        bill += 3

else:
    print("Sorry, you have to grow taller before you can ride.")

print(f"Your final bill is {bill}.")