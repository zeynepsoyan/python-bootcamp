# Dictionaries{Key:Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    123: "Some numbers"}

print(programming_dictionary["Bug"]) # Beware of key errror
print(programming_dictionary[123])

programming_dictionary["Loop"] = "The action of doing sometihing over and over again."
print(programming_dictionary)

empty_dictionary = {}
# programming_dictionary = {}
# print(programming_dictionary)

# edit the value if the key exists, add a new entry if not
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

travel_log2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

travel_log3 = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
        },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
        }
]