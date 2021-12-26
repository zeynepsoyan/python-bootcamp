# creates a new variable within the scope of the function
# name (parameter) = "Zeynep" (argument)
def greet_with_name(name):
    print( f"Hello {name}")
    print( f"How do you do {name}?")

greet_with_name("Zeynep")

# functions with more than one inputs
def  greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# call the function with positional arguments
greet_with("Zeynep", "Zurich")

# call the function with keyword arguments
greet_with(location="Zurich", name="Zeynep")