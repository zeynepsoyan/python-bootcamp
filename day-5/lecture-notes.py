# For loop
fruits = ["Apple","Peach","Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

# For loop with range
# print numbers from 1 to 10 incrementing by 3
for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)