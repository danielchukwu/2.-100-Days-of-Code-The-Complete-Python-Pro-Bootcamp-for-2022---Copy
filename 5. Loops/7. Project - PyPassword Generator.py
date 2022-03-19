# Python - 3.10
# Topic - PyPassword Generator Project
# program - write a program that askes
#           1. How many letters would you like in your password?
#              14
#           1. How many symbols would you like?
#              3
#           3. How many numbers would you like?
#              4
#           5. Here is your password: 4FW*K8x4%Y8VwKfMxKu(


# program - done✅
from math import floor
import random

print(['m', 'y', ' ', 'l', 'o', 'v', 'e'])


# intro:
print("\nPYPASSWORD GENERATOR - PROJECT")

# variables: letters = [...], symbols = [...], numbers= [...]
letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(' ')
numbers = "0 1 2 3 4 5 6 7 8 9".split(' ')
symbols = "! # $ % ( ) * +".split(' ')
# print(f"Letters = {letters}\nNumbers{numbers}\nSybols{symbols}")


# input: letters, numbers and symbols
nr_letters = int( input("How many letters would you like in your password?\n") )
nr_numbers = int( input("How many symbols would you like?\n") )
nr_symbols = int( input("How many numbers would you like?\n") )

# needed variables: a list that holds all the combination 
password = []

# process:
# 1st: get random values for letters, numbers, symbols and append into a list
for _ in range(0, nr_letters):
   random_letter = random.choice(letters)
   password.append(random_letter)

for _ in range(0, nr_numbers):
   random_number = random.choice(numbers)
   password.append(random_number)

for _ in range(0, nr_symbols):
   random_symbol = random.choice(symbols)
   password.append(random_symbol)

# 2nd: shuffle the list
# print(f"prev_password = {password}")
random.shuffle(password)
# print(f"password = {password}")

#3rd: needed variable: string variable to store the password
password_found = "".join(password)


# output:
print(f"New password is {password_found}")