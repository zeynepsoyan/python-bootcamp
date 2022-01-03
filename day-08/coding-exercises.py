# Paint Area Calculator

import math

def paint_calc(height, width, cover):
    num_cans = math.ceil((height * width) / cover)
    print(f"You'll need {num_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Prime Numbers

def prime_checker(number):
    result = "It's a prime number."
    for num in range(2, number):
        if number % num == 0:
            result = "It's not a prime number."
    print(result)

n = int(input("Check this number: "))
prime_checker(number=n)