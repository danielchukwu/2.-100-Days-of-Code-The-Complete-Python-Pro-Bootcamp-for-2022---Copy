# Python - 3.10
# Topic - Multiple if statements
# program - 


# if else

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
   print("You can ride the rollercoaster!")
   age = int(input("What is your age? "))
   bill = 0

   if (age <= 18):
      print("your bill is $5.")
      bill = 5
   elif (age > 18):
      print("your bill is $7.")
      bill = 7
   else:
      print("your bill is $12.")
      bill = 12

   wants_photo = input("Do you want a photo taken? Y or N. ")
   if wants_photo == "Y":
      bill += 3

   print(f"your final bill is {bill}")
else: 
   print("Sorry, you have to grow taller before you can ride.")