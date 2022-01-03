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


def compare(a, b, guess):
    if guess == 'A' and a['follower_count'] >= b['follower_count']:
        return True
    elif guess == 'B' and a['follower_count'] <= b['follower_count']:
        return True
    else:
        return False

def play_game():

    print(art.logo)
    score = 0

    is_guess_correct = True

    while is_guess_correct:
        a = random.choice(data)
        b = random.choice(data)

        print("Debug:", a['name'], a['follower_count'])
        print("Debug:", b['name'], b['follower_count'])

        print(f"Compare A: {a['name']}, a(n) {a['description']}, from {a['country']}.")
        print(art.vs)
        print(f"Compare B: {b['name']}, a(n) {b['description']}, from {b['country']}.")

        guess = input("Who has more followers? Type 'A' or 'B': ")
        is_guess_correct = compare(a, b, guess)

        clearConsole()
        print(art.logo)
        if is_guess_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")


play_game()