# Python - 3.10
# Topic - Sum of Even Numbers Program from 1-100
# program - write a program that calculates the sum of all the even numbers from 1 to 100, 
#           including 1 and 100


# program - done✅

# intro
print("\nSUM OF EVEN NUMBERS(1 - 100) - PROGRAM")

# needed: variable to store addition of even numbers
total = 0

# process
for number in range(2, 101, 2):
   print(number)
   total += number

# output:
print(f"The total sum of even numbers between 1 - 100 is {total}\n")



# OR
total = 0

for number in range(1, 101):
   if number % 2 == 0:
      print(number)
      total += number

# output:
print(f"The total sum of even numbers between 1 - 100 is {total}\n")