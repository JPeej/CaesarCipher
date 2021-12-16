
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# The function caesar performs the shift encryption or shift decryption.
# It will first iterate through the provided message on each character.
# If the character is not in the alphabet it will be immediately added to the correct index within cipher_text.
# If the character is in the alphabet it will then run through either the encode or decode if statement.
# Each uses a variable called position to determine the index position of the iterated character in the alphabet list.
# Some protections are put in to wrap through either side of the list if the index after the shift is out of range.
# Finally, the program is repeated if requested.

def caesar(cipher_start, shift_amount, cipher_direction):
    cipher_text = ""
    for char in cipher_start:
        if char in alphabet:
            if cipher_direction == "decode":
                position = alphabet.index(char)
                if (position + shift_amount) > len(alphabet):
                    cipher_text += alphabet[(position + shift) % len(alphabet)]
                else:
                    cipher_text += alphabet[position + shift]
            else:
                position = alphabet.index(char)
                if (position + shift) < 0:
                    cipher_text += len(alphabet) - (shift_amount - position)
                else:
                    cipher_text += alphabet[position - shift]
        else:
            cipher_text += char
    print(f"Your {direction}d message is: {cipher_text}")

while True:
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(cipher_start = text, shift_amount = shift, cipher_direction = direction)
    if input("Repeat the program? (Y/N)").strip().upper() !='Y':
        break
