# by ariana daney
# last modified november 6, 2019
# unit 7 daily exercises

# ex. 1
original = "abcdefghij"
first = original[0:3]
last = original[3:]
final = first + last

print(final)

# ex. 2
word = "Python"
for character in word:
    print(character)

# ex. 3


def without_end(words):
    words = words[1:-1]
    return words


print(without_end("Hello"))
print(without_end("python"))
print(without_end("coding"))


# ex. 4
def longest(list_of_words):
    longest_word = ""
    for x in list_of_words:
        if len(x) > len(longest_word):
            longest_word = x
    return longest_word


print(longest(["cat", "dog", "ant"]))

# ex. 5


def upper_lower():
    user_word = input("please enter a word")
    print(user_word.upper())
    print(user_word.lower())


upper_lower()

# ex. 6


def title_case():
    user_word = input("please enter a word")
