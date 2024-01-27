import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+', '@', '?']

print("Welcome to Password Generator ver. 1.0.0 !!!")
number_of_letters = int(input("How many letters do you want in your password?\n"))
number_of_digits = int(input("How many numbers do you want in your password?\n"))
number_of_symbols = int(input("How many special symbols do you want in your password?\n"))

password_list = []

for char in range(1, number_of_letters + 1):
    random_char = random.choice(letters)
    password_list.append(random_char)
for char in range(1, number_of_digits + 1):
    random_char = random.choice(digits)
    password_list.append(random_char)
for char in range(1, number_of_symbols + 1):
    random_char = random.choice(symbols)
    password_list.append(random_char)

random.shuffle(password_list)
password_string = ""

for element in password_list:
    password_string += element

print(f"Your password is: \33[31m{password_string}")
