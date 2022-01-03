import art

""" 
def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = (alphabet.index(letter) + shift) % len(alphabet)
        cipher_text += alphabet[position]
    print(f"The encoded text is {cipher_text}")

def decrypt(text, shift):
    plain_text = ""
    for letter in text:
        position = (alphabet.index(letter) - shift) % len(alphabet)
        plain_text += alphabet[position]
    print(f"The decoded text is {plain_text}") 
"""

def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = (alphabet.index(char) - shift) % len(alphabet)
            end_text += alphabet[position]
        else:
            end_text += char
    print(f"The {cipher_direction}ed text is {end_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(text, shift, direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye!")


""" 
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift) 
"""