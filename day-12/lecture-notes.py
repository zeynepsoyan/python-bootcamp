# Scope 
enemies = "Skeleton"

def increase_enemies():
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Modifying Global Variables 1st way (not very good)
enemies = "Skeleton"

def increase_enemies():
    global enemies
    enemies = "Zombie"
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Modifying Global Variables 2nd way
enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# Global Constants
# used for generally non-changeable values
URL = "https://www.google.com"
TWITTER_HANDLE = "@zeynoso"


# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
#print(potin_strength)


# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(potion_strength)
        print(player_health)

    drink_potion()

print(player_health)


# There is no Block Scope
game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    
    print(new_enemy)
