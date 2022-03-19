# Python - 3.10
# Topic - Split The Bill Program
# program - write a program which will select a random name from a list of names. The person selected
#           will have to pay for everybody's food bill

# Note: You are not allowed to use the choice() function
# Hint: use split().

# program - done✅
import random

# intro
print("\nPICK WHO PAYS FOR DINNER - PROGRAM")
print("Give me everybody's name seperated by a comma. ")

# input: recieve several names seperated by a comma e.g daniel, gabe, john, tony
names = input('Enter names: ')

# process:
# 1st: split names into a list data structure
names_list = names.split(', ')

# 2nd: get length of list
no_of_names = len(names_list)

# 3rd: use random.randint(a, b) to get a number between 0 and list length of the list
number = random.randint(0, no_of_names-1)

# 4th: get a name from the list
name = names_list[number]


# output: display result
print(f"The person who pays for dinner is {name}")
