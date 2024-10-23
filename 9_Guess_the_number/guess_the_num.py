import random
from art import logo

print(logo)

# Global Variable
EASY_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 10


# 3. Function to check users guess against actual answer
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too High.")
    elif user_guess < actual_answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {actual_answer}")

# 4. Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #1.  Choosing a random number between 1 to 100
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 to 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the nmumber.")

    guess = 0
    while guess != answer:
    # 2.Let the user guess a number
        guess = int(input("Make a guess: "))
        check_answer(guess, answer)

game()