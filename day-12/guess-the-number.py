from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
NUMBER = randint(1,100)

def check_guess(guess):
    """Checks answer against guess, returns True if the guess is right."""
    if guess == NUMBER:
        return True
    elif guess > NUMBER:
        print("Too high.")
        return False
    else:
        print("Too low.")
        return False  

def set_difficulty():
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 and 100.")
    print(f"Psst, the correct answer is {NUMBER}")

    attempts = set_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if check_guess(guess):
            print(f"You got it! The answer was {NUMBER}.")
            return
        
        attempts -= 1

        if attempts == 0:
            print("You've run out of guesses, you lose.")
        else: 
            print("Guess again.")

game()