# python random library uses the current time stamp for the seed

import random

random_int = random.randint(1, 100) #generates a random integer between 1 an 100 (inclusive)
random_float = random.random()  #generates a float between 0 and 1 (1 exlusive)
random_float * 5    #random float between 0 and 5 (5 exlusive)

# we can change the sees as follows
#   random.seed(123) 
#   test_seed = int(input("Create a seed number: "))
# but this will always produce the same number, not random

#lists

fruits = ["Cherry", "Apple", "Pear"]
print(fruits[0])    #will print Cherry because computers start to count from 0
print(fruits[-1])   #this will print the last item from the list

fruits[0] = "Sherry"
print(fruits[0])    #we have manipulated the first element of the list

fruits.extend(["Apple", "Watermelon"])
print(fruits)

#split()
print("A, B, C, D".split(", ")) #splits the  string according to the parameter and returns a string

#choice()
print(random.choice(fruits)) #chooses a random element from a given list

#nested lists
vegetables = ["Spinach, Kale, Lettuce, Carrot"]
dirty_dozen = [fruits, vegetables]