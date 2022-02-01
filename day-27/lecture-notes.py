# Unlimited Arguments

def add(*args):
    # print(args)
    # print(type(args))
    # print(args[0])
    result = 0
    for n in args:
        result += n
    return result

print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6,7,8,9,10))


# Keyworded Arguments

def calculate(n, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)

# Example

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)

