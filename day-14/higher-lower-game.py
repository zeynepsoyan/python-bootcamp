# Play here: http://www.higherlowergame.com/

import random
import os
import art
from game_data import data

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def format_data(account):
    """Takes the account data and returns the printable format."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a(n) {description}, from {country}."

def check_guess(a_followers, b_followers, guess):
    """Takes the account followers and user guess, and returns True if the answer is correct."""
    if a_followers >= b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

def play_game():

    print(art.logo)

    score = 0
    is_guess_correct = True
    b = random.choice(data)

    while is_guess_correct:

        a, b = b, random.choice(data)
        while a == b:
            b = random.choice(data)

        print("Debug:", a['name'], a['follower_count'])
        print("Debug:", b['name'], b['follower_count'])

        print(f"Compare A: {format_data(a)}.")
        print(art.vs)
        print(f"Against B: {format_data(b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_guess_correct = check_guess(a['follower_count'], b['follower_count'], guess)

        clearConsole()
        print(art.logo)
        if is_guess_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")


play_game()