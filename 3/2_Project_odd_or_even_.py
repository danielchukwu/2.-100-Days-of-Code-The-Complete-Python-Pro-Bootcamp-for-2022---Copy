# Python - 3.10
# Topic - Odd or Even Program
# program - create a program that recieves an input and determines if it is an odd number or an even number
# Key tool - Modulo Operator %


# program - done✅

# intro
print("EVEN OR ODD PROGRAM")

# input: Enter a number
number = float(input("Enter a number? "))

# process: determine if it is odd or even
check = number % 2

# output: display in f-String
# print(check)
if (check == 0):
   print('This is an Even Number!')
else:
   print('This is an Odd Number!')
