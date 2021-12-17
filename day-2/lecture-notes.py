#Primitive Data Types

#String
print("Hello"[4])
print("123" + "456")

#Integer
print(123 + 456)
# len(123) -> TypeError: object of type 'int' has no len() 

#Float
my_float = 3.14159
another_float = 7_234_345.45    # = 7234345.45 : to increase readibility

#Boolean
True
False

#type() to know the type

print(type("This is a string"))
print(type(123456))
print(type(12.456))
print(type(True))

#type-casting = type-conversion

print(type(str(123)))
print(type(int("123456")))
print(10 + float("100.5"))
print(str(12) + str(12.4456))

#Mathematical Operations

print(2 + 5)
print(7 - 4)
print(6 / 3)    #always returns a float
print(2 ** 3)   #exponential

#PEMDAS-LR (left-to-right) = () , ** , *  / , +  -  

#rounding

print(round(2.88888), 2)    #two digits after .
print(7 // 3)   #will do integer division

#formatting strings - !!

score = 0
score += 1

isWinning = True

print(f"Your score is {score}, you are winning is {isWinning}")