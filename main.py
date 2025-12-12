alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction in ["encode", "decode"]:
        break

text = input("Type your message:\n").lower()

while True:
    try:
        shift = int(input("Type the shift number:\n"))
        break
    except ValueError:
        print("\nPlease enter a valid number\n")

def caesar(original_text, shift_amount, direction):
    text_lst = list(original_text.lower())

    for index, letter in enumerate(text_lst):

        if letter in alphabet:
            if direction == "encode":
                shifted_letter_index = alphabet.index(letter) + shift_amount
            elif direction == "decode":
                shifted_letter_index = alphabet.index(letter) + -shift_amount
            
            while shifted_letter_index > 25: # this will handle cases where the shifted index exceeds the list length
                shifted_letter_index -= 26
            
            text_lst[index] = alphabet[shifted_letter_index]
        else:
            continue
    result = "".join(text_lst)
    print(result)

caesar(text, shift, direction)
