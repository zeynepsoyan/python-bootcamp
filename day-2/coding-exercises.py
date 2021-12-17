# 1 - Data Types

two_digit_number = input("Type a two digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
total = first_digit + second_digit
print("The sum of digits is: " + str(total))

# 2 - BMI Calculator

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)

print("Your BMI index is: ", round(bmi, 1))

# 3 - Life in Weeks

max_age = 90
age = int(input("What is your current age? "))

years_left = (90 - age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

message = f"You have {days_left} days, {weeks_left} weeks, {months_left} months left on earth."
print(message)