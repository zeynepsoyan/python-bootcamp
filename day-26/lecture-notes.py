# List Comprehension
# new_list = [new_item FOR item IN list IF test]

# old way
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# using list comprehension
comprehension_list = [n + 1 for n in numbers]
print(comprehension_list)

# string comprehension
name = "Zeynep"
new_name = [letter for letter in name]
print(new_name)

# double range challange
new_range = [n*2 for n in range(5)]
print(new_range)

# conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)


# Dictionary Comprehension
# new_dict = {new_key:new_value FOR item IN list}
# new_dict = {new_key:new_value FOR (key,value) IN dict.items()}
# new_dict = {new_key:new_value FOR (key,value) IN dict.items() IF test}

import random 

student_scores = {student:random.randint(0,100) for student in names}
print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score >= 50}
print(passed_students)

# Iterate over pandas Dataframe
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)

# Loop through columns
for (key, value) in student_df.items():
    print(key)
    print(value)

# Loop through rows
for (index, row) in student_df.iterrows(): # row is a Series object
    print(index)
    print(row.student)
    print(row.score)