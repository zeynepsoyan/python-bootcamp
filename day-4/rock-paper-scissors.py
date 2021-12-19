import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand = [rock, paper, scissors]

print("Welcome to the Rock, Paper Scissors game. You are playing against a computer. Which has no arms or hands. Would be such a shame if you lost...\n")
user_choice = int(input("So which will you choose? Rock (0), Paper (1) or Scissors (2)? "))
comp_choice = random.choice([0,1,2])

if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number")
else:
    print("You chose: \n", hand[user_choice])
    print("Computer chose: \n", hand[comp_choice])
    
    if user_choice == comp_choice:
        print("It's a draw")
    elif user_choice == 0 and comp_choice == 1 or user_choice == 1 and comp_choice == 2 or user_choice == 2 and comp_choice == 1:
        print("You lose")
    else:
        print("You win")


