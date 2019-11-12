# by Ariana Daney
# last modified november 12, 2019
# this program lets the user code or decode a word from rearranging the alphabet however much the user wants


alphabet = "abcdefghijklmnopqrstuvwxyz"
encoded_word = []


def shift():
    user_shift = int(input("how many units do you want to shift the alphabet"))
    first = alphabet[0:user_shift]
    second = alphabet[user_shift:]
    alphabet2 = second + first
    return alphabet2


def encode(new_alphabet):
    user_word = input("please enter a word to encode")
    user_word = user_word.lower()
    for letter in user_word:
        position = alphabet.index(letter)
        final_position = new_alphabet[position]
        encoded_word.append(final_position)
        final_encoded_word = "".join(encoded_word)
    print(final_encoded_word)


def main():
    new_alphabet = shift()
    input("please enter e to encode, d to decode, or q to quit")
    if e
    encode(new_alphabet)


main()
