# Average Height
# cannot use len() and sum() functions

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

count = 0
total_height = 0
for h in student_heights:
    total_height += h           #len(student_heights)
    count += 1                  #sum(student_heights)

average = round(total_height/count)
print(average)

# High Score
# cannot use max() function

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print("The highest score in the class is:", max_score)

# Adding Even Numbers

total = 0
for number in range(2, 101, 2):
    total += number

# for number in range(1, 101):
#     if number % 2 == 0:
#       total += number

print(total)

# FizzBuzz

for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)