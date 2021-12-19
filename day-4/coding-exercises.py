import random

# 1 - Random Exercise
'''
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
'''
side = random.randint(0,1)

if side:    #side == 1
    print("Heads")
else:
    print("Tails")

# 2 - Banker Roulette - Who will pay the bill?

names_str = input("Give me everybody's names, seperated by ', ' : ")
names = names_str.split(", ")

person = names[random.randint(0, len(names)-1)]
print(f"{person} is going to pay the bill today. Bon Appétit!\n")

#short way
#   person = random.choice(names)

# 3 - Treasure Map

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
column, row = int(position[0])-1, int(position[1])-1

map[row][column] = 'X'

print(f"{row1}\n{row2}\n{row3}")
