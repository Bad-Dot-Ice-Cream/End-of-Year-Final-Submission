import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '/', '~', '*', '+']

print("\nWelcome to the Python Password Generator!")
print("-------------------------------------------------")
nr_letters = int(input("How many letters would you like in your password?\n>  "))
nr_numbers = int(input("How many numbers would you like in your password?\n>  "))
nr_symbols = int(input("How many symbols would you like in your password?\n>  "))

password_list = []

# Finding letters
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Finding numbers
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

# Finding symbols
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print("-------------------------------------------------")
print(f"Your password is:\n   {password} \nThanks for stopping by!")