import random

word_list = ["manikandan", "dhanya", "vigneshwari"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print(letter)
    else:
        print("-")
