import random

rock = "Rock"

paper ="Paper"

scissor ="Scissor"

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors.\n"))
computer_choice = random.randint(0, 2)
print(f"Computer Chose: {computer_choice}")

if user_choice