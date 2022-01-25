# 1- Squaring Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)

# 2- Filtering Even Numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)

# 3- Data Overlap
import csv
from os import set_inheritable

with open("./file1.txt") as file_1:
    numbers_1 = file_1.readlines()
with open("./file2.txt") as file_2:
    numbers_2 = file_2.readlines()

overlap = [int(num) for num in numbers_1 if num in numbers_2]
print(overlap)

# 4- Dictionary Comprehension 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split()
sentence_dict = {word:len(word) for word in sentence_list}
print(sentence_dict)

# 5- Dictionary Comprehension 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

def convert_f(temp_c):
    return (temp_c * 9/5) + 32

weather_f = {day:convert_f(temp_c) for (day, temp_c) in weather_c.items()}

print(weather_f)