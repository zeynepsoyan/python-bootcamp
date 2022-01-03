import os
import art

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def find_highest_bidder(bidders):
    highest_bidder = ""
    highest_bid = 0
    for key in bidders:
        if bidders[key] > highest_bid:
            highest_bidder = key
            highest_bid = bidders[key]
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


print(art.logo)
print("Welcome to the secret auction program.")

bidders = {}
other_bidders = True

while other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid? $"))
    check_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    bidders[name] = bid

    if check_bidders == 'no':
        other_bidders = False
        find_highest_bidder(bidders)  
    else:
        clearConsole()