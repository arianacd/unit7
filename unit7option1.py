# by Ariana Daney
# last modified november 12, 2019
# this program lets the user code or decode a word from rearranging the alphabet however much the user wants


alphabet = "abcdefghijklmnopqrstuvwxyz"
encoded_word = []
decoded_word = []


def shift():
    """
    this function shifts the alphabet the number of times the user chooses
    :return: the shifted alphabet
    """
    user_shift = int(input("how many units do you want to shift the alphabet, choose a number from 1 to 25"))
    first = alphabet[0:user_shift]
    second = alphabet[user_shift:]
    alphabet2 = second + first
    return alphabet2


def encode():
    """
    this function takes a word or sentence from the user and encodes it using the shifted alphabet
    :return: nothing
    """
    new_alphabet = shift()
    user_word = input("please enter a word to encode")
    user_word = user_word.lower()
    final_encoded_word = ""
    for letter in user_word:
        if letter not in alphabet:
            encoded_word.append(letter)
        else:
            position = alphabet.index(letter)
            final_position = new_alphabet[position]
            encoded_word.append(final_position)
        final_encoded_word = "".join(encoded_word)
    print(final_encoded_word)


def decode():
    """
    this function takes letters, words, or sentences from the user and decodes it using the shifted alphabet
    :return: nothing
    """
    new_alphabet = shift()
    user_decode_word = input("please enter a word to decode")
    user_decode_word = user_decode_word.lower()
    final_decoded_word = ""
    for letter in user_decode_word:
        if letter not in alphabet:
            decoded_word.append(letter)
        else:
            position = new_alphabet.index(letter)
            final_position = alphabet[position]
            decoded_word.append(final_position)
        final_decoded_word = "".join(decoded_word)
    print(final_decoded_word)


def main():
    while True:
        user_input = input("please enter e to encode, d to decode, or q to quit")
        if user_input == "e":
            encode()
        elif user_input == "d":
            decode()
        elif user_input == "q":
            print("good bye!")
            break


main()
