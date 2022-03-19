# Python - 3.10
# Topic - Nested if else conditional statement and elif
# program - using if else conditional statement to run specific blocks of code while skiping the other


# if else

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
   print("You can ride the rollercoaster!")
   age = int(input("What is your age? "))
   if (age <= 18):
      print("Please pay $7.")
   elif (age > 18):
      print("Please pay $12.")
else: 
   print("Sorry, you have to grow taller before you can ride.")