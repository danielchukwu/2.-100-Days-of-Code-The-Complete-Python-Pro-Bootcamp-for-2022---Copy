# Python - 3.10
# Topic - Data Types
# program - write a program that adds the digits in a 2 digit number. 
#           e.g. if the input was 35, then the output should be 3 + 5 = 8


# program - 

# recieve input of number
number_in_string = input("Enter any 2-digit number:")

# split 2-digits into individual variables
first_digit = number_in_string[0]
second_digit = number_in_string[1]

# Add 2-digits together
result = int(first_digit) + int(second_digit)

# print result
print("Ans:",result)