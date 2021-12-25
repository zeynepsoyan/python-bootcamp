import random
import hangman_art, hangman_words
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
guessed_letters = []
game_over = False
lives = 6

display = []
for _ in range(word_length):
    display.append("_")

# Testing the code
print(f"Psst, the word is {chosen_word}")

while not game_over:
    guess = input("Guess a letter: ").lower()
    clearConsole()
    if guess not in guessed_letters:
        guessed_letters.append(guess)

        if guess not in chosen_word:
            lives -= 1
            print(f"The letter {guess} is not in the word. You've got {lives} lives left.")
            if lives == 0:
                game_over = True
                print("You lose.")
        else:
            for letter_index in range(word_length):
                if chosen_word[letter_index] == guess:
                    display[letter_index] = guess

    else:
        print(f"You've already guessed {guess}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("Congrats! You won.")
    
    print(hangman_art.stages[lives])