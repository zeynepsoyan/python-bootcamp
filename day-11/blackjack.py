# Breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
import os
import art

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def check_winner(user_score, dealer_score):
    if user_score > 21:
        return "You went over. You lose 😤"
    elif user_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, dealer has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif dealer_score > 21:
        return "Dealer went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():

    print(logo)

    user_hand = []
    dealer_hand = []
    is_game_over = False

    for _ in range(2):
        user_hand.append(deal_card())
        dealer_hand.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"    Your cards: {user_hand}, current score: {sum(user_hand)}")
        print(f"    Dealer's first card: {dealer_hand[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                user_hand.append(deal_card())
            else:
                is_game_over = True        
        
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
        
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(check_winner(user_score, dealer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clearConsole()
    play_game()