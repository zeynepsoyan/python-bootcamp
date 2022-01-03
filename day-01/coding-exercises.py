# 1 - Printing
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


# 2 - Debugging Practice
'''
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
 print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
'''
#Missing double quotes before the word Day.
print("Day 1 - String Manipulation")

#Outer double quotes changed to single quotes.
print('String Concatenation is done with the "+" sign.')

#Extra indentation removed
print('e.g. print("Hello " + "world")')

#Extra ( in print function removed.
#SyntaxError: unexpected EOF while parsing -> unclosed brackets
print("New lines can be created with a backslash and n.")


# 3 - Input Function
print("Your name has " + str(len(input("2. What is your name? "))) + " characters\n")


# 4 - Variables
a = input("a: ")
b = input("b: ")

a, b = b, a

# --- OR ---
'''
c = a
a = b
b = c
'''

print("a: " + a)
print("b: " + b)

#Variable naming: Separate with underscore -> user_name