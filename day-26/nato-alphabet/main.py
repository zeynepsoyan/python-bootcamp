#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter:row.code for (index, row) in data.iterrows()}
word = input("Enter word: ").upper()
nato_list = [code_dict[letter] for letter in word]
print(nato_list)