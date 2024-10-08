import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the python Password Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# Easy Level

# password = ""

# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range (0, nr_numbers):
#     password += random.choice(numbers)

# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# print(password)

# Hard Level
password_List = []

for char in range(0, nr_letters):
    password_List.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_List.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password_List.append(random.choice(symbols))

random.shuffle(password_List)

password=""
for char in password_List:
    password += char

print(f"Your password is: {password}")



