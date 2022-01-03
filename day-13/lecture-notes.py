############DEBUGGING#####################

# Describe Problem
## Problem: It doesn't print when it reaches to the end of the loop.
## Solution: Range is exclusive on the upper bound.
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
## Problem: IndexError
## Solution: Randint returns number between 1-6. But Python list indices are between 0-5
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Play Computer
## Problem: 1994 doesn't print anything.
## Solution: Create a condition with equality to 1994.
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# Fix the Errors
## Indentation error
## String-int comparison error (TypeError)
## f-String
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")

# Print is Your Friend
## Problem: Double equation "for word_per_page"
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)

# Use a Debugger
## Problem: Indentation
## Solution: Indent b_list.append() to be inside the for loop
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])