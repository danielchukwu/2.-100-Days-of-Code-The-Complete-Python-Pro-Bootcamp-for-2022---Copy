# Python - 3.10
# Topic - Range () function
# program - this is used with for loop to iterate through a range of numbers



# learning - 

# logic 1: takes 2 arguments where 1 is inclusive but 10 is not. and steps by 1
print("\nRange() function: with 2 arguments")
for number in range(1, 10):
   print(number)

# logic 2: range() can also take 3 arguments where the 3rd argument is the step. 
print("\nRange() function: with 3 arguments")
for number in range(1, 10, 2):
   print(number)

# STORY TIME:
# One time in history gauss's school teacher gave him an assignment to add up all the number from 1 to 100
# e.g 1 + 2 + 3 + 4 .... 99 + 100
# and report the result
# Assignment: Get the result of this using python
print("\nSUMATION OF NUMBERS BETWEEN 1 - 100")
total = 0
for number in range(1, 100):
   total += number

print(total)