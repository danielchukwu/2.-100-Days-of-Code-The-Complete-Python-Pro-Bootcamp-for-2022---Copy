# Python - 3.10
# Topic - Pizza Ordering program
# program - Congratulations, you've got a job at Python Pizza. Your first job is to build 
#           an automatic pizza order program.
# Based on a user's order, work out their final bill:
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# pepperoni for small pizza: +$2
# pepperoni for medium and large pizza: +$3

# extra cheese for any size: +1




# program - done✅

# intro
print("\nWelcome to Python Pizza Deliveries!")

# prerequisite variables
bill = 0

# input: size
size = input("What size of pizza do you want? S, M, L. ").upper()

# input: add pepperoni
add_pepperoni = input("Do you want pepperoni?. Y or N. ").upper()

# input: extra cheese
extra_cheese = input("Do you want extra cheese?. Y or N. ").upper()


# process: order processing

# 1st: size
if size == "S":
   print("Small Pizza is $15")
   bill = 15
elif(size == "M"):
   bill = 20
   print("Medium Pizza is $20")
elif(size == "L"):
   bill = 25
   print("Large Pizza is $25")

# 2nd: add_pepperoni
if add_pepperoni == "Y" and size == "S":
   print("+$2 - addeed pepperoni")
   bill += 2
elif add_pepperoni == "Y" and (size == "M" or size == "L"):
   print("+$3 - addeed pepperoni")
   bill += 3

# 3rd: extra_cheese
if extra_cheese == "Y":
   print("+$1 - added extra cheese")
   bill+=1


# output: display result
print(f"your final bill is ${bill}")

