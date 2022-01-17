# Higher order functions
# Calculator

from ast import Add


def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2, func):
    return func(n1, n2)


print(calculator(8, 2, add))
print(calculator(8, 2, substract))
print(calculator(8, 2, multiply))
print(calculator(8, 2, divide))